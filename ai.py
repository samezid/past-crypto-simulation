import requests
from datetime import datetime, timedelta

# Token dari CoinCap dan exchangerate-host (dalam format access_key)
COINCAP_TOKEN = "11aec9beacb072ec7c03416cb39702eadc201d872e8f24c16458943023023acf"
EXCHANGE_ACCESS_KEY = "af1f09ab2857826bd7cc046804a785ad"

def get_usd_to_idr_rate():
    url = "https://api.exchangerate.host/live"
    params = {
                "access_key": EXCHANGE_ACCESS_KEY,
                "source": "USD",
                "currencies": "IDR"
             }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("success"):
            return float(data["quotes"]["USDIDR"])
        else:
            print("Gagal ambil kurs: response tidak berhasil")
            return 15000
    except Exception as e:
        print("Gagal ambil kurs USD → IDR:", e)
        return 15000

def get_price_on_date(coin_id, date_str):
    try:
        # Konversi tanggal ke UNIX timestamp ms
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

        if "data" in data and data["data"]:
            price_usd = float(data["data"][0]["priceUsd"])
            rate = get_usd_to_idr_rate()
            price_idr = price_usd * rate

            print(f"\nHarga {coin_id} pada {date_str}:")
            print(f"USD : ${price_usd:,.2f}")
            print(f"IDR : Rp{price_idr:,.0f}")
        else:
            print(f"Tidak ada data harga {coin_id} pada {date_str}.")

    except Exception as e:
        print("Terjadi kesalahan:", e)

# ========== MAIN ==========
coin = input("Masukkan nama coin (contoh: bitcoin): ").lower()
tanggal = input("Masukkan tanggal (format YYYY-MM-DD): ")
get_price_on_date(coin, tanggal)
