from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint

Base = declarative_base()
class Case(Base):
    __tablename__ = 'cases'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    case_number = Column(String, unique=True)
    case_name = Column(String)
    status = Column(String)
    filing_date = Column(String)
    status_date = Column(String)

    def __repr__(self):
            return "lol"
