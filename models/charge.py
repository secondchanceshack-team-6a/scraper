from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Sequence
from sqlalchemy.orm import relationship
from models.case import Case

Base = declarative_base()
class Charge(Base):
    __tablename__ = 'charges'

    id = Column(Integer, Sequence('charge_id_seq'), primary_key=True)
    tca_code = Column(String, unique=True, nullable=False)
    tca_desc = Column(String, nullable=False)
    filing_date = Column(String, nullable=False)
    violation_date = Column(String, nullable=False)
    disposition_date = Column(String, nullable=False)
    case_id = Column('person_id', Integer, ForeignKey(Case.id), nullable=False)
    

    def __repr__(self):
            return "lol"
