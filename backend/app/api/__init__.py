from fastapi import APIRouter
from .customers import router as customers_router
from .insurances import router as insurances_router
from .documents import router as documents_router
from .dashboard import router as dashboard_router

__all__ = [
    "customers_router",
    "insurances_router",
    "documents_router",
    "dashboard_router",
    "router"
]

router = APIRouter()
router.include_router(customers_router)
router.include_router(insurances_router)
router.include_router(documents_router)
router.include_router(dashboard_router)
