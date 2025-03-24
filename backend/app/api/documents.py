from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import get_db
from ..services import document_service
from ..schemas.document import Document

router = APIRouter(prefix="/documents", tags=["documents"])

@router.post("/upload/{customer_id}")
async def upload_document(
    customer_id: int,
    file: UploadFile = File(...),
    insurance_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    file_path = await document_service.save_upload_file(file, customer_id, insurance_id)
    document = document_service.create_document(
        db,
        customer_id=customer_id,
        filename=file.filename,
        file_path=file_path,
        insurance_id=insurance_id
    )
    return {"message": "Document uploaded successfully", "document_id": document.id}

@router.get("/customer/{customer_id}", response_model=List[Document])
def read_customer_documents(customer_id: int, db: Session = Depends(get_db)):
    return document_service.get_customer_documents(db, customer_id)

@router.get("/insurance/{insurance_id}", response_model=List[Document])
def read_insurance_documents(insurance_id: int, db: Session = Depends(get_db)):
    return document_service.get_insurance_documents(db, insurance_id)

@router.get("/{document_id}", response_model=Document)
def read_document(document_id: int, db: Session = Depends(get_db)):
    document = document_service.get_document(db, document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@router.delete("/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):
    success = document_service.delete_document(db, document_id)
    if not success:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"message": "Document deleted successfully"} 