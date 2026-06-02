import json
from openai import OpenAI
from backend.config import OPENAI_API_KEY, WRITER_MODEL


class WriterAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = WRITER_MODEL

    def _system(self, guidelines, resume_master, job_type):
        return f"""You are an expert technical resume writer who produces believable, interview-safe, ATS-optimized resumes.

GUIDELINES:
{guidelines}

CANDIDATE SOURCE — your foundation, not your prison:
{resume_master}

═══ HOW TO USE THE SOURCE FILE ═══

The bullet banks are EXAMPLES of how to describe this candidate's real work. They are not copy-paste templates. You must ADAPT them to match the JD's language, tools, and emphasis.

ADAPTATION RULES:
1. If the JD asks for a tool the candidate used (e.g., FastAPI, Spark, PostgreSQL) — use it directly.
2. If the JD asks for a tool the candidate has equivalent experience with (e.g., JD says Tornado, candidate used FastAPI) — describe the same backend work using Tornado naturally. Do not mention FastAPI alongside it. Write as if Tornado was the tool used.
3. If the JD asks for a tool the candidate has NO experience with and NO equivalent — do not mention it. Do not fake it.
4. When adapting, be SPECIFIC. "Built Tornado-based async API services with WebSocket handlers for real-time data streaming" is believable. "Used Tornado" is not.

BELIEVABILITY TEST — apply to every bullet:
- Would this survive a 30-minute technical interview about this specific bullet?
- Does it name a real pattern, not just a tool category?
- Does it describe ONE clear responsibility with ONE outcome?
- Is it 20-30 words, not a run-on sentence with 6 tools crammed in?

BULLET WRITING:
- Each bullet: one responsibility + one technical method + one outcome/purpose
- Length: 20-30 words. Never under 15. Never a sentence fragment.
- 60% of bullets end with purpose clause: enabling, supporting, improving, reducing, delivering, ensuring
- Do NOT stack 5+ tools in one bullet. Split into two if needed.
- Vary verbs. Never repeat the same verb more than {"2 times" if job_type == "fulltime" else "3 times"} across the resume.

AI CONTENT CONTROL:
- Read the JD's AI Intensity. If the JD is about pipelines, APIs, or data platforms with zero AI mentions, use ZERO AI bullets.
- If the JD mentions LangChain or vector DBs as "preferred" (not required), use maximum 1-2 AI bullets across the entire resume.
- If the JD is clearly an AI role, use the AI lane fully.
- Do not lead with AI content for non-AI roles. Ever.

CLOUD: {"GC MODE: Clouds FIXED per company." if job_type == "gc" else "One cloud per company. OR condition = keep AWS default. Switch only when JD clearly emphasizes another cloud."}
SKILLS: Cloud = ONE category. Only list tools that appear in your bullets.
OUTPUT: Return ONLY valid JSON. No markdown fences. No explanation."""

    def _structure(self, job_type):
        if job_type == "contract":
            return """JSON keys: summary (6-10 bullets), technical_skills (category lines), exp1_description, exp1 (12-15 bullets), exp1_env, exp2_description, exp2 (10-14 bullets), exp2_env, exp3_description, exp3 (7-10 bullets), exp3_env, exp4_description, exp4 (7-10 bullets), exp4_env"""
        elif job_type == "fulltime":
            return """JSON keys: summary (5-8 bullets), technical_skills, exp1 (10-12 bullets), exp2 (8-10), exp3 (6-9), exp4 (5-7). NO description/env/exp5."""
        return """JSON keys: summary (10-15 bullets), technical_skills, exp1 (12-14 bullets), exp1_env, exp2 (12-14), exp2_env, exp3 (10-14), exp3_env, exp4 (10-14), exp4_env, exp5 (10-14), exp5_env. 5 companies, NO descriptions."""

    def write(self, jd, job_type, role_type, role_name, company_name, guidelines, resume_master):
        system = self._system(guidelines, resume_master, job_type)
        user = f"""Write a tailored resume for:

JOB DESCRIPTION:
{jd}

JOB TYPE: {job_type} | ROLE TYPE: {role_type} | ROLE NAME: {role_name} | COMPANY: {company_name}

STRUCTURE: {self._structure(job_type)}

BEFORE WRITING, silently answer:
1. What is the ACTUAL job being hired for? (not just the title)
2. What are the top 5 required skills?
3. What AI intensity does this JD have? (0=none, 1=light, 2=ML, 3=GenAI, 4=Agentic)
4. Which tools in the JD need adaptation from the source file?

Then write the resume. Return ONLY JSON."""

        return self._call(system, user)

    def rewrite(self, jd, job_type, role_type, role_name, company_name, guidelines, resume_master, draft, feedback):
        system = self._system(guidelines, resume_master, job_type)
        fb = self._fmt(feedback)

        exp_count = 5 if job_type == "gc" else 4
        has_desc = job_type == "contract"
        has_env = job_type in ("contract", "gc")
        keys = ["summary", "technical_skills"]
        for i in range(1, exp_count + 1):
            if has_desc: keys.append(f"exp{i}_description")
            keys.append(f"exp{i}")
            if has_env: keys.append(f"exp{i}_env")

        user = f"""Score was {feedback.get('ats_score', 'N/A')}/100. Fix these issues:

JD: {jd}
JOB TYPE: {job_type} | ROLE: {role_type} | TITLE: {role_name} | COMPANY: {company_name}

PREVIOUS DRAFT:
{json.dumps(draft, indent=2)}

SCORER FEEDBACK:
{fb}

Apply every suggested rewrite. Expand short bullets to 20-30 words. Keep unflagged bullets. Include ALL keys: {', '.join(keys)}
Return ONLY improved JSON."""

        return self._call(system, user, temp=0.2)

    def _call(self, system, user, temp=0.3):
        try:
            r = self.client.chat.completions.create(
                model=self.model,
                temperature=temp,
                max_tokens=8000,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            )
            content = r.choices[0].message.content.strip()
            return json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Writer JSON Error: {e}")
            raise ValueError(f"Writer returned invalid JSON: {e}")
        except Exception as e:
            print(f"Writer API Error: {e}")
            raise

    def _fmt(self, sf):
        p = []
        if sf.get("score_reasoning"): p.append(f"OVERALL: {sf['score_reasoning']}")
        for i, f in enumerate(sf.get("top_3_fixes", []), 1): p.append(f"  {i}. {f}")
        for it in sf.get("feedback", []):
            loc = it.get("section", "?")
            idx = it.get("bullet_index")
            if idx is not None: loc += f" bullet {idx}"
            sev = it.get("severity", "minor").upper()
            p.append(f"\n  [{sev}] {loc}: {it.get('problem', '')}")
            if it.get("current_text"): p.append(f"    CURRENT: {it['current_text']}")
            if it.get("suggested_rewrite"): p.append(f"    REWRITE TO: {it['suggested_rewrite']}")
        for it in sf.get("missing_from_jd", []):
            p.append(f"  MISSING: {it.get('keyword', '')} ({it.get('jd_importance', '')}): {it.get('suggestion', '')}")
        return "\n".join(p)