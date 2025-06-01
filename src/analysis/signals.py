from .indicators import calculate_sma, calculate_rsi

def generate_signals(data):
    """Basic SMA crossover strategy"""
    signals = []
    sma_short = calculate_sma(data, window=5)
    sma_long = calculate_sma(data, window=20)
    
    for i in range(1, len(data)):
        if sma_short[i] > sma_long[i] and sma_short[i-1] <= sma_long[i-1]:
            signals.append("BUY")
        elif sma_short[i] < sma_long[i] and sma_short[i-1] >= sma_long[i-1]:
            signals.append("SELL")
        else:
            signals.append("HOLD")
    return signals
