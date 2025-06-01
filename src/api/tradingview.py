import requests

class TradingViewData:
    def __init__(self, symbol="EURUSD"):
        self.symbol = symbol
    
    def get_data(self):
        """Mock data for testing"""
        return {
            'close': [1.08, 1.09, 1.07],
            'volume': [1000, 1500, 800]
        }
