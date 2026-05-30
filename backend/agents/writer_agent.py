import json
from anthropic import Anthropic
from backend.config import ANTHROPIC_API_KEY, WRITER_MODEL

class WriterAgent:
    def __init__(self):
        self.client = Anthropic(api_key=ANTHROPIC_API_KEY)
        self.model = WRITER_MODEL

    def _system(self, guidelines, resume_master, job_type):
        cloud_rule = ("GC MODE: Clouds FIXED. Cardinal Health=Azure, UBS=Azure/Snowflake, MTA=GCP, Cognizant=AWS, Couth=AWS. NEVER change these. If JD emphasizes one cloud, give that company more bullets." if job_type == "gc"
            else "Each company=ONE cloud. Defaults: Bee Data=AWS, Allied Health=AWS, BYJUS=GCP, Cognizant=none. If JD lists clouds as OR condition (AWS/Azure/GCP), KEEP AWS as default. Only switch when JD CLEARLY emphasizes another cloud (appears 5+ times or listed as required). Count cloud mentions in JD to decide. NEVER put two clouds in the same company.")
        verb_rule = "max 2" if job_type == "fulltime" else "max 3"
        return f"""You are an expert technical resume writer.

GUIDELINES:
{guidelines}

CANDIDATE SOURCE (ONLY source — never invent):
{resume_master}

═══ CRITICAL RULES ═══

RULE 1 — BULLET COMPLETENESS (MOST IMPORTANT):
Every bullet MUST be 18-25+ words. NEVER write bullets under 15 words.
A bullet is: Action + What You Built + Technical Details + Purpose/Impact Clause.

BAD (too short — scorer WILL flag this as critical violation):
  "Built ingestion pipelines using Kinesis and Airflow for batch processing"

GOOD (complete — this is what every bullet should look like):
  "Built batch and real-time data ingestion pipelines using Kinesis and Apache Airflow enabling efficient processing of high-volume streaming and historical telecom data"

60%+ of bullets MUST end with a PURPOSE CLAUSE using: enabling, supporting, improving, reducing, delivering, ensuring, achieving, providing.
Read each bullet aloud — if it stops mid-thought, it is INCOMPLETE. A 6-word bullet looks junior. A 20-word bullet looks senior.

RULE 2 — CLOUD: {cloud_rule}
RULE 3 — Skills cloud = ONE category: "Cloud Platforms: AWS (...), GCP (...)"
RULE 4 — Each role = one platform story. Never mix clouds in same company.
RULE 5 — JSON only. No markdown fences. No bullet symbols. Parentheses limit (3) = bullet points only. Verbs: {verb_rule} repeats."""

    def _structure(self, job_type):
        if job_type == "contract":
            return """Return JSON with keys: summary (6-10 bullets, each 18+ words), technical_skills (category lines), exp1_description, exp1 (12-15 bullets, 18+ words each), exp1_env, exp2_description, exp2 (10-14 bullets), exp2_env, exp3_description, exp3 (7-10 bullets), exp3_env, exp4_description, exp4 (7-10 bullets), exp4_env"""
        elif job_type == "fulltime":
            return """Return JSON with keys: summary (5-8 bullets, each 18+ words), technical_skills, exp1 (10-12 bullets, 18+ words each), exp2 (8-10 bullets), exp3 (6-9 bullets), exp4 (5-7 bullets). NO description/env/exp5."""
        return """Return JSON with keys: summary (10-15 bullets, each 18+ words), technical_skills, exp1 (12-14 bullets, 18+ words each), exp1_env, exp2 (12-14 bullets), exp2_env, exp3 (10-14 bullets), exp3_env, exp4 (10-14 bullets), exp4_env, exp5 (10-14 bullets), exp5_env. NO description fields. 5 companies."""

    def write(self, jd, job_type, role_type, role_name, company_name, guidelines, resume_master):
        prompt = f"""Write a tailored resume for this job:

JOB DESCRIPTION:
{jd}

JOB TYPE: {job_type} | ROLE TYPE: {role_type} | ROLE NAME: {role_name} | COMPANY: {company_name}

{self._structure(job_type)}

CRITICAL: Every bullet = 18-25+ words with purpose clause. Short fragments like "Optimized SQL queries for performance" are NOT acceptable. Complete each thought with what it enabled or achieved.

Return ONLY JSON. No other text."""
        return self._call(prompt, guidelines, resume_master, job_type)

    def rewrite(self, jd, job_type, role_type, role_name, company_name, guidelines, resume_master, draft, feedback):
        fb = self._fmt(feedback)
        exp_count = 5 if job_type == "gc" else 4
        has_desc = job_type == "contract"
        has_env = job_type in ("contract", "gc")
        keys = ["summary", "technical_skills"]
        for i in range(1, exp_count + 1):
            if has_desc: keys.append(f"exp{i}_description")
            keys.append(f"exp{i}")
            if has_env: keys.append(f"exp{i}_env")

        prompt = f"""Score was {feedback.get('ats_score', 'N/A')}/100. Fix these issues:

JOB DESCRIPTION:
{jd}

JOB TYPE: {job_type} | ROLE TYPE: {role_type} | ROLE NAME: {role_name} | COMPANY: {company_name}

PREVIOUS DRAFT:
{json.dumps(draft, indent=2)}

SCORER FEEDBACK — Fix these:
{fb}

CRITICAL: If scorer flagged short bullets, EXPAND them to 18-25+ words with purpose clauses. Do NOT return any bullet under 15 words.
Keep bullets the scorer did NOT flag.
Include ALL keys: {', '.join(keys)}
Return ONLY improved JSON."""
        return self._call(prompt, guidelines, resume_master, job_type, temp=0.2)

    def _call(self, prompt, guidelines, resume_master, job_type, temp=0.3):
        try:
            r = self.client.messages.create(
                model=self.model, max_tokens=8000, temperature=temp,
                system=self._system(guidelines, resume_master, job_type),
                messages=[{"role": "user", "content": prompt}],
            )
            c = r.content[0].text.strip()
            if c.startswith("```"):
                c = c.split("\n", 1)[1]
            if c.endswith("```"):
                c = c[:c.rfind("```")]
            return json.loads(c.strip())
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
