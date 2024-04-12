from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Record

app_router = APIRouter()


@app_router.post("/record/")
def create_record(record: dict, db: Session = Depends(get_db)):
    db_record = Record(**record)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


@app_router.get("/record/{record_id}/")
def get_retrieve_record(record_id: int, db: Session = Depends(get_db)):
    record = db.query(Record).filter(Record.id == record_id).first()
    if record is None:
        raise HTTPException(
            status_code=404,
            detail="record not found"
        )
    return record
