from colorama import Fore, Style
import pyfiglet
from datetime import datetime

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
print(Fore.YELLOW + "-------------Past Crypto Profit/Loss Simulation-------------"  + Style.RESET_ALL)
print(" ")
print(Fore.MAGENTA + "="*60 + Style.RESET_ALL)
print(Fore.MAGENTA + "created by Fachrizal Ainurrahman|Github : github.com/samezid" + Style.RESET_ALL)
print(Fore.MAGENTA + "="*60 + Style.RESET_ALL)
print(" ")
print(" ")

# input user
print("-"*60)
jenis_coin = input("Masukkan Jenis Coin (Contoh : BTC/ETH) : ".upper())
modal = float(input("Masukkan Jumlah Modal Beli Coin : Rp."))
tanggal_beli = input("Masukkan Simulasi Tanggal Beli Coin (Format YYYY-MM-DD) : ")
tanggal_jual = input("Masukkan Simulasi Tanggal Jual Coin (Format YYYY-MM-DD) : ")
print("-"*60)

# validasi input


# operasi
harga_beli = harga_coin[jenis_coin][tanggal_beli]
harga_jual = harga_coin[jenis_coin][tanggal_jual]

print(harga_beli)
print(harga_jual)
