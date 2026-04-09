from fastapi import APIRouter
from app.services.data_service import get_stock_price

router = APIRouter()

@router.get("/price/{symbol}")
def price(symbol: str):
    return get_stock_price(symbol)
