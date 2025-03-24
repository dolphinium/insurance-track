from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services import insurance_service
from ..schemas.insurance import Insurance, InsuranceCreate, InsuranceWithRelations

router = APIRouter(prefix="/insurances", tags=["insurances"])

@router.post("/", response_model=Insurance)
def create_insurance(insurance: InsuranceCreate, db: Session = Depends(get_db)):
    return insurance_service.create_insurance(db, insurance)

@router.get("/", response_model=List[Insurance])
def read_insurances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return insurance_service.get_insurances(db, skip=skip, limit=limit)

@router.get("/customer/{customer_id}", response_model=List[Insurance])
def read_customer_insurances(customer_id: int, db: Session = Depends(get_db)):
    return insurance_service.get_customer_insurances(db, customer_id)

@router.get("/upcoming-renewals/", response_model=List[Insurance])
def read_upcoming_renewals(days: int = 14, db: Session = Depends(get_db)):
    return insurance_service.get_upcoming_renewals(db, days)

@router.get("/{insurance_id}", response_model=InsuranceWithRelations)
def read_insurance(insurance_id: int, db: Session = Depends(get_db)):
    db_insurance = insurance_service.get_insurance(db, insurance_id)
    if db_insurance is None:
        raise HTTPException(status_code=404, detail="Insurance not found")
    return db_insurance

@router.put("/{insurance_id}", response_model=Insurance)
def update_insurance(insurance_id: int, insurance: InsuranceCreate, db: Session = Depends(get_db)):
    db_insurance = insurance_service.update_insurance(db, insurance_id, insurance)
    if db_insurance is None:
        raise HTTPException(status_code=404, detail="Insurance not found")
    return db_insurance

@router.delete("/{insurance_id}")
def delete_insurance(insurance_id: int, db: Session = Depends(get_db)):
    success = insurance_service.delete_insurance(db, insurance_id)
    if not success:
        raise HTTPException(status_code=404, detail="Insurance not found")
    return {"message": "Insurance deleted successfully"} 