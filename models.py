from sqlalchemy import Column, Float, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

class Trade(Base):
    __tablename__ = "trade"

    trade_date_time =  Column(DateTime)
    instrument_id = Column(String)
    instrument_name = Column(String)
    asset_class = Column(String)
    counterparty = Column(String)
    trader = Column(String)
    trade_id = Column(String, primary_key=True, index=True)
    tradeDetails = relationship("TradeDetails", back_populates="trade")


class TradeDetails(Base):
    __tablename__ = "tradeDetails"

    trade_id = Column(Integer, ForeignKey("trade.trade_id"), primary_key=True, index=True)
    buySellIndicator = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

    trade = relationship("Trade", back_populates="tradeDetails")