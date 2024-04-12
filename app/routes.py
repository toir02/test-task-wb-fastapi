from fastapi import (
    APIRouter,
    Depends
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
