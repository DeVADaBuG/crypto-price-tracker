import requests

def get_bitcoin_price():
    try:
        res = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        return res.json()['bitcoin']['usd']
    except Exception:
        return 'API Error'

print(f"Current BTC Price: ${get_bitcoin_price()}")
