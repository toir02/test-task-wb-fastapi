from sqlalchemy import (
    Column,
    Integer,
    JSON
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)
