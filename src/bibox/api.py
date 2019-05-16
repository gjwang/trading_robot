#-*- coding:utf-8 -*-

import hmac
import hashlib
import json, requests

#1-买，2-卖
ORDER_SIDE_BUY  = 1
ORDER_SIDE_SELL = 2

#订单类型，2-限价单
#ORDER_TYPE_MARKET = ?
ORDER_TYPE_LIMIT = 2

ACCOUNT_TYPE_COMMON = 0  #0-普通账户
account_type = ACCOUNT_TYPE_COMMON
BIBOX_API = "https://api.bibox.com/v1/orderpending"

class BiboxClient(object):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        
    def getSign(self, data):
        result = hmac.new(self.api_secret.encode("utf-8"), data.encode("utf-8"), hashlib.md5).hexdigest()
        return result
    
    def doApiRequestWithApikey(self, url, cmds):
        s_cmds = json.dumps(cmds)
        sign = self.getSign(s_cmds)
        r = requests.post(url, data={'cmds': s_cmds, 'apikey': self.api_key,'sign':sign})
        print(r.text)
        return r.text
    
    def post_order(self, cmds):
        return self.doApiRequestWithApikey(BIBOX_API,cmds)
    
    def order_buy(self, pair, order_type, price, amount):
        return self.order_create(pair, order_type, ORDER_SIDE_BUY, price, amount)
    
    def order_sell(self, pair, order_type, price, amount):
        return self.order_create(pair, order_type, ORDER_SIDE_SELL, price, amount)
        
    def order_create(self, pair, order_type, order_side, price, amount):
        cmds = [
            {
                'cmd':"orderpending/trade",
                'body':{
                    'pair':pair,
                    'account_type':ACCOUNT_TYPE_COMMON,
                    'order_type':order_type,
                    'order_side':order_side,
                    'price':price,
                    'amount':amount,
                }
            }
        ]
        
        result =  self.post_order(cmds)
        order_id = json.loads(result)['result'][0]['result']
        return order_id
        
    def order_cancel(self, order_id):
        cmds = [
            {
                'cmd':"orderpending/cancelTrade",
                'body':{
                    'orders_id':order_id,
                }
            }
        ]        

        self.post_order(cmds)


