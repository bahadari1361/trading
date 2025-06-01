import pandas as pd

def calculate_sma(data, window=20):
    """Simple Moving Average"""
    return data['close'].rolling(window).mean()

def calculate_rsi(data, window=14):
    """Relative Strength Index"""
    delta = data['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    rs = gain.rolling(window).mean() / loss.rolling(window).mean()
    return 100 - (100 / (1 + rs))
