from sqlalchemy.orm import Session
import models
from sqlalchemy import or_


def get_trade_by_id(db: Session, trade_id: int):
    return db.query(models.Trade).filter(models.Trade.trade_id == trade_id).first()


def get_trades(db: Session, search, assetClass, end, maxPrice, minPrice, start, tradeType, skip: int = 0, limit: int = 100):
    query = db.query(models.Trade).join(models.TradeDetails).filter(or_(models.Trade.counterparty.like(search)),
                                        or_(models.Trade.instrument_id.like(search)),
                                        or_(models.Trade.instrument_name.like(search)),
                                        or_(models.Trade.trader.like(search)),
                                        or_(models.Trade.trade_date_time < end),
                                        or_(models.Trade.trade_date_time > start),
                                        or_(models.TradeDetails.price > minPrice),
                                        or_(models.TradeDetails.price < maxPrice),
                                        or_(models.Trade.trade_date_time > start),
                                        or_(models.TradeDetails.buySellIndicator == tradeType),
                                        or_(models.Trade.asset_class == assetClass),
                                        ).distinct().offset(skip).limit(limit).all()
    return query