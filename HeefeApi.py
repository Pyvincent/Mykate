# -*- coding: UTF-8 -*-

import requests
import json

data = dict(grant_type='password', username='inhanduser', password='ag5fdc1h8hz-vfk')

host = "https://qa01.test.keefegp.com/qa/Vending/VendingApi/token"
inmateurl = "https://qa01.test.keefegp.com/qa/Vending/VendingAPI/api/v1/Accounts/45346/history"
purchaseurl = "https://qa01.test.keefegp.com/qa/Vending/VendingAPI/api/v1/Accounts/45346/purchase"
refundurl = "https://qa01.test.keefegp.com/qa/Vending/VendingAPI/api/v1/Accounts/45346/refund"

s = requests.Session()

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset-UTF-8",
    "Accept": "/",
    "Host": "qa01.test.keefegp.com",
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)"
}

purchase_body = {
    "deviceId": "12",
    "transactionId": "ZippyThePinhead",
    "pin": "1234",
    "lineItems":
        [
            {
                "itemId": "7689",
                "slotId": "B1",
                "amount": 1.50,
            }
        ]

}

response = s.post(host, data=data, headers=headers)
print(response.status_code)
print(response.text)

access_token = eval(response.text)['access_token']
token_type = eval(response.text)['token_type']
print(access_token)
print(token_type)
auth = "Bearer " + access_token

headersall = {
    "Authorization": auth,
    "Content-type": "application/json",
    "Accept": "/",
    "Host": "qa01.test.keefegp.com",
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)"
}

purchase_body = s.post(purchaseurl, data=json.dumps(purchase_body), headers=headersall)
print(purchase_body.url)
print(purchase_body.status_code)
print(purchase_body.text)

body_data = dict(deviceId="12", pin="1234")
history = s.post(inmateurl, data=json.dumps(body_data), headers=headersall)
print(history.url)
print(history.status_code)
print(history.text)

refund_data = dict(deviceId="12", transactionId="ZippyThePinhead", pin="1234", amount=1.50)
refund = s.post(refundurl, data=json.dumps(refund_data), headers=headersall)
print(refund.url)
print(refund.status_code)
print(refund.text)

# inmateurl = "https://qa01.test.keefegp.com/qa/Vending/VendingAPI/api/v1/Accounts/0043555/Balance"
#
# body_data = dict(deviceId="12", transactionId="SayHelloToZippyThePinhead", Pin="1234")

# body_data = {
#     "deviceId": "12", "transactionId": "SayHelloToZippyThePinhead", "pin": "1234"
# }

# host = "qa01.test.keefegp.com"
#
# auth = "Bearer " + access_token
# s = requests.Session()
#
# headers = {
#     "Authorization": auth,
# }
#
# b_response = s.post(inmateurl, data=body_data, headers=headers)
#
# print(b_response.status_code)
# print(b_response.url)
# print(b_response.text)


# /********2************/

# from urllib.request import Request,urlopen
# from urllib.parse import urlencode
#
# url = "https://qa01.test.keefegp.com/qa/Vending/VendingApi/token"
#
# data = {'grant_type': 'password', 'username': 'inhanduser', 'password': 'ag5fdc1h8hz-vfk'}
#
# re = Request(url, urlencode(data).encode())
# json = urlopen(re).read().decode()
# print(json)

inmateurl = "https://qa01.test.keefegp.com/qa/Vending/VendingAPI/api/v1/Accounts/0043555/history"
purchaseurl = "https://qa01.test.keefegp.com/qa/Vending/VendingAPI/api/v1/Accounts/0043555/purchase"
refundurl = "https://qa01.test.keefegp.com/qa/Vending/VendingAPI/api/v1/Accounts/0043555/refund"

s = requests.Session()
auth = "Bearer " + "P3hAs_3U3__gM7e_C-U2KP3Jrhf0Znma_G-9e8EyJQmrsEVKNYiPxrZUuik3QDsG2jLQHAoGjcJHZvpApkvgQIhKtYEbZIUbe3gKnAlffnlea6-2yJWzJOuD6_EayD6FHEQ--D6JPx75G22gx2EEGvKphNpwZc097OvEw7PvOuKOzIiM9aKVHArqno5eha4lGOis69gQWQlcUPsmKz9nQA"

headers = {
    "Authorization": auth,
    "Content-type": "application/json",
    "Accept":"/",
    # "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
}

purchase_body = {
    "deviceId": "12",
    "transactionId": "SayHelloToZippyThePinhead",
    "pin": "1234",
    "lineItems":
        [
            {
                "itemId": "10057",
                "slotId": "B1",
                "amount": 1.23
            }
        ]

}

# purchase_body = dict(deviceId="12", transactionId="SayHelloToZippyThePinhead", pin="1234", lineItems=lineItem)
purchase_body = s.post(purchaseurl, data=json.dumps(purchase_body), headers=headers)
print(purchase_body.url)
print(purchase_body.status_code)
print(purchase_body.text)

body_data = dict(deviceId="12", pin="1234")
history = s.post(inmateurl, data=json.dumps(body_data), headers=headers)
print(history.url)
print(history.status_code)
print(history.text)

refund_data = dict(deviceId="12", transactionId="SayHelloToZippyThePinhead", pin="1234", amount=3.0)
refund = s.post(refundurl, data=json.dumps(refund_data), headers=headers)
print(refund.url)
print(refund.status_code)
print(refund.text)




# P3hAs_3U3__gM7e_C-U2KP3Jrhf0Znma_G-9e8EyJQmrsEVKNYiPxrZUuik3QDsG2jLQHAoGjcJHZvpApkvgQIhKtYEbZIUbe3gKnAlffnlea6-2yJWzJOuD6_EayD6FHEQ--D6JPx75G22gx2EEGvKphNpwZc097OvEw7PvOuKOzIiM9aKVHArqno5eha4lGOis69gQWQlcUPsmKz9nQA
# bearer

