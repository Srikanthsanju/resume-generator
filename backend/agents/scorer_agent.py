import json
from openai import OpenAI
from backend.config import OPENAI_API_KEY, SCORER_MODEL


class ScorerAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = SCORER_MODEL

    def score(self, draft, jd, job_type, guidelines, strategy, iteration=1):
        system = f"""You are a resume evaluator. You have the approved strategy and must check whether the writer executed it correctly.

APPROVED STRATEGY:
{json.dumps(strategy, indent=2)}

GUIDELINES:
{guidelines}

═══ SCORING ═══

Give 5 SEPARATE scores (0-100 each):

1. ATS_KEYWORD_COVERAGE: What % of primary_skills from the strategy appear in resume bullets with proof? Not just in skills section — in actual experience bullets.

2. ROLE_ESSENCE: Does this resume SELL the role_essence? If strategy says "Build GCP data pipelines" but resume reads like "Document data governance," this score is LOW. Read the resume at a glance — what job does it look like?

3. BELIEVABILITY: Are bullets specific, interview-safe, 20-30 words, not overstuffed with 5+ tools? Would a hiring manager believe this person did this work?

4. SKILL_PROOF: For each primary_skill, is there at least one bullet that proves hands-on experience? List which skills have proof and which don't.

5. ROLE_DRIFT_RISK: Is the resume drifting into a different role? If the suppress list says "no RAG, no LLM" but the resume mentions them, drift is HIGH. Score 0=no drift, 100=completely wrong role.

HARD FAIL CONDITIONS:
If ATS_KEYWORD_COVERAGE < 85 → must improve
If ROLE_ESSENCE < 85 → must rewrite core bullets
If SKILL_PROOF < 80 → must add proof bullets
If BELIEVABILITY < 75 → must fix overstuffed bullets
If ROLE_DRIFT_RISK > 25 → must remove drifting content

BULLET CHECKS:
- Any bullet under 15 words = CRITICAL (short_bullet)
- Suppressed terms appearing = CRITICAL (role_drift)
- Primary skill with zero proof bullets = MAJOR (missing_proof)

ITERATION {iteration}: {"First evaluation. Be thorough — find every issue so the rewrite can fix them all at once." if iteration == 1 else "Second evaluation. Check if fixes from iteration 1 were applied. Score MUST increase if fixes were applied."}

OUTPUT — ONLY this JSON:
{{
  "ats_score": <0-100 overall>,
  "scores": {{
    "ats_keyword_coverage": <0-100>,
    "role_essence": <0-100>,
    "believability": <0-100>,
    "skill_proof": <0-100>,
    "role_drift_risk": <0-100>
  }},
  "score_reasoning": "2-3 sentences explaining the scores",
  "pass": true/false based on hard fail conditions,
  "skill_proof_matrix": [
    {{"skill": "Python", "proven": true, "where": "exp1 bullet 2"}},
    {{"skill": "BigQuery", "proven": false, "where": "not found"}}
  ],
  "feedback": [
    {{
      "section": "summary|skills|exp1|exp2|exp3|exp4|exp5",
      "bullet_index": <0-based or null>,
      "issue_type": "short_bullet|role_drift|missing_proof|grammar|weak_verb|overstuffed|vague|repetition|other",
      "severity": "critical|major|minor",
      "problem": "What is wrong",
      "current_text": "Exact text",
      "suggested_rewrite": "Concrete 20-30 word rewrite"
    }}
  ],
  "missing_from_jd": [
    {{"keyword": "...", "jd_importance": "required|preferred", "suggestion": "Where to add it"}}
  ],
  "top_fixes": ["Most impactful fix", "Second fix", "Third fix"]
}}"""

        user = f"JD:\n{jd}\n\nJOB TYPE: {job_type}\nITERATION: {iteration}/2\n\nRESUME JSON:\n{json.dumps(draft, indent=2)}"
        try:
            r = self.client.chat.completions.create(
                model=self.model, temperature=0.1, max_tokens=4000,
                response_format={"type": "json_object"},
                messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
            )
            res = json.loads(r.choices[0].message.content.strip())
            if "ats_score" in res:
                res["ats_score"] = max(0, min(100, int(res["ats_score"])))
            res["iteration"] = iteration
            res["job_type"] = job_type
            return res
        except Exception as e:
            print(f"Scorer Error: {e}")
            return {"ats_score": 0, "scores": {}, "score_reasoning": str(e), "pass": False, "skill_proof_matrix": [], "feedback": [], "missing_from_jd": [], "top_fixes": [str(e)], "error": str(e)}
