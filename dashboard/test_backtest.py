from backtest.backtester import Backtester
import random
import matplotlib.pyplot as plt

# Simulate historical price data
prices = [random.uniform(90, 110) for _ in range(100)]
asset = 'btcusdt'

# Run the backtest
bt = Backtester(prices, asset)
trades = bt.run()

# Output the trades
print("Trades Executed:")
for trade in trades:
    print(trade)

# Plot price with buy/sell markers
buy_signals = [i for i, t in enumerate(trades) if t[0] == 'buy']
sell_signals = [i for i, t in enumerate(trades) if t[0] == 'sell']
buy_prices = [t[1] for t in trades if t[0] == 'buy']
sell_prices = [t[1] for t in trades if t[0] == 'sell']

plt.plot(prices, label="Price")
plt.scatter(buy_signals, buy_prices, marker='^', color='green', label="Buy")
plt.scatter(sell_signals, sell_prices, marker='v', color='red', label="Sell")
plt.title("Backtest Trade Signals")
plt.legend()
plt.show()


