import requests
import json


url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()

rate_float = data ["bpi"]["EUR"]
current_rate = rate_float ["rate"]
print(current_rate,response.status_code)
