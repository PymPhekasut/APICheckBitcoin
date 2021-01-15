#ProgramCheck.py

condition = {'THB_BTC':{'buy':950000,'sell':1080000},
             'THB_ETH':{'buy':20000,'sell':30000},
             'THB_DOGE':{'buy':0.459,'sell':0.615},}

#print(condition['THB_BTC'])

def CheckCondition(coin,price):
    #coin = 'THB_BTC',price = 1050000
    text = ''
    check_buy = condition[coin]['buy']
    if price <= check_buy:
        txt = '{} Low price! only {:,.3f} Go to buy!\ngood price: {:,.3f}'.format(coin,price,check_buy)
        print(txt)
        text += txt + '\n--------'
        
    check_sell = condition[coin]['sell']
    if price >= check_sell:
        txt = '{} High price! only {:,.3f} Go to sell!\ngood price: {:,.3f}'.format(coin,price,check_sell)
        print(text)
        text +=txt + '\n'

    return text
           


CheckCondition('THB_BTC',10000)
