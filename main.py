from colorama import Fore, Style
import pyfiglet

banner = pyfiglet.figlet_format("WELCOME TO")


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
print(" ")
print(" ")
print(Fore.MAGENTA + "="*60 + Style.RESET_ALL)
print(Fore.MAGENTA + "="*60 + Style.RESET_ALL)
print(" ")
print(Fore.YELLOW + banner.rstrip() + Style.RESET_ALL)
print(" ")
print(Fore.YELLOW + "-------------Past Cryto Profit/Loss Simulation-------------"  + Style.RESET_ALL)
print(" ")
print(Fore.MAGENTA + "="*60 + Style.RESET_ALL)
print(Fore.MAGENTA + "created by Fachrizal Ainurrahman|Github : github.com/samezid" + Style.RESET_ALL)
print(Fore.MAGENTA + "="*60 + Style.RESET_ALL)
print(" ")
print(" ")

# input user
print("-"*60)
jenis_coin = input("Masukkan Jenis Coin (Contoh : BTC/ETH) : ".upper())
modal = input("Masukkan Jumlah Modal Beli Coin : Rp.".replace(".", "")) 
tanggal_beli = input("Masukkan Simulasi Tanggal Beli Coin (Format YYYY-MM-DD) : ")
tanggal_beli = input("Masukkan Simulasi Tanggal Jual Coin (Format YYYY-MM-DD) : ")
print("-"*60)

print(jenis_coin)