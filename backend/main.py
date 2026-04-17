from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="AI Resume Screening API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API is running"}