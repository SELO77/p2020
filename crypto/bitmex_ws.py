import time
from asyncio import get_event_loop

import websockets

URI = 'wss://www.bitmex.com/realtime'

PUBLIC_TOPICS = {
    "ANNOUNCEMENT": "announcement",  # Site announcements
    "CHAT": "chat",  # Trollbox chat
    "CONNECTED": "connected",  # Statistics of connected users/bots
    "FUNDING": "funding",  # Updates of swap funding rates. Sent every funding interval (usually 8hrs)
    "INSTRUMENT": "instrument",  # Instrument updates including turnover and bid/ask
    "INSURANCE": "insurance",  # Daily Insurance Fund updates
    "LIQUIDATION": "liquidation",  # Liquidation orders as they're entered into the book
    "ORDERBOOKL2_25": "orderBookL2_25",  # Top 25 levels of level 2 order book
    "ORDERBOOKL2": "orderBookL2",  # Full level 2 order book
    "ORDERBOOK10": "orderBook10",  # Top 10 levels using traditional full book push
    "PUBLICNOTIFICATIONS": "publicNotifications",  # System-wide notifications (used for short-lived messages)
    "QUOTE": "quote",  # Top level of the book
    "QUOTEBIN1M": "quoteBin1m",  # 1-minute quote bins
    "QUOTEBIN5M": "quoteBin5m",  # 5-minute quote bins
    "QUOTEBIN1H": "quoteBin1h",  # 1-hour quote bins
    "QUOTEBIN1D": "quoteBin1d",  # 1-day quote bins
    "SETTLEMENT": "settlement",  # Settlements
    "TRADE": "trade",  # Live trades
    "TRADEBIN1M": "tradeBin1m",  # 1-minute trade bins, candle
    "TRADEBIN5M": "tradeBin5m",  # 5-minute trade bins
    "TRADEBIN1H": "tradeBin1h",  # 1-hour trade bins
    "TRADEBIN1D": "tradeBin1d",  # 1-day trade bins
}


BTC = 'XBT'
USD = 'USD'
ETH = 'ETH'

XBTUSD = f'{BTC}{USD}'
ts = lambda : int(time.time())
ms_ts = lambda : int(time.time() * 1000)


async def subscribe_topic(ws, topic, pair=None):
    if pair:
        topic = f'{topic}:{pair}'
    msg = '{"op": "subscribe", "args": ["%s"]}' % topic
    print(f"Send message msg={msg}")
    await ws.send(msg)


async def init():
    row_count = 0

    async with websockets.connect(URI) as ws:
        # await subscribe_topic(ws, PUBLIC_TOPICS['ORDERBOOKL2'], XBTUSD)  # 1초에 약 100개 이상의 객체 전달
        await subscribe_topic(ws, PUBLIC_TOPICS['TRADE'], XBTUSD)
        # await subscribe_topic(ws, PUBLIC_TOPICS['LIQUIDATION'], XBTUSD)
        # await subscribe_topic(ws, PUBLIC_TOPICS['TRADEBIN1M'], XBTUSD)

        st = ts()
        st_ts = ms_ts()
        print(f"Start ms={st_ts}")

        b_ts = ms_ts()
        while True:
            message = await ws.recv()
            c_ts = ms_ts()
            m_interval = c_ts - b_ts
            row_count += 1
            print(f'{ts()-st}/{row_count}/{m_interval}/{message}')

            b_ts = c_ts


if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(init())
