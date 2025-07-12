from colorama import Fore, Style
import pyfiglet
from datetime import datetime
import pandas as pd

harga_coin = {
    "BTC": {
        "2021-01-01": 400_000_000,
        "2021-12-01": 800_000_000,
        "2023-01-01": 350_000_000
    },
    "ETH": {
        "2021-01-01": 12_000_000,
        "2021-12-01": 60_000_000,
        "2023-01-01": 22_000_000
    }
}

# welcome Massage
banner = pyfiglet.figlet_format("WELCOME TO")

print(" ")
print(" ")
print(Fore.MAGENTA + "="*60 + Style.RESET_ALL)
print(Fore.MAGENTA + "="*60 + Style.RESET_ALL)
print(" ")
print(Fore.YELLOW + banner.rstrip() + Style.RESET_ALL)
print(" ")
print(Fore.YELLOW + "-------------Past Crypto Profit/Loss Simulator-------------"  + Style.RESET_ALL)
print(" ")
print(Fore.MAGENTA + "="*60 + Style.RESET_ALL)
print(Fore.MAGENTA + "created by Fachrizal Ainurrahman|Github : github.com/samezid" + Style.RESET_ALL)
print(Fore.MAGENTA + "="*60 + Style.RESET_ALL)
print(" ")
print(" ")

# input user
print("-"*60)

while True:
    try:
        jenis_coin = input("Masukkan Jenis Coin (Contoh : BTC/ETH) : ".upper())
        if jenis_coin not in ["BTC", "ETH"]:
            raise ValueError("jenis coin tidak tersedia")
        break
    except ValueError:
        print("jenis coin tidak tersedia")

while True:
    try:
        modal = float(input("Masukkan Jumlah Modal Beli Coin : Rp."))
        break
    except ValueError:
        print("input harus diisi dengan angka dan tidak boleh 0, silakan coba lagi.")

while True:
    try:
        tanggal_beli = input("Masukkan Simulasi Tanggal Beli Coin (Format YYYY-MM-DD) : ")
        break
    except ValueError:
        print("tanggal tidak tersedia")

while True:
    try:
        tanggal_jual = input("Masukkan Simulasi Tanggal Jual Coin (Format YYYY-MM-DD) : ")
        break
    except ValueError:
        print("tanggal tidak tersedia")


# -------------------------
print("-"*60)

# validasi input


# operasi
harga_beli = harga_coin[jenis_coin][tanggal_beli] #mendapat harga saat beli disimpan di = harga_beli
jumlah_coin = modal/ harga_beli #mendapat jumlah coin dari sejumlah modal

harga_jual = harga_coin[jenis_coin][tanggal_jual] #mendapat harga saat mau jual disimpat di = harga_jual
gain = jumlah_coin * harga_jual

laba = gain - modal




# output
print(f"Harga {jenis_coin} saat beli : {harga_beli}")
print(f"Jumlah {jenis_coin} yang didapat sebanyak : {jumlah_coin}")
print(f"harga {jenis_coin} saat jual : {harga_jual}")
print(f"pendapatan yang diperoleh : {gain}")
print(f"keuntungan bersih : {laba}")
print("-"*60)
