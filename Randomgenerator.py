import requests
import json
import time


url = "http://localhost:8080/stock/"

response = requests.get("http://localhost:8080/stock/all")

if response.status_code == 200:
    stocks = response.json()
    stock_ids = [stock['stockId'] for stock in stocks]
    # print(stock_ids)

    # print("Error: Could not retrieve stocks.")


headers = {'content-type': 'application/json'}
arrli = stock_ids


def getPayload(price, val):
    return {
        "email": "a_t",
        "stockId": val,
        "price": price
    }


price = 100
val = ""
while 1:

    while price > 30:

        price -= 10
        for num in arrli:
            val = num
            response = requests.put(url, data=json.dumps(
                getPayload(price, val)), headers=headers)
        # print(response.status_code)
        # print(response.json())
        time.sleep(0.5)
    while price < 120:
        price += 10
        for num in arrli:
            val = num
            response = requests.put(url, data=json.dumps(
                getPayload(price, val)), headers=headers)
        # response = requests.put(url, data=json.dumps(getPayload(price,val)), headers=headers)
        # print(response.status_code)
        # print(response.json())
        time.sleep(0.5)
