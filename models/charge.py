from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint

Base = declarative_base()
class Charge(Base):
    __tablename__ = 'cases'

    id = Column(Integer, primary_key=True)
    tca_code = Column(String, unique=True)
    tca_desc = Column(String)
    filling_date = Column(String)
    violation_date = Column(String)
    disposition_date = Column(String)

    def __repr__(self):
            return "lol"
