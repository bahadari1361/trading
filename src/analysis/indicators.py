import pandas as pd

def calculate_sma(data, window=5):
    return pd.Series(data['close']).rolling(window).mean()
