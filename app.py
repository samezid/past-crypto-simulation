from colorama import Fore, Style
import pyfiglet
import coin_rate
from exchange_rate import usdidr


# welcome Massage
banner = pyfiglet.figlet_format("WELCOME TO")

print(" ")
print(" ")
print(Fore.GREEN + "="*60 + Style.RESET_ALL)
print(Fore.GREEN + "="*60 + Style.RESET_ALL)
print(" ")
print(Fore.YELLOW + banner.rstrip() + Style.RESET_ALL)
print(" ")
print(Fore.YELLOW + "-------------Past Crypto Profit/Loss Simulator-------------"  + Style.RESET_ALL)
print(" ")
print(Fore.GREEN + "="*60 + Style.RESET_ALL)
print(Fore.GREEN + "created by Fachrizal Ainurrahman|Github : github.com/samezid" + Style.RESET_ALL)
print(Fore.GREEN + "="*60 + Style.RESET_ALL)
print(" ")
print(" ")

# input user
print("-"*60)

while True:
    try:
        jenis_coin = input("Masukkan Jenis Coin : ")
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
def format_indo(angka):
    # hasil = angka * usdidr
    return "{:,.0f}".format(angka).replace(",", "X").replace(".", ",").replace("X", ".")

harga_beli = coin_rate.get_coin_rate(jenis_coin, tanggal_beli) #sudah benar
jumlah_coin = modal/ harga_beli #sudah benar
harga_jual = coin_rate.get_coin_rate(jenis_coin, tanggal_jual) #sudah benar
gain = jumlah_coin * harga_jual #sudah benar
laba = gain - modal



# output
print(f"Harga {jenis_coin} saat beli : Rp.{format_indo(harga_beli)}")
print(f"harga {jenis_coin} saat jual : Rp.{format_indo(harga_jual)}")
print(" ")
print(f"Jumlah {jenis_coin} yang didapat sebanyak : {jumlah_coin:,.6f} BTC")
print(" ")
print(f"pendapatan yang diperoleh : Rp.{format_indo(gain)}")
print(f"keuntungan bersih : Rp.{format_indo(laba)}")
print("-"*60)
