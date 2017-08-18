# -*- coding: UTF-8 -*-

import requests

data = dict(grant_type='password', username='inhanduser', password='ag5fdc1h8hz-vfk')

host = "https://qa01.test.keefegp.com/qa/Vending/VendingApi/token"

response = requests.post(host, data=data)
print(response.status_code)
print(response.text)

access_token = eval(response.text)['access_token']
token_type = eval(response.text)['token_type']
print(access_token)
print(token_type)

inmateurl = "https://qa01.test.keefegp.com/qa/Vending/VendingAPI/api/v1/Accounts/0043555/Balance"

body_data = dict(deviceId="12", transactionId="SayHelloToZippyThePinhead", pin="1234")

# body_data = {
#     "deviceId": "12", "transactionId": "SayHelloToZippyThePinhead", "pin": "1234"
# }

host = "qa01.test.keefegp.com"

auth = "Bearer " + access_token
s = requests.Session()

headers = {
    "Authorization": auth,
}

b_response = s.post(inmateurl, data=body_data, headers=headers)

print(b_response.status_code)
print(b_response.url)
print(b_response.text)


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
