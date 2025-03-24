from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from .insurance import Insurance
from .document import Document

class CustomerBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    notes: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class CustomerWithRelations(Customer):
    insurances: List[Insurance] = []
    documents: List[Document] = []

    class Config:
        from_attributes = True 