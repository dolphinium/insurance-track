from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DocumentBase(BaseModel):
    filename: str
    file_path: str

class Document(DocumentBase):
    id: int
    customer_id: int
    insurance_id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True 