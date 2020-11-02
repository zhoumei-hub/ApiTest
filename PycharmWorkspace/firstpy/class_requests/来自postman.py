"""
======================
Author: 柠檬班-小简
Time: 2020/6/24 21:42
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""


import requests

url = "http://api.lemonban.com/futureloan/member/register"

payload = "{\"mobile_phone\":\"18600001111\",\"pwd\":\"123456789\"}"
headers = {
  'X-Lemonban-Media-Type': 'lemonban.v2',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))