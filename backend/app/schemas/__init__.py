from .customer import Customer, CustomerCreate, CustomerWithRelations
from .insurance import Insurance, InsuranceCreate, InsuranceWithRelations
from .document import Document
from pydantic import BaseModel

__all__ = [
    "Customer",
    "CustomerCreate",
    "CustomerWithRelations",
    "Insurance",
    "InsuranceCreate",
    "InsuranceWithRelations",
    "Document"
]

class DashboardStats(BaseModel):
    total_customers: int
    active_policies: int
    upcoming_renewals: int
    message: str | None = None
