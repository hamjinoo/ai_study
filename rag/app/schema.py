from pydantic import BaseModel, Field
from typing import List, Optional

class SourceItem(BaseModel):
    id: str
    title: str
    location: str
    quote: str

class AnswerSchema(BaseModel):
    one_line: str
    answer_md: str
    sources: List[SourceItem] = Field(default_factory=list)
    limits: str = ""
    next_questions: List[str] = Field(default_factory=list)
