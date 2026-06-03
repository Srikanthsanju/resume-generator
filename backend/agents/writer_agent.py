import json
from openai import OpenAI
from backend.config import OPENAI_API_KEY, WRITER_MODEL


class WriterAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = WRITER_MODEL

    def _system(self, guidelines, resume_master, job_type, strategy):
        verb_limit = "max 2" if job_type == "fulltime" else "max 3"
        return f"""You are a resume writer. You do NOT decide strategy. The strategy has already been decided and approved. You ONLY execute it.

APPROVED STRATEGY (follow this exactly):
{json.dumps(strategy, indent=2)}

GUIDELINES:
{guidelines}

CANDIDATE SOURCE:
{resume_master}

═══ EXECUTION RULES ═══

1. FOLLOW THE STRATEGY. The primary_role, role_essence, bullet_distribution, company_strategy, and suppress list are YOUR instructions. Do not override them.

2. PRIMARY SKILLS must appear in bullets with proof. Every skill in primary_skills needs at least one bullet that demonstrates hands-on use.

3. SUPPRESS means DO NOT MENTION. If a skill is in the suppress list, it must not appear anywhere in the resume — not in summary, not in skills, not in bullets.

4. BULLET DISTRIBUTION controls the MIX. If strategy says 70% engineering, then 70% of bullets must be hands-on building/coding/pipelines, not documentation or governance.

5. COMPANY STRATEGY controls WHAT EACH COMPANY EMPHASIZES. Follow it.

6. ADAPTATION: If JD asks for a tool you have equivalent experience with (JD says Dataflow, you used Spark Streaming), describe the same work using the JD's tool naturally. Be specific — name patterns, not just tools.

7. BELIEVABILITY: Every bullet must survive a 30-minute interview. One responsibility, one method, one outcome. 20-30 words. No 5-tool stacking.

8. 60% of bullets end with purpose clause: enabling, supporting, improving, reducing, delivering, ensuring.

9. Verb variety: {verb_limit} repeats max across entire resume.

OUTPUT: Return ONLY valid JSON. No markdown. No explanation."""

    def _structure(self, job_type):
        if job_type == "contract":
            return "JSON keys: summary, technical_skills, exp1_description, exp1, exp1_env, exp2_description, exp2, exp2_env, exp3_description, exp3, exp3_env, exp4_description, exp4, exp4_env"
        elif job_type == "fulltime":
            return "JSON keys: summary, technical_skills, exp1, exp2, exp3, exp4. NO description/env/exp5."
        return "JSON keys: summary, technical_skills, exp1, exp1_env, exp2, exp2_env, exp3, exp3_env, exp4, exp4_env, exp5, exp5_env. 5 companies, NO descriptions."

    def write(self, jd, job_type, role_type, role_name, company_name, guidelines, resume_master, strategy):
        system = self._system(guidelines, resume_master, job_type, strategy)
        user = f"""Execute the approved strategy and write the resume.

JD: {jd}
JOB TYPE: {job_type} | ROLE: {role_type} | TITLE: {role_name} | COMPANY: {company_name}
STRUCTURE: {self._structure(job_type)}

Before writing, verify internally:
- Am I following the bullet_distribution percentages?
- Am I proving every primary_skill with at least one bullet?
- Am I suppressing everything in the suppress list?
- Am I following each company_strategy instruction?

Return ONLY JSON."""
        return self._call(system, user)

    def rewrite(self, jd, job_type, role_type, role_name, company_name, guidelines, resume_master, strategy, draft, feedback):
        system = self._system(guidelines, resume_master, job_type, strategy)
        fb = self._fmt(feedback)

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

RULES:
- Apply every suggested rewrite from the scorer.
- Expand short bullets to 20-30 words.
- Keep unflagged bullets unchanged.
- Still follow the approved strategy.
- Include ALL keys: {', '.join(keys)}
Return ONLY improved JSON."""
        return self._call(system, user, temp=0.2)

    def _call(self, system, user, temp=0.3):
        try:
            r = self.client.chat.completions.create(
                model=self.model, temperature=temp, max_tokens=8000,
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
