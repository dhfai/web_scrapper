from pydantic import BaseModel

class ScrapeRequest(BaseModel):
    url: str
    num_pages: int