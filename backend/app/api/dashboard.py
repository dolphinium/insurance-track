from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.dashboard_service import DashboardService
from ..schemas import DashboardStats

router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard"]
)

@router.get("/stats", response_model=DashboardStats)
def get_dashboard_stats(db: Session = Depends(get_db)):
    """
    Get dashboard statistics including:
    - Total number of customers
    - Number of active insurance policies
    - Number of upcoming renewals (next 30 days)
    """
    dashboard_service = DashboardService(db)
    return dashboard_service.get_dashboard_stats() 