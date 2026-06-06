import json
from openai import OpenAI
from backend.config import OPENAI_API_KEY, WRITER_MODEL


class WriterAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = WRITER_MODEL

    def _system(self, guidelines, resume_master, job_type, strategy):
        verb_limit = "max 2" if job_type == "fulltime" else "max 3"
        return f"""You are a resume writer. You ONLY execute the approved strategy. You do NOT decide what to write — the strategy tells you.

APPROVED STRATEGY:
{json.dumps(strategy, indent=2)}

GUIDELINES:
{guidelines}

CANDIDATE SOURCE (ONLY source — never invent tools, skills, or metrics not in this file):
{resume_master}

EXECUTION RULES:
1. Follow strategy: primary_role, role_essence, bullet_distribution, company_strategy, suppress list.
2. Every primary_skill needs at least one bullet proving hands-on use.
3. Suppress list = DO NOT MENTION anywhere.
4. Bullet distribution percentages control the mix of engineering vs support bullets.
5. ADAPTATION: If JD asks for a tool with equivalent experience, describe the same work using JD's tool. Be specific.
6. BELIEVABILITY: One responsibility, one method, one outcome per bullet.
7. 60%+ bullets end with purpose clause: enabling, supporting, improving, reducing, delivering, ensuring.
8. Verb variety: {verb_limit} repeats max across resume.
9. DO NOT copy or rephrase JD sentences into summary or descriptions. Write from the candidate's experience.
10. DO NOT invent skills not in the source file. If a tool is not in the source, do not mention it.
OUTPUT: ONLY valid JSON. No markdown. No explanation."""

    def _format_rules(self, job_type):
        """FORMAT RULES — placed in user prompt so the model prioritizes them."""
        if job_type == "contract":
            return """
═══ MANDATORY FORMAT — VIOLATING THESE IS A FAILURE ═══

summary: EXACTLY 7-10 bullets. Each bullet 25-40 words. Technical and specific. Do NOT use generic phrases like "proven track record" or "strong communicator." Do NOT rephrase JD sentences.

technical_skills: 7-9 categories. Each category has 3-8 items. Cloud = ONE combined category.

exp1_description: 2 sentences describing engineering scope. Do NOT start with "At [Company]." Start with action: "Led backend engineering for..." or "Designed and deployed..."

exp1 (Bee Data): EXACTLY 12-15 bullets. Each bullet 25-40 words. Every bullet must name a specific tool/pattern AND describe what it achieved.

exp1_env: Single line listing all tools used in exp1 bullets.

exp2_description: Same rules as exp1_description.
exp2 (Allied Health): EXACTLY 10-14 bullets. Each 25-40 words.
exp2_env: Single line.

exp3_description: Same rules.
exp3 (BYJU'S): EXACTLY 7-10 bullets. Each 25-40 words.
exp3_env: Single line.

exp4_description: Same rules.
exp4 (Cognizant): EXACTLY 7-10 bullets. Each 25-40 words.
exp4_env: Single line.

TOTAL BULLETS ACROSS ALL COMPANIES: minimum 40, maximum 50.
If your output has fewer than 40 bullets total, you have FAILED."""
        elif job_type == "fulltime":
            return """
═══ MANDATORY FORMAT — VIOLATING THESE IS A FAILURE ═══

summary: EXACTLY 5-8 bullets. Each 25-35 words. Technical, specific. No generic phrases.
technical_skills: 6-8 categories.
exp1 (Bee Data): EXACTLY 10-12 bullets. Each 25-35 words.
exp2 (Allied Health): EXACTLY 8-10 bullets. Each 25-35 words.
exp3 (BYJU'S): EXACTLY 6-9 bullets. Each 25-35 words.
exp4 (Cognizant): EXACTLY 5-7 bullets. Each 25-35 words.
NO description, env, or exp5 fields.
TOTAL: minimum 30, maximum 40 bullets."""
        else:  # gc
            return """
═══ MANDATORY FORMAT — VIOLATING THESE IS A FAILURE ═══

summary: EXACTLY 10-15 bullets. Each 25-35 words. Technical, specific.
technical_skills: 8-12 categories.
exp1 (Cardinal Health): EXACTLY 12-14 bullets. Each 25-35 words. exp1_env: single line.
exp2 (UBS): EXACTLY 12-14 bullets. Each 25-35 words. exp2_env: single line.
exp3 (MTA): EXACTLY 10-14 bullets. Each 25-35 words. exp3_env: single line.
exp4 (Cognizant): EXACTLY 10-14 bullets. Each 25-35 words. exp4_env: single line.
exp5 (Couth InfoTech): EXACTLY 10-14 bullets. Each 25-35 words. exp5_env: single line.
NO description fields. TOTAL: minimum 55, maximum 70 bullets."""

    def _keys(self, job_type):
        if job_type == "contract":
            return "summary, technical_skills, exp1_description, exp1, exp1_env, exp2_description, exp2, exp2_env, exp3_description, exp3, exp3_env, exp4_description, exp4, exp4_env"
        elif job_type == "fulltime":
            return "summary, technical_skills, exp1, exp2, exp3, exp4"
        return "summary, technical_skills, exp1, exp1_env, exp2, exp2_env, exp3, exp3_env, exp4, exp4_env, exp5, exp5_env"

    def write(self, jd, job_type, role_type, role_name, company_name, guidelines, resume_master, strategy):
        system = self._system(guidelines, resume_master, job_type, strategy)
        format_rules = self._format_rules(job_type)

        user = f"""Execute the approved strategy and write the resume.

JD: {jd}
JOB TYPE: {job_type} | ROLE: {role_type} | TITLE: {role_name} | COMPANY: {company_name}
JSON KEYS: {self._keys(job_type)}

{format_rules}

BEFORE RETURNING, COUNT YOUR BULLETS:
- Count exp1 bullets. Is it 12-15? If not, add more.
- Count exp2 bullets. Is it 10-14? If not, add more.
- Count total bullets. Is it 40+? If not, you have failed.
- Check each bullet length. Is every bullet 25-35 words? If any is under 20, expand it.

Return ONLY JSON."""

        return self._call(system, user)

    def rewrite(self, jd, job_type, role_type, role_name, company_name, guidelines, resume_master, strategy, draft, feedback):
        system = self._system(guidelines, resume_master, job_type, strategy)
        fb = self._fmt(feedback)
        format_rules = self._format_rules(job_type)

        exp_count = 5 if job_type == "gc" else 4
        has_desc = job_type == "contract"
        has_env = job_type in ("contract", "gc")
        keys = ["summary", "technical_skills"]
        for i in range(1, exp_count + 1):
            if has_desc: keys.append(f"exp{i}_description")
            keys.append(f"exp{i}")
            if has_env: keys.append(f"exp{i}_env")

        user = f"""Score was {feedback.get('ats_score', 'N/A')}/100. Fix the issues below.

SCORER FEEDBACK:
{fb}

PREVIOUS DRAFT:
{json.dumps(draft, indent=2)}

{format_rules}

RULES:
- Apply every suggested rewrite from the scorer.
- Expand short bullets to 25-35 words.
- If any section has too few bullets, ADD MORE from the resume source.
- Keep unflagged bullets unchanged.
- Still follow the approved strategy.
- Include ALL keys: {', '.join(keys)}

BEFORE RETURNING, COUNT YOUR BULLETS. Total must be 40+.
Return ONLY improved JSON."""

        return self._call(system, user, temp=0.2)

    def _call(self, system, user, temp=0.3):
        try:
            r = self.client.chat.completions.create(
                model=self.model, temperature=temp, max_completion_tokens=16000,
                response_format={"type": "json_object"},
                messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
            )
            return json.loads(r.choices[0].message.content.strip())
        except json.JSONDecodeError as e:
            raise ValueError(f"Writer returned invalid JSON: {e}")
        except Exception as e:
            print(f"Writer API Error: {e}")
            raise

    def _fmt(self, sf):
        p = []
        if sf.get("score_reasoning"): p.append(f"OVERALL: {sf['score_reasoning']}")
        for i, f in enumerate(sf.get("top_fixes", sf.get("top_3_fixes", [])), 1): p.append(f"  {i}. {f}")
        for it in sf.get("feedback", []):
            loc = it.get("section", "?")
            idx = it.get("bullet_index")
            if idx is not None: loc += f" bullet {idx}"
            p.append(f"\n  [{it.get('severity', '').upper()}] {loc}: {it.get('problem', '')}")
            if it.get("current_text"): p.append(f"    CURRENT: {it['current_text']}")
            if it.get("suggested_rewrite"): p.append(f"    REWRITE TO: {it['suggested_rewrite']}")
        for it in sf.get("missing_from_jd", []):
            p.append(f"  MISSING: {it.get('keyword', '')} ({it.get('jd_importance', '')}): {it.get('suggestion', '')}")
        return "\n".join(p)
