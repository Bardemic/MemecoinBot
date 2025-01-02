class Coin:
    def __init__(self):
        self.name = None
        self.trades = []
        self.market_cap = None
        self.volume = None
        self.link = None
    
    def update_trades(self, trades):
        self.trades = trades
