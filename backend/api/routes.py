from fastapi import APIRouter, UploadFile, File
from backend.services.resume_parser import extract_text
from backend.services.ranking import rank_resume

router = APIRouter()

job_description = ""


@router.post("/upload_job")
async def upload_job(desc: str):
    global job_description
    job_description = desc
    return {"message": "Job description stored"}


@router.post("/rank_candidate")
async def rank_candidate(file: UploadFile = File(...)):
    global job_description

    try:
        resume_text = extract_text(await file.read())
        result = rank_resume(resume_text, job_description)
        return result
    except Exception as e:
        return {"error": str(e)}


@router.post("/rank_multiple")
async def rank_multiple(files: list[UploadFile] = File(...)):
    global job_description

    results = []

    try:
        for file in files:
            text = extract_text(await file.read())
            score = rank_resume(text, job_description)
            results.append({"name": file.filename, **score})

        results = sorted(results, key=lambda x: x["final_score"], reverse=True)

        return {"ranked_candidates": results}

    except Exception as e:
        return {"error": str(e)}