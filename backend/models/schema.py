from pydantic import BaseModel
from typing import List


class ResumeResult(BaseModel):
    final_score: float
    semantic_score: float
    skill_score: float
    decision: str
    matched_skills: List[str]
    missing_skills: List[str]