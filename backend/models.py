from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional

class Note(BaseModel):
    title:str
    content:str
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

