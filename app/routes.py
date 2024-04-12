from fastapi import (
    APIRouter,
    Depends,
    HTTPException, Query
)
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Record

app_router = APIRouter()


@app_router.post("/record/")
def create_record(
        record: dict,
        db: Session = Depends(get_db)
):
    db_record = Record(**record)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


@app_router.get("/record/{record_id}/")
def get_retrieve_record(
        record_id: int,
        db: Session = Depends(get_db)
):
    record = db.query(Record).filter(Record.id == record_id).first()
    if record is None:
        raise HTTPException(
            status_code=404,
            detail="record not found"
        )
    return record


@app_router.get("/records/")
async def get_records(
        page: int = Query(default=1, ge=1),
        page_size: int = Query(default=10, le=100),
        db: Session = Depends(get_db)
):
    skip = (page - 1) * page_size
    records = db.query(Record).offset(skip).limit(page_size).all()
    return records
