import time
from backend.agents.planner_agent import PlannerAgent
from backend.agents.writer_agent import WriterAgent
from backend.agents.scorer_agent import ScorerAgent
from backend.utils.file_loader import FileLoader


class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.writer = WriterAgent()
        self.scorer = ScorerAgent()
        self.loader = FileLoader()

    def classify(self, jd, job_type, role_type):
        """Step 1: Classify JD and generate strategy (called by Read JD button)."""
        return self.planner.plan(jd, job_type, role_type)

    def generate(self, jd, job_type, role_type, role_name, company_name, strategy):
        """Step 2: Generate resume using approved strategy (called by Generate button)."""
        logs = []
        start = time.time()

        logs.append("Loading static files...")
        gl = self.loader.load_guidelines(job_type)
        rm = self.loader.load_resume_master(job_type)
        logs.append(f"Loaded {job_type} guidelines and resume master.")
        logs.append(f"Strategy: {strategy.get('role_essence', 'N/A')}")
        logs.append(f"AI Intensity: {strategy.get('ai_intensity', 'N/A')}")
        logs.append(f"Primary Skills: {', '.join(strategy.get('primary_skills', []))}")
        suppress = strategy.get('suppress', [])
        if suppress:
            logs.append(f"Suppressed: {', '.join(suppress)}")

        # Iteration 1: Write
        logs.append("Iteration 1: Writer executing strategy...")
        t = time.time()
        d1 = self.writer.write(jd, job_type, role_type, role_name, company_name, gl, rm, strategy)
        logs.append(f"Iteration 1: Draft in {time.time()-t:.1f}s")

        # Iteration 1: Score
        t = time.time()
        s1 = self.scorer.score(d1, jd, job_type, gl, strategy, 1)
        sc1 = s1.get("ats_score", 0)
        scores1 = s1.get("scores", {})
        logs.append(f"Iteration 1: ATS={sc1} | Essence={scores1.get('role_essence', '?')} | Proof={scores1.get('skill_proof', '?')} | Drift={scores1.get('role_drift_risk', '?')} ({len(s1.get('feedback', []))} issues) in {time.time()-t:.1f}s")
        logs.append(f"Pass: {s1.get('pass', '?')}")

        # Iteration 2: Rewrite
        logs.append("Iteration 2: Writer rewriting with feedback...")
        t = time.time()
        d2 = self.writer.rewrite(jd, job_type, role_type, role_name, company_name, gl, rm, strategy, d1, s1)
        logs.append(f"Iteration 2: Rewrite in {time.time()-t:.1f}s")

        # Iteration 2: Score
        t = time.time()
        s2 = self.scorer.score(d2, jd, job_type, gl, strategy, 2)
        sc2 = s2.get("ats_score", 0)
        scores2 = s2.get("scores", {})
        logs.append(f"Iteration 2: ATS={sc2} | Essence={scores2.get('role_essence', '?')} | Proof={scores2.get('skill_proof', '?')} | Drift={scores2.get('role_drift_risk', '?')} ({len(s2.get('feedback', []))} issues) in {time.time()-t:.1f}s")
        logs.append(f"Pass: {s2.get('pass', '?')}")

        # Pick best
        if sc2 >= sc1:
            fr, fs = d2, sc2
            logs.append(f"Using final ({sc1}→{sc2})")
        else:
            fr, fs = d1, sc1
            logs.append(f"Using draft (regression {sc1}→{sc2})")

        logs.append(f"Done in {time.time()-start:.1f}s")

        return {
            "final_resume": fr,
            "final_score": fs,
            "iteration_1": {"resume": d1, "score_result": s1},
            "iteration_2": {"resume": d2, "score_result": s2},
            "logs": logs,
        }
