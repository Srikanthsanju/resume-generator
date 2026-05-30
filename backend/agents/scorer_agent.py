import json
from openai import OpenAI
from backend.config import OPENAI_API_KEY, SCORER_MODEL

class ScorerAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = SCORER_MODEL

    def _mode(self, jt):
        if jt == "contract": return "CONTRACT: 12-15 bullets/recent role normal. Env+Desc expected. Verb max 3."
        if jt == "fulltime": return "FULLTIME: 10-12 bullets/recent role. No env/desc. Ownership language positive. Verb max 2."
        return "GC: 5 companies, 10yr. All 3 clouds expected (fixed per company). Cardinal=Azure, UBS=Azure, MTA=GCP, Cognizant=AWS, Couth=AWS. GenAI only Cardinal. ML only UBS+Cardinal. Env expected. No desc. Verb max 3."

    def _chrono(self, jt):
        if jt == "gc": return "Never penalize MTA/Cognizant/Couth for missing AI. GenAI only in Cardinal Health."
        return "Never penalize BYJU'S/Cognizant for missing GenAI. Basic ML fine for BYJU'S."

    def score(self, draft, jd, job_type, guidelines, iteration=1):
        system = f"""You are a senior technical recruiter and ATS expert.

━━━ TASK 1: GLOBAL ATS SCORE (0-100) ━━━

95-100: Perfect. Zero violations, natural tone, every JD requirement.
90-94: Excellent. 1-2 minor gaps, submission-ready.
85-89: Strong but has fixable issues.
80-84: Good foundation, multiple improvements needed.
70-79: Decent but noticeable gaps.
Below 70: Significant problems.

SCORING DISCIPLINE:
- Do NOT default to 85. Differentiate: 82, 86, 91, 94.
- If 5+ fixable issues → score BELOW 87.
- If genuinely strong with 1-2 minor issues → score 90+.
- Calibrate: 8 issues = 80-84, not 85-89.
- ITERATION 2: If fixes from iteration 1 were applied, score MUST increase. If ignored, call out which fixes were skipped.

{self._mode(job_type)}

━━━ TASK 2: POINTED FEEDBACK ━━━

CHECK IN THIS ORDER:

A. BULLET COMPLETENESS (CHECK FIRST — MOST IMPORTANT)
   Count words in EVERY bullet. Any bullet under 15 words = CRITICAL violation (issue_type: "short_bullet").
   Bullets should be 18-25 words minimum. Short fragments are UNACCEPTABLE for a senior engineer resume.
   60%+ of bullets must end with PURPOSE CLAUSE (enabling, supporting, improving, reducing, delivering, ensuring).
   BAD: "Built ingestion pipelines using Kinesis and Airflow for batch processing" (12 words, abrupt)
   GOOD: "Built batch and real-time data ingestion pipelines using Kinesis and Apache Airflow enabling efficient processing of high-volume streaming and historical telecom data" (24 words, complete)
   For EVERY short bullet, provide an EXPANDED rewrite of 18-25 words.

B. GUIDELINE VIOLATIONS
   >3 "and" per bullet, semicolons, comma before "and", arrows/symbols, slashes
   Weak verbs ("Responsible for", "Worked on"), abbreviation errors
   Verb repetition beyond limit for this job type
   Parentheses >3 across BULLET POINTS (skills section EXEMPT)
   Chronology violations (GenAI in pre-2022 roles)

C. JD ALIGNMENT GAPS
   Required JD skills completely missing from resume
   JD keywords missing from first 3-4 bullets of most recent role
   Skills categories not ordered to match JD priority

D. QUALITY ISSUES
   Repeated concepts across roles (amnesia)
   CLOUD MIXING: multiple clouds in same company = CRITICAL
   Cloud split into multiple skills categories instead of one
   Generic/AI-generated sounding text

CHRONOLOGY: {self._chrono(job_type)}
Parentheses limit = BULLET POINTS only. Skills section exempt.

RESUME GLANCE TEST:
After detailed analysis, step back. Does this look polished and recruiter-ready? If bullets are inconsistently short, if the resume looks sparse or if the writing quality varies between sections — flag "presentation" as major.

GUIDELINES:
{guidelines}

━━━ OUTPUT — ONLY THIS JSON ━━━

{{"ats_score":<0-100>,"score_reasoning":"2-3 sentences. Mention bullet length if short bullets exist.","feedback":[{{"section":"summary|skills|exp1|exp2|exp3|exp4|exp5","bullet_index":<0-based or null>,"issue_type":"short_bullet|grammar|weak_verb|chronology|repetition|or_condition|missing_keyword|vague_bullet|verb_repetition|parentheses|cloud_mixing|presentation|other","severity":"critical|major|minor","problem":"What is wrong","current_text":"Exact text","suggested_rewrite":"Concrete 18-25 word rewrite"}}],"missing_from_jd":[{{"keyword":"...","jd_importance":"required|preferred|nice_to_have","suggestion":"Where and how to add it"}}],"top_3_fixes":["Fix 1","Fix 2","Fix 3"]}}
"""
        user = f"JOB DESCRIPTION:\n{jd}\n\nJOB TYPE: {job_type}\nITERATION: {iteration} of 2\n\nRESUME DRAFT JSON:\n{json.dumps(draft, indent=2)}"
        try:
            r = self.client.chat.completions.create(
                model=self.model, temperature=0.1, max_tokens=4000,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            )
            res = json.loads(r.choices[0].message.content.strip())
            if "ats_score" in res:
                res["ats_score"] = max(0, min(100, int(res["ats_score"])))
            res["iteration"] = iteration
            res["job_type"] = job_type
            return res
        except Exception as e:
            print(f"Scorer Error: {e}")
            return {"ats_score": 0, "score_reasoning": str(e), "feedback": [], "missing_from_jd": [], "top_3_fixes": [str(e)], "error": str(e)}
