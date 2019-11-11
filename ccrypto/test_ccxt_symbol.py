from ccxt.base import exchange

print(exchange.load_markets())

etheur1 = exchange.markets['ETH/EUR']  # get market structure by symbol
etheur2 = exchange.market('ETH/EUR')  # same result in a slightly different way

etheurId = exchange.market_id('BTC/USD')  # get market id by symbol

symbols = exchange.symbols  # get a list of symbols
symbols2 = list(exchange.markets.keys())  # same as previous line

print(exchange.id, symbols)  # print all symbols

currencies = exchange.currencies  # a list of currencies

kraken = ccxt.kraken()
kraken.load_markets()

kraken.markets['BTC/USD']  # symbol → market (get market by symbol)
kraken.markets_by_id['XXRPZUSD']  # id → market (get market by id)

kraken.markets['BTC/USD']['id']  # symbol → id (get id by symbol)
kraken.markets_by_id['XXRPZUSD']['symbol']  #
