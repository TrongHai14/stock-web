from fastapi import APIRouter
from app.services.data_service import get_stock_price
from app.services.indicator_service import add_indicators
from app.services.bank_service import analyze_bank

router = APIRouter()

@router.get("/indicator/{symbol}")
def indicator(symbol: str):
    data = get_stock_price(symbol)
    return add_indicators(data)

@router.get("/bank/{symbol}")
def bank(symbol: str):
    return analyze_bank(symbol)
