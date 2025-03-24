from sqlalchemy.orm import Session
from ..models.document import Document
from typing import List, Optional
import os
import aiofiles
from fastapi import UploadFile
import shutil

UPLOAD_DIR = "storage"

async def save_upload_file(upload_file: UploadFile, customer_id: int, insurance_id: Optional[int] = None) -> str:
    # Create customer directory if it doesn't exist
    customer_dir = os.path.join(UPLOAD_DIR, f"customer_{customer_id}")
    os.makedirs(customer_dir, exist_ok=True)

    # If insurance_id is provided, create insurance directory
    if insurance_id:
        customer_dir = os.path.join(customer_dir, f"insurance_{insurance_id}")
        os.makedirs(customer_dir, exist_ok=True)

    file_path = os.path.join(customer_dir, upload_file.filename)
    
    # Save the file
    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await upload_file.read()
        await out_file.write(content)
    
    return file_path

def create_document(
    db: Session,
    customer_id: int,
    filename: str,
    file_path: str,
    insurance_id: Optional[int] = None
) -> Document:
    db_document = Document(
        customer_id=customer_id,
        insurance_id=insurance_id,
        filename=filename,
        file_path=file_path
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def get_document(db: Session, document_id: int) -> Optional[Document]:
    return db.query(Document).filter(Document.id == document_id).first()

def get_customer_documents(db: Session, customer_id: int) -> List[Document]:
    return db.query(Document).filter(Document.customer_id == customer_id).all()

def get_insurance_documents(db: Session, insurance_id: int) -> List[Document]:
    return db.query(Document).filter(Document.insurance_id == insurance_id).all()

def delete_document(db: Session, document_id: int) -> bool:
    db_document = get_document(db, document_id)
    if db_document:
        # Delete the file
        try:
            os.remove(db_document.file_path)
        except OSError:
            pass  # File might not exist
        
        # Delete from database
        db.delete(db_document)
        db.commit()
        return True
    return False 