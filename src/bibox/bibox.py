'''
Created on May 15, 2019

@author: gjwang
'''

from api import BiboxClient
from api import ORDER_TYPE_LIMIT

api_key    = 'your_api_key'
api_secret = 'your_api_secret'

if __name__ == '__main__':
    biboxClient = BiboxClient(api_key, api_secret)
    
    pair = 'FOR_USDT' 
    biboxClient.order_buy(pair, order_type=ORDER_TYPE_LIMIT, price=0.01, amount=100)
    biboxClient.order_sell(pair, order_type=ORDER_TYPE_LIMIT, price=1, amount=1)
    
    order_id = biboxClient.order_sell(pair, order_type=ORDER_TYPE_LIMIT, price=1, amount=1.1)
    biboxClient.order_cancel(order_id)
