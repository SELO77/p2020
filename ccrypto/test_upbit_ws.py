import asyncio
import traceback
from enum import Enum
from typing import Optional

import websockets
from websockets.client import Connect


# https://docs.upbit.com/docs/upbit-quotation-websocket
class UPBITEnum(Enum):
    NAME = 'Upbit'
    WS_BASE_URI = 'wss://api.upbit.com/websocket/v1'
    WS_SUB_TOPIC_MESSAGE_TEMPLATE = '[{"ticket":"tyranno77"},{"type":"%s","codes":["%s"], "isOnlySnapshot": %s}, {"format": "%s"}]'
    WS_MESSAGE_FORMAT_DEFAULT = 'DEFAULT'
    WS_MESSAGE_FORMAT_SIMPLE = 'SIMPLE'
    WS_TOPICS = {
        'ORDER_BOOK': 'orderbook',
        'TRADE': 'trade',
        'TICKER': 'ticker',
    }
    WS_IS_ONLY_SNAPSOT_TRUE = "true"
    WS_IS_ONLY_SNAPSOT_FALSE = "false"
    KRW_BTC = 'KRW-BTC'

    WS_ORDER_BOOK_SUB_MESSAGE = WS_SUB_TOPIC_MESSAGE_TEMPLATE % (WS_TOPICS['ORDER_BOOK'],
                                                                 KRW_BTC,
                                                                 WS_IS_ONLY_SNAPSOT_FALSE,
                                                                 WS_MESSAGE_FORMAT_DEFAULT)

    WS_TRADE_SUB_MESSAGE = WS_SUB_TOPIC_MESSAGE_TEMPLATE % (WS_TOPICS['TRADE'],
                                                            KRW_BTC,
                                                            WS_IS_ONLY_SNAPSOT_FALSE,
                                                            WS_MESSAGE_FORMAT_DEFAULT)

    WS_TICKER_SUB_MESSAGE = WS_SUB_TOPIC_MESSAGE_TEMPLATE % (WS_TOPICS['TICKER'],
                                                             KRW_BTC,
                                                             WS_IS_ONLY_SNAPSOT_FALSE,
                                                             WS_MESSAGE_FORMAT_DEFAULT)


class Subscriber:
    def __init__(self, name, uri, **kwargs):
        self.name = name
        self.uri = uri
        self.kwargs = kwargs
        self.is_open = False
        self.ws: Optional[Connect] = None
        self.messages = []

    async def init(self):
        print(f'{self} start to initialize.')
        await self.__init()

    def __str__(self):
        return f'Subscriber({self.name})'

    async def __init(self):
        await self.connect()
        while self.is_open:
            message = await self.ws.recv()
            print(f'received msg={message}')
            await self.on_message(message)
            if not self.is_open:
                await self.close()

    async def before_connect(self, **kwargs):
        pass

    async def after_connect(self, **kwargs):
        pass

    async def wait_connect(self):
        while not self.is_open:
            await asyncio.sleep(1)

    async def connect(self):
        if self.is_open: return
        await self.before_connect()
        try:
            self.ws = await websockets.connect(self.uri)
            self.is_open = True
        except Exception as e:
            print(f'{self}, open failed. e={repr(e)}, trace={traceback.format_exc()}')
        await self.after_connect()

    async def before_close(self, **kwargs):
        pass

    async def after_close(self, **kwargs):
        pass

    async def close(self):
        await self.before_close()
        await self.ws.close()
        self.is_open = False
        await self.after_close()

    async def on_message(self, message_pack):
        self.messages.append(message_pack)

    async def send_message(self, message):
        print(f'sending ws message={message}')
        await self.ws.send(message)

    async def ping(self):
        await self.send_message('PING')


class Collector(Subscriber):
    async def on_message(self, message_pack):
        await super(Collector, self).on_message(message_pack)

    def handle_data(self, _id):
        pass
