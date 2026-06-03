import json, traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from backend.agents.orchestrator import Orchestrator
from backend.utils.docx_generator import DocxGenerator
from backend.utils.file_loader import FileLoader
from backend.utils.filename_generator import generate_filename
from backend.utils.jd_parser import extract_jd_details
from backend.config import OUTPUTS_DIR

app = FastAPI(title="AI Resume Generator", version="4.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

orchestrator = Orchestrator()
docx_gen = DocxGenerator()
file_loader = FileLoader()


class ReadJdRequest(BaseModel):
    jd: str
    job_type: str
    role_type: str


class GenerateRequest(BaseModel):
    jd: str
    job_type: str
    role_type: str
    role_name: str
    company_name: str
    strategy: dict  # The approved strategy from Read JD


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/read-jd")
def read_jd(req: ReadJdRequest):
    """Step 1: Classify JD and return editable strategy card."""
    try:
        strategy = orchestrator.classify(req.jd, req.job_type, req.role_type)
        recruiter = extract_jd_details(req.jd)
        return {"strategy": strategy, "recruiter": recruiter}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(500, f"Planner error: {e}")


@app.post("/api/generate")
def generate_resume(req: GenerateRequest):
    """Step 2: Generate resume using approved strategy."""
    try:
        if req.job_type not in ("contract", "fulltime", "gc"):
            raise ValueError(f"Invalid job_type: {req.job_type}")

        result = orchestrator.generate(
            jd=req.jd, job_type=req.job_type, role_type=req.role_type,
            role_name=req.role_name, company_name=req.company_name,
            strategy=req.strategy,
        )

        tp = file_loader.get_template_path(req.job_type)
        fn = generate_filename(req.company_name, req.job_type, req.role_type)
        docx_gen.generate(result["final_resume"], tp, fn, req.job_type)
        result["logs"].append(f"Generated: {fn}")

        # Save logs
        lp = OUTPUTS_DIR / fn.replace(".docx", "_log.json")
        lp.write_text(json.dumps({
            "request": req.model_dump(), "strategy": req.strategy,
            "iteration_1": result["iteration_1"], "iteration_2": result["iteration_2"],
            "final_score": result["final_score"], "logs": result["logs"],
        }, indent=2), encoding="utf-8")

        s1 = result["iteration_1"]["score_result"]
        s2 = result["iteration_2"]["score_result"]

        return {
            "ats_score": result["final_score"],
            "scores": s2.get("scores", {}),
            "score_reasoning": s2.get("score_reasoning", ""),
            "pass": s2.get("pass", False),
            "skill_proof_matrix": s2.get("skill_proof_matrix", []),
            "filename": fn,
            "download_url": f"/api/download/{fn}",
            "iteration_1_score": s1.get("ats_score", 0),
            "iteration_1_scores": s1.get("scores", {}),
            "iteration_1_reasoning": s1.get("score_reasoning", ""),
            "iteration_1_top_fixes": s1.get("top_fixes", s1.get("top_3_fixes", [])),
            "iteration_1_feedback_count": len(s1.get("feedback", [])),
            "iteration_2_score": s2.get("ats_score", 0),
            "iteration_2_scores": s2.get("scores", {}),
            "iteration_2_reasoning": s2.get("score_reasoning", ""),
            "iteration_2_feedback_count": len(s2.get("feedback", [])),
            "logs": result["logs"],
        }
    except FileNotFoundError as e:
        raise HTTPException(404, str(e))
    except ValueError as e:
        raise HTTPException(422, str(e))
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(500, f"Pipeline error: {e}")


@app.get("/api/download/{filename}")
def download(filename: str):
    fp = OUTPUTS_DIR / filename
    if not fp.exists():
        raise HTTPException(404, "File not found")
    return FileResponse(
        path=str(fp), filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": f'attachment; filename="{filename}"', "X-Content-Type-Options": "nosniff"},
    )


if __name__ == "__main__":
    import uvicorn
    from backend.config import HOST, PORT
    uvicorn.run("backend.main:app", host=HOST, port=PORT, reload=True)
