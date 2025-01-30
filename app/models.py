from pydantic import BaseModel
from typing import List

class ScrapeRequest(BaseModel):
    url: str
    num_pages: int
    task: str  # ✅ Dinamis: Bisa diubah user
    parameters: List[str]  # ✅ Dinamis: Bisa diubah user
