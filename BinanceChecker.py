#BinanceChecker

from binance.client import Client

api_key = '---------------'
api_secret = '-----------------'
client = Client(api_key, api_secret)

#depth = client.get_order_book(symbol='BNBBTC')
#print(depth)


prices = client.get_all_tickers()

mycoin = ['BTCBUSD','DOGEBUSD','ETHBUSD'] #check several coin

for p in prices:
    for c in mycoin:
        sym = c
        if p['symbol'] == sym:
            #print(p)
            pc = float(p['price']) #bitcoin price 
            rate = 1.30 #1 USD = 1 AUD
            cal = pc*rate
            print('bitcoin: {} price: {:,.2f} AUD'.format(sym,cal))
            print('USD price: {}'.format(pc))
