from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services import customer_service
from ..schemas.customer import Customer, CustomerCreate, CustomerWithRelations

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("/", response_model=Customer)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return customer_service.create_customer(db, customer)

@router.get("/", response_model=List[Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return customer_service.get_customers(db, skip=skip, limit=limit)

@router.get("/{customer_id}", response_model=CustomerWithRelations)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = customer_service.get_customer(db, customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.put("/{customer_id}", response_model=Customer)
def update_customer(customer_id: int, customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = customer_service.update_customer(db, customer_id, customer)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    success = customer_service.delete_customer(db, customer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted successfully"} 