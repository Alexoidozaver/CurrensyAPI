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

    def to_str(self):
        object_dict = dict()
        object_dict["id"] = self._id
        object_dict["ask"] = self.ask
        object_dict["ask_change"] = self.ask_change
        object_dict["bid"] = self.bid
        object_dict["bid_change"] = self.bid_change
        object_dict["centralbank"] = self.centralbank
        object_dict["centralbank_change"] = self.centralbank_change
        object_dict["commercial"] = self.commercial
        object_dict["commercial_change"] = self.commercial_change
        object_dict["name"] = self.name
        return object_dict
