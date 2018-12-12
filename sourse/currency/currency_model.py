from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, String
from app import application as app

Base = declarative_base(app.sqlalchemy)


class Currency(Base):
    __tablename__ = 'currency'
    _id = Column(Integer, primary_key=True)
    ask = Column(Integer)
    ask_change = Column(Integer)
    bid = Column(Integer)
    bid_change = Column(Integer)
    centralbank = Column(Integer)
    centralbank_change = Column(Integer)
    commercial = Column(Integer)
    commercial_change = Column(Integer)
    name = Column(String)
    date = Column(Date)
