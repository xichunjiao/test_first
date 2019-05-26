import requests,json
url_login='http://www.weboffcial.com'
url_purchase='http://www.weboffcial.com/purchase.php'
data_login={
    'username':'张三',
    'password':'123456'
}
data_purchase={
    'userid':'',
    'purchaseAmount':'',
    'accountBalance':'',
    'purchaseBid':'111111'
}
# data0=json.dumps(data)
data_purchase['purchaseAmount']=1000
r_login=requests.post(url_login,json.dumps(data_login))
print(r_login.text)
data_login_rsp=json.loads(r_login.text)
data_purchase['userid']=data_login_rsp['userid']
data_purchase['accountBalance']=data_login_rsp['accountBalance']
r_purchase=requests.post(url_purchase,json.dumps(data_purchase))
print(r_purchase.text)




