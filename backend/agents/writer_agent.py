import json
from backend.config import OPENAI_API_KEY, ANTHROPIC_API_KEY, WRITER_MODEL


class WriterAgent:
    def __init__(self):
        self.model = WRITER_MODEL
        self.is_claude = self.model.startswith("claude")

        if self.is_claude:
            from anthropic import Anthropic
            self.client = Anthropic(api_key=ANTHROPIC_API_KEY)
        else:
            from openai import OpenAI
            self.client = OpenAI(api_key=OPENAI_API_KEY)

    def _system(self, guidelines, resume_master, job_type):
        cloud_rule = ("GC MODE: Clouds FIXED per company. Cardinal Health=Azure, UBS=Azure/Snowflake, MTA=GCP, Cognizant=AWS, Couth=AWS." if job_type == "gc"
            else "One cloud per company. OR condition in JD = keep AWS default. Switch only when JD clearly emphasizes another cloud (5+ mentions or listed as required).")
        verb_limit = "max 2" if job_type == "fulltime" else "max 3"

        return f"""You are an expert technical resume writer who produces believable, interview-safe, ATS-optimized resumes.

GUIDELINES:
{guidelines}

CANDIDATE SOURCE — your foundation, not a copy-paste menu:
{resume_master}

═══ HOW TO USE THE SOURCE FILE ═══

The bullet banks show how to describe this candidate's real work. You must ADAPT them to match the JD's language, tools and emphasis.

ADAPTATION RULES:
1. If the JD asks for a tool the candidate used (FastAPI, Spark, PostgreSQL) — use it directly.
2. If the JD asks for a tool with equivalent experience (JD says Tornado, candidate used FastAPI) — describe the same backend work using Tornado naturally. Do not mention FastAPI alongside it.
3. If the JD asks for a tool with NO equivalent — do not mention it. Do not fake it.
4. When adapting, be SPECIFIC. "Built Tornado-based async API services with WebSocket handlers for real-time data streaming" is believable. "Used Tornado" is not.

BELIEVABILITY TEST for every bullet:
- Would this survive a 30-minute technical interview?
- Does it name a real pattern, not just a tool category?
- Does it describe ONE responsibility with ONE outcome?
- Is it 20-30 words, not a run-on with 6 tools crammed in?

BULLET WRITING:
- One responsibility + one technical method + one outcome/purpose
- Length: 20-30 words. Never under 15. Never a fragment.
- 60% of bullets end with purpose clause: enabling, supporting, improving, reducing, delivering, ensuring
- Do NOT stack 5+ tools in one bullet. Split if needed.
- Vary verbs. Max {verb_limit} repeats across resume.

AI CONTENT CONTROL:
- If JD has zero AI mentions → zero AI bullets.
- If JD mentions AI as "preferred" → max 1-2 AI bullets across entire resume.
- If JD is clearly an AI role → use AI lane fully.
- Never lead with AI content for non-AI roles.

CLOUD: {cloud_rule}
SKILLS: Cloud = ONE combined category. Only list tools that appear in bullets.
OUTPUT: Return ONLY valid JSON. No markdown. No explanation."""

    def _structure(self, job_type):
        if job_type == "contract":
            return """JSON keys: summary (6-10 bullets), technical_skills (category lines), exp1_description, exp1 (12-15 bullets), exp1_env, exp2_description, exp2 (10-14), exp2_env, exp3_description, exp3 (7-10), exp3_env, exp4_description, exp4 (7-10), exp4_env"""
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

BEFORE WRITING, silently decide:
1. What is the ACTUAL job? (not just the title)
2. Top 5 required skills?
3. AI intensity? (0=none, 1=light, 2=ML, 3=GenAI, 4=Agentic)
4. Which JD tools need adaptation from source?

Return ONLY JSON."""

        return self._call(system, user)

    def rewrite(self, jd, job_type, role_type, role_name, company_name, guidelines, resume_master, draft, feedback):
        system = self._system(guidelines, resume_master, job_type)
        fb = self._fmt(feedback)

        exp_count = 5 if job_type == "gc" else 4
        has_desc = job_type == "contract"
        has_env = job_type in ("contract", "gc")
        keys = ["summary", "technical_skills"]
        for i in range(1, exp_count + 1):
            if has_desc:
                keys.append(f"exp{i}_description")
            keys.append(f"exp{i}")
            if has_env:
                keys.append(f"exp{i}_env")

        user = f"""Score was {feedback.get('ats_score', 'N/A')}/100. Fix these issues:

JD: {jd}
JOB TYPE: {job_type} | ROLE: {role_type} | TITLE: {role_name} | COMPANY: {company_name}

PREVIOUS DRAFT:
{json.dumps(draft, indent=2)}

SCORER FEEDBACK:
{fb}

Apply suggested rewrites. Expand short bullets to 20-30 words. Keep unflagged bullets.
Include ALL keys: {', '.join(keys)}
Return ONLY improved JSON."""

        return self._call(system, user, temp=0.2)

    def _call(self, system, user, temp=0.3):
        try:
            if self.is_claude:
                r = self.client.messages.create(
                    model=self.model,
                    max_tokens=8000,
                    temperature=temp,
                    system=system,
                    messages=[{"role": "user", "content": user}],
                )
                content = r.content[0].text.strip()
                # Strip markdown fences if present
                if content.startswith("```"):
                    content = content.split("\n", 1)[1]
                if content.endswith("```"):
                    content = content[: content.rfind("```")]
                return json.loads(content.strip())
            else:
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
                return json.loads(r.choices[0].message.content.strip())

        except json.JSONDecodeError as e:
            print(f"Writer JSON Error: {e}")
            raise ValueError(f"Writer returned invalid JSON: {e}")
        except Exception as e:
            print(f"Writer API Error: {e}")
            raise

    def _fmt(self, sf):
        p = []
        if sf.get("score_reasoning"):
            p.append(f"OVERALL: {sf['score_reasoning']}")
        for i, f in enumerate(sf.get("top_3_fixes", []), 1):
            p.append(f"  {i}. {f}")
        for it in sf.get("feedback", []):
            loc = it.get("section", "?")
            idx = it.get("bullet_index")
            if idx is not None:
                loc += f" bullet {idx}"
            sev = it.get("severity", "minor").upper()
            p.append(f"\n  [{sev}] {loc}: {it.get('problem', '')}")
            if it.get("current_text"):
                p.append(f"    CURRENT: {it['current_text']}")
            if it.get("suggested_rewrite"):
                p.append(f"    REWRITE TO: {it['suggested_rewrite']}")
        for it in sf.get("missing_from_jd", []):
            p.append(f"  MISSING: {it.get('keyword', '')} ({it.get('jd_importance', '')}): {it.get('suggestion', '')}")
        return "\n".join(p)
