import json
from openai import OpenAI
from backend.config import OPENAI_API_KEY, PLANNER_MODEL


class PlannerAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = PLANNER_MODEL

    def plan(self, jd: str, job_type: str, role_type: str) -> dict:
        system = """You are a resume strategy planner. Your job is to analyze a Job Description and create a precise strategy that a resume writer will follow. You do NOT write the resume. You only plan what the resume should contain.

CRITICAL RULE: The job title and top technical requirements control the resume theme. Do not let secondary responsibilities (documentation, stakeholder reviews, Agile ceremonies, governance) override the job title.

OUTPUT FORMAT — Return ONLY this JSON:
{
  "primary_role": "The actual role being hired for",
  "role_essence": "One sentence: what does the hiring manager want this person to DO daily?",
  "ai_intensity": "Level 0-4: 0=No AI, 1=Light ML, 2=ML focused, 3=GenAI/RAG, 4=Agentic AI",
  "primary_skills": ["Top 8-12 skills that MUST appear in resume bullets with proof"],
  "secondary_skills": ["3-5 skills that get 1-2 bullets max"],
  "suppress": ["Skills/terms to NOT mention unless JD explicitly requires them"],
  "bullet_distribution": {
    "primary_engineering": "percentage — hands-on building, coding, pipelines, APIs",
    "secondary_support": "percentage — governance, quality, monitoring",
    "cicd_deployment": "percentage — CI/CD, testing, deployment",
    "communication": "percentage — stakeholder, agile, documentation"
  },
  "company_strategy": {
    "company_1": "What to emphasize for the most recent role",
    "company_2": "What to emphasize for the second role",
    "company_3": "What to emphasize for the third role",
    "company_4": "What to emphasize for the fourth role"
  },
  "cloud_decision": "Which cloud to use as primary and why",
  "resume_strategy": "2-3 sentence strategy: what should the resume SELL?",
  "forbidden_drift": ["Specific themes that would make this resume sound like the WRONG role"]
}"""

        user = f"""Analyze this JD and create a resume strategy:

JOB DESCRIPTION:
{jd}

JOB TYPE: {job_type}
ROLE TYPE SELECTED BY USER: {role_type}

IMPORTANT:
- The role_essence should describe what this person DOES, not what they document or analyze.
- primary_skills must come from the JD's required/mandatory section.
- suppress should include AI/ML terms if this is NOT an AI role.
- bullet_distribution percentages must add to 100.
- company_strategy should describe the ENGINEERING work, not documentation work.
- forbidden_drift should list themes that would make the resume sound like a different role (e.g., "Data Governance Analyst" when hiring for "Data Engineer").

Return ONLY JSON."""

        try:
            r = self.client.chat.completions.create(
                model=self.model,
                temperature=0.2,
                max_completion_tokens=2000,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            )
            return json.loads(r.choices[0].message.content.strip())
        except Exception as e:
            print(f"Planner Error: {e}")
            return {
                "primary_role": role_type,
                "role_essence": "Could not classify JD",
                "ai_intensity": "Level 1",
                "primary_skills": [],
                "secondary_skills": [],
                "suppress": [],
                "bullet_distribution": {"primary_engineering": "70", "secondary_support": "15", "cicd_deployment": "10", "communication": "5"},
                "company_strategy": {},
                "cloud_decision": "AWS default",
                "resume_strategy": "Could not generate strategy",
                "forbidden_drift": [],
                "error": str(e),
            }
