def generate_signal(data):
    sma = calculate_sma(data)
    return "BUY" if data['close'][-1] > sma[-1] else "SELL"
