from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List
from decimal import Decimal
from .document import Document

class InsuranceBase(BaseModel):
    type: str
    renewal_date: date
    coverage_details: Optional[str] = None
    premium_amount: Optional[Decimal] = None
    notes: Optional[str] = None

class InsuranceCreate(InsuranceBase):
    customer_id: int

class Insurance(InsuranceBase):
    id: int
    customer_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class InsuranceWithRelations(Insurance):
    documents: List[Document] = []

    class Config:
        from_attributes = True 