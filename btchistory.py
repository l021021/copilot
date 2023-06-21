import requests

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

params = {
    "vs_currency": "usd",
    "days": "30"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    btc_prices = response.json()["prices"]
    print(btc_prices)
else:
    print("Error: Could not retrieve BTC price history.")
