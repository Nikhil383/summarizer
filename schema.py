from pydantic import BaseModel

class BookSummary(BaseModel):
    title: str
    summary: str
    saved_path: str
