from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from ..models import Customer, Insurance
from ..schemas import DashboardStats

class DashboardService:
    def __init__(self, db: Session):
        self.db = db

    def get_dashboard_stats(self) -> DashboardStats:
        # Get total customers
        total_customers = self.db.query(Customer).count()

        # Get active policies
        active_policies = self.db.query(Insurance).count()

        # Get upcoming renewals (next 30 days)
        today = datetime.now().date()
        thirty_days = today + timedelta(days=30)
        upcoming_renewals = (
            self.db.query(Insurance)
            .filter(Insurance.renewal_date.between(today, thirty_days))
            .count()
        )

        return DashboardStats(
            total_customers=total_customers,
            active_policies=active_policies,
            upcoming_renewals=upcoming_renewals
        ) 