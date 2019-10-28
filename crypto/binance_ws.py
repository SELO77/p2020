import time
from asyncio import get_event_loop

import websockets

BTC = 'btc'
USD = 'usdt'

IT_1M = '1m'

# All symbols for streams are lowercase
BTCUSD = f'{BTC}{USD}'
ts = lambda : int(time.time())
ms_ts = lambda : int(time.time() * 1000)

# wss://fstream.binance.com/ws/btcusdt@ticker
URI = 'wss://fstream.binance.com/'
COMBINED_STREAM_URI = URI + 'stream?streams='

SUB_COMBINED_STREAM_URI = COMBINED_STREAM_URI + f'{BTCUSD}@ticker/{BTCUSD}@depth/{BTCUSD}@kline_{IT_1M}'
STREAM_NAME_FORMAT = '{symbol}@{name}'

# https://binance-docs.github.io/apidocs/futures/en/#symbol-order-book-ticker-market_data
PUBLIC_TOPICS = {
    'Aggregate Trade Streams': 'aggTrade',
    'Mark Price Stream': 'markPrice',
    'CANDLE': 'kline_{interval}',
    'Ticker': 'ticker',
    'ORDERBOOK-DELTA': 'depth',
}


async def subscribe_topic(ws, topic, pair=None):
    if pair:
        topic = f'{topic}:{pair}'
    msg = '{"op": "subscribe", "args": ["%s"]}' % topic
    print(f"Send message msg={msg}")
    await ws.send(msg)


async def test():
    uri = SUB_COMBINED_STREAM_URI
    print(uri)
    async with websockets.connect(uri) as ws:
        while True:
            message = await ws.recv()
            print(f'{ms_ts()},{message}')


if __name__ == '__main__':
    loop = get_event_loop()
    # t = loop.create_task(test())
    # asyncio.gather(*[t])
    loop.run_until_complete(test())
