from .customers import router as customers_router
from .insurances import router as insurances_router
from .documents import router as documents_router

__all__ = ["customers_router", "insurances_router", "documents_router"]
