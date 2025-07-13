import requests

def exchange_rate():
    exchange = "af1f09ab2857826bd7cc046804a785ad"
    url = "https://api.exchangerate.host/live"
    params = {
              "access_key": exchange,
              "source": "USD",
              "currencies": "IDR"
            }
    response = requests.get(url, params=params)
    data = response.json()

    return(float(data["quotes"]["USDIDR"]))

print(exchange_rate())

