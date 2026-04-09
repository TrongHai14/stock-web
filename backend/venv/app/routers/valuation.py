from fastapi import APIRouter
from app.services.valuation_service import pb

router = APIRouter()

@router.get("/pb")
def get_pb(price: float, book: float):
    return {"PB": pb(price, book)}
