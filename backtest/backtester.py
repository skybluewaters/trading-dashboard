from strategies.momentum_strategy import MomentumStrategy

class Backtester:
    def __init__(self, prices, asset):
        self.strategy = MomentumStrategy(asset)
        self.strategy.prices = prices[:20]
        self.trades = []
        self.position = None

    def run(self):
        for price in prices[20:]:
            self.strategy.prices.append(price)
            if self.strategy.should_buy():
                if self.position != 'long':
                    self.trades.append(('buy', price))
                    self.position = 'long'
            elif self.strategy.should_sell():
                if self.position != 'short':
                    self.trades.append(('sell', price))
                    self.position = 'short'
        return self.trades

