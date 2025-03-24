from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.customers import router as customers_router
from .api.insurances import router as insurances_router
from .api.documents import router as documents_router

app = FastAPI(title="Insurance Tracking System")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(customers_router)
app.include_router(insurances_router)
app.include_router(documents_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Insurance Tracking System API"} 