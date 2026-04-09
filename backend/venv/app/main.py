from fastapi import FastAPI
from app.routers import stock, analysis, valuation

app = FastAPI()

app.include_router(stock.router, prefix="/stock")
app.include_router(analysis.router, prefix="/analysis")
app.include_router(valuation.router, prefix="/valuation")

@app.get("/")
def root():
    return {"message": "Stock Pro API 🚀"}
