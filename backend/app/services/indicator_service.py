import pandas as pd

def add_indicators(data):
    df = pd.DataFrame(data)

    # RSI
    delta = df['close'].diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = -delta.clip(upper=0).rolling(14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # MACD
    ema12 = df['close'].ewm(span=12).mean()
    ema26 = df['close'].ewm(span=26).mean()
    df['MACD'] = ema12 - ema26

    # Bollinger
    df['MA20'] = df['close'].rolling(20).mean()
    df['Upper'] = df['MA20'] + 2 * df['close'].rolling(20).std()
    df['Lower'] = df['MA20'] - 2 * df['close'].rolling(20).std()

    return df.to_dict(orient="records")
