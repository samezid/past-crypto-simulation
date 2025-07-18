import requests
from datetime import datetime, timedelta
from exchange_rate import usdidr

COINCAP_TOKEN = "11aec9beacb072ec7c03416cb39702eadc201d872e8f24c16458943023023acf"

def get_coin_rate(coin_id,  date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        start = int(date.timestamp() * 1000)
        end = int((date + timedelta(days=1)).timestamp() * 1000)

        url = f"https://rest.coincap.io/v3/assets/{coin_id}/history"
        headers = {
            "Authorization": f"Bearer {COINCAP_TOKEN}"
        }
        params = {
            "interval": "d1",
            "start": start,
            "end": end
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        coin_price = float(data["data"][0]["priceUsd"])
        exchange_to_idr = coin_price * usdidr

        return exchange_to_idr

    except Exception as e:
          print("Terjadi kesalahan:", e)


print(get_coin_rate("bitcoin", "2024-01-01"))
