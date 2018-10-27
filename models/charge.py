from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy import ForeignKey

Base = declarative_base()
class Charge(Base):
    __tablename__ = 'cases'

    id = Column(Integer, primary_key=True)
    tca_code = Column(String, unique=True, nullable=False)
    tca_desc = Column(String, nullable=False)
    filing_date = Column(String, nullable=False)
    violation_date = Column(String, nullable=False)
    disposition_date = Column(String, nullable=False)
    case_id = Column(Integer, ForeignKey('cases.id'), nullable=False)

    def __repr__(self):
            return "lol"
