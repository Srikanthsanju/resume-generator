import json
import time
from backend.agents.writer_agent import WriterAgent
from backend.agents.scorer_agent import ScorerAgent
from backend.utils.file_loader import FileLoader


class Orchestrator:
    """Runs Writer → Scorer → Writer → Scorer (2 fixed iterations)."""

    def __init__(self):
        self.writer = WriterAgent()
        self.scorer = ScorerAgent()
        self.file_loader = FileLoader()

    def run(self, jd, job_type, role_type, role_name, company_name):
        logs = []
        start = time.time()

        logs.append("Loading static files...")
        guidelines = self.file_loader.load_guidelines(job_type)
        resume_master = self.file_loader.load_resume_master(job_type)
        logs.append(f"Loaded {job_type} guidelines and resume master.")

        # ── Iteration 1 ──
        logs.append("Iteration 1: Writer generating draft...")
        t1 = time.time()
        draft_1 = self.writer.write(jd, job_type, role_type, role_name, company_name, guidelines, resume_master)
        logs.append(f"Iteration 1: Draft generated in {time.time()-t1:.1f}s")

        logs.append("Iteration 1: Scorer evaluating...")
        t2 = time.time()
        score_1 = self.scorer.score(draft_1, jd, job_type, guidelines, iteration=1)
        s1 = score_1.get("ats_score", 0)
        fc1 = len(score_1.get("feedback", []))
        logs.append(f"Iteration 1: Score = {s1}/100 ({fc1} issues) in {time.time()-t2:.1f}s")

        # ── Iteration 2 ──
        logs.append("Iteration 2: Writer rewriting with feedback...")
        t3 = time.time()
        draft_2 = self.writer.rewrite(jd, job_type, role_type, role_name, company_name, guidelines, resume_master, draft_1, score_1)
        logs.append(f"Iteration 2: Rewrite generated in {time.time()-t3:.1f}s")

        logs.append("Iteration 2: Scorer evaluating final...")
        t4 = time.time()
        score_2 = self.scorer.score(draft_2, jd, job_type, guidelines, iteration=2)
        s2 = score_2.get("ats_score", 0)
        fc2 = len(score_2.get("feedback", []))
        logs.append(f"Iteration 2: Score = {s2}/100 ({fc2} issues) in {time.time()-t4:.1f}s")

        # ── Pick best ──
        if s2 >= s1:
            final_resume, final_score = draft_2, s2
            logs.append(f"Using final draft ({s1} → {s2})")
        else:
            final_resume, final_score = draft_1, s1
            logs.append(f"Using draft (regression: {s1} → {s2})")

        logs.append(f"Pipeline complete in {time.time()-start:.1f}s")

        return {
            "final_resume": final_resume,
            "final_score": final_score,
            "iteration_1": {"resume": draft_1, "score_result": score_1},
            "iteration_2": {"resume": draft_2, "score_result": score_2},
            "logs": logs,
        }
