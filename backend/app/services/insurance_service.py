from sqlalchemy.orm import Session
from ..models.insurance import Insurance
from ..schemas.insurance import InsuranceCreate
from typing import List, Optional
from datetime import date

def get_insurance(db: Session, insurance_id: int) -> Optional[Insurance]:
    return db.query(Insurance).filter(Insurance.id == insurance_id).first()

def get_insurances(db: Session, skip: int = 0, limit: int = 100) -> List[Insurance]:
    return db.query(Insurance).offset(skip).limit(limit).all()

def get_customer_insurances(db: Session, customer_id: int) -> List[Insurance]:
    return db.query(Insurance).filter(Insurance.customer_id == customer_id).all()

def get_upcoming_renewals(db: Session, days: int = 14) -> List[Insurance]:
    today = date.today()
    end_date = today.replace(day=today.day + days)
    return db.query(Insurance).filter(
        Insurance.renewal_date.between(today, end_date)
    ).all()

def create_insurance(db: Session, insurance: InsuranceCreate) -> Insurance:
    db_insurance = Insurance(**insurance.model_dump())
    db.add(db_insurance)
    db.commit()
    db.refresh(db_insurance)
    return db_insurance

def update_insurance(db: Session, insurance_id: int, insurance: InsuranceCreate) -> Optional[Insurance]:
    db_insurance = get_insurance(db, insurance_id)
    if db_insurance:
        for key, value in insurance.model_dump().items():
            setattr(db_insurance, key, value)
        db.commit()
        db.refresh(db_insurance)
    return db_insurance

def delete_insurance(db: Session, insurance_id: int) -> bool:
    db_insurance = get_insurance(db, insurance_id)
    if db_insurance:
        db.delete(db_insurance)
        db.commit()
        return True
    return False 