from vnstock import Vnstock

def get_stock_price(symbol: str):
    stock = Vnstock().stock(symbol=symbol, source='VCI')

    df = stock.quote.history(
        start='2024-01-01',
        end='2025-01-01',
        interval='1D'
    )

    return df[['time', 'close']].to_dict(orient='records')
