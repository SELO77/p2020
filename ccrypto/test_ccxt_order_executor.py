import ccxt
from environs import Env


env = Env()
env.read_env()

UPBIT_ACCESS_KEY = env('UPBIT_ACCESS_KEY')
UPBIT_SECRET_KEY = env('UPBIT_SECRET_KEY')


config = {
    'apiKey': UPBIT_ACCESS_KEY, 'secret': UPBIT_SECRET_KEY,
}

# CCXT Example, https://github.com/ccxt/ccxt/tree/master/examples/py
upbit = ccxt.upbit(config=config) # 1000원 단위 주문 가능

binance = ccxt.binance()

BTCKRW = 'BTC/KRW'
BTCUSDT = 'BTC/USDT'


def test():
    # print(upbit.load_markets())
    print(upbit.fetch_ticker(BTCKRW))
    print(upbit.fetch_balance())
    upbit_order_book = upbit.fetch_order_book(BTCKRW)

    symbol = BTCKRW
    expected_trades_base_amount = int(input("EXPECTED ORDER AMOUNT KRW > ")) # WON

    dt = upbit_order_book['datetime']
    print(dt)
    bids = upbit_order_book['bids']
    asks = upbit_order_book['asks']
    for row in bids:
        print(row)

    print("----")

    bid_order_range = bids[-8:]
    first_order = bid_order_range[0]

    largest_amount_at_price = first_order[0]
    largest_amount = first_order[1]

    _c = 0
    for price, amount in bid_order_range:
        if amount >= largest_amount:
            largest_amount = amount
            largest_amount_at_price = price
        _c +=1

    order_price = largest_amount_at_price + 2000
    order_amount = expected_trades_base_amount / order_price
    print(order_price, order_amount)


    order_dict = {
        'symbol': symbol,
        'type': 'limit',
        'side': 'buy',
        'amount': order_amount,
        'price': order_price,

    }


    ### WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING
    ### WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING
    ### WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING
    ### WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING
    ### WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING

    ### ORDER EXECUTE
    ## symbol, type, side, amount, price = None, params = {}
    executed_order = upbit.create_order(**order_dict)
    print(executed_order)
    order_id = executed_order['id']
    #
    #
    # # CANCLE ORDER
    # sleep(3)
    # upbit.cancel_order(order_id)

    # binance_order_book = binance.fetch_order_book(BTCUSDT)
    # print(binance.fetch_ticker(BTCUSDT))

    ### WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING
    ### WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING
    ### WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING
    ### WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING
    ### WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING WARNNING


if __name__ == '__main__':
    test()
