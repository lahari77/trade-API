from typing import List, Union

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
import pandas as pd
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)
import datetime as dt

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def load_db(db: Session = Depends(get_db)):
    trade_file = 'trade.csv'
    trade_details_file = 'trade_details.csv'
    df = pd.read_csv(trade_file)
    df2 = pd.read_csv(trade_details_file)
    df.to_sql(con=engine, index_label='id', name=models.Trade.__tablename__, if_exists='replace')
    df2.to_sql(con=engine, index_label='id', name=models.TradeDetails.__tablename__, if_exists='replace')
                
    return "Done"

@app.get("/trades/")
def get_trades( search: Union[str, None] = None,
                assetClass: Union[str, None] = None,
                end: Union[dt.datetime, None] = None,
                maxPrice: Union[float, None] = None,
                minPrice: Union[float, None] = None,
                start: Union[dt.datetime, None] = None,
                tradeType: Union[str, None] = None, 
                db: Session = Depends(get_db)):
                
    trades = crud.get_trades(db)
    return trades


@app.get("/trades/{trade_id}", response_model=schemas.Trade)
def get_trade_by_id(trade_id: int, db: Session = Depends(get_db)):
    db_trade = crud.get_trade_by_id(db, trade_id=trade_id)
    if db_trade is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_trade
