import asyncio
from data.market_data import stream_price_feed
from strategies.momentum_strategy import MomentumStrategy
from execution.broker_interface import place_order
from alerts.notifier import send_alert

ASSET = 'BTC-USD'
QUANTITY = 1

strategy = MomentumStrategy(ASSET)

async def handle_price(price):
    strategy.on_new_price(price)
    if strategy.should_buy():
        place_order(ASSET, 'buy', QUANTITY)
        send_alert(f"BUY signal for {ASSET} at {price:.2f}")
    elif strategy.should_sell():
        place_order(ASSET, 'sell', QUANTITY)
        send_alert(f"SELL signal for {ASSET} at {price:.2f}")

async def run():
    await stream_price_feed(ASSET, handle_price)

if __name__ == '__main__':
    asyncio.run(run())

