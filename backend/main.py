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

app = FastAPI(title="AI Resume Generator", version="3.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

orchestrator = Orchestrator()
docx_gen = DocxGenerator()
file_loader = FileLoader()


class GenerateRequest(BaseModel):
    jd: str
    job_type: str       # contract | fulltime | gc
    role_type: str
    role_name: str
    company_name: str


class GenerateResponse(BaseModel):
    ats_score: int
    score_reasoning: str
    filename: str
    download_url: str
    iteration_1_score: int
    iteration_1_reasoning: str
    iteration_1_top_fixes: list[str]
    iteration_1_feedback_count: int
    iteration_2_score: int
    iteration_2_reasoning: str
    iteration_2_feedback_count: int
    logs: list[str]
    recruiter_email: str
    recruiter_name: str
    job_title: str
    work_location: str


class ParseJdRequest(BaseModel):
    jd: str


class ParseJdResponse(BaseModel):
    recruiter_email: str
    recruiter_name: str
    job_title: str
    work_location: str


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/parse-jd", response_model=ParseJdResponse)
def parse_jd(req: ParseJdRequest):
    """Extract recruiter details from JD text without generating a resume."""
    return extract_jd_details(req.jd)


@app.post("/api/generate", response_model=GenerateResponse)
def generate_resume(req: GenerateRequest):
    try:
        if req.job_type not in ("contract", "fulltime", "gc"):
            raise ValueError(f"Invalid job_type: {req.job_type}")

        result = orchestrator.run(
            jd=req.jd, job_type=req.job_type,
            role_type=req.role_type, role_name=req.role_name,
            company_name=req.company_name,
        )

        template_path = file_loader.get_template_path(req.job_type)
        filename = generate_filename(req.company_name, req.job_type, req.role_type)

        docx_gen.generate(
            resume_data=result["final_resume"],
            template_path=template_path,
            output_filename=filename,
            job_type=req.job_type,
        )

        result["logs"].append(f"Generated: {filename}")

        # Save iteration logs
        log_path = OUTPUTS_DIR / filename.replace(".docx", "_log.json")
        log_path.write_text(json.dumps({
            "request": req.model_dump(),
            "iteration_1": result["iteration_1"],
            "iteration_2": result["iteration_2"],
            "final_score": result["final_score"],
            "logs": result["logs"],
        }, indent=2), encoding="utf-8")

        s1 = result["iteration_1"]["score_result"]
        s2 = result["iteration_2"]["score_result"]

        # Extract recruiter details from JD
        jd_details = extract_jd_details(req.jd)

        return GenerateResponse(
            ats_score=result["final_score"],
            score_reasoning=s2.get("score_reasoning", ""),
            filename=filename,
            download_url=f"/api/download/{filename}",
            iteration_1_score=s1.get("ats_score", 0),
            iteration_1_reasoning=s1.get("score_reasoning", ""),
            iteration_1_top_fixes=s1.get("top_3_fixes", []),
            iteration_1_feedback_count=len(s1.get("feedback", [])),
            iteration_2_score=s2.get("ats_score", 0),
            iteration_2_reasoning=s2.get("score_reasoning", ""),
            iteration_2_feedback_count=len(s2.get("feedback", [])),
            logs=result["logs"],
            recruiter_email=jd_details["recruiter_email"],
            recruiter_name=jd_details["recruiter_name"],
            job_title=jd_details["job_title"],
            work_location=jd_details["work_location"],
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Pipeline error: {str(e)}")


@app.get("/api/download/{filename}")
def download_resume(filename: str):
    filepath = OUTPUTS_DIR / filename
    if not filepath.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(
        path=str(filepath),
        filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"',
            "X-Content-Type-Options": "nosniff",
            "Cache-Control": "no-cache",
        },
    )


if __name__ == "__main__":
    import uvicorn
    from backend.config import HOST, PORT
    uvicorn.run("backend.main:app", host=HOST, port=PORT, reload=True)
