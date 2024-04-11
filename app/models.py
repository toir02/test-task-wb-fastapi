from sqlalchemy import (
    Column,
    Integer,
    JSON
)

from app.database import Base


class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)
