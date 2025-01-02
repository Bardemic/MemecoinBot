class Trade:
    def __init__(self, trade_type, sol, meme_coin):
        if trade_type != "buy" and trade_type != "sell":
            raise ValueError("type incorrect name")
        
        self.trade_type = trade_type
        self.sol_amount = sol
        self.meme_coin_amount = meme_coin

