import pandas as pd

def ambil_harga_tanggal(csv_path, tanggal_str):
    df = pd.read_csv(csv_path)

    # Parsing tanggal dengan waktu
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')
    tanggal_input = pd.to_datetime(tanggal_str, format='%Y-%m-%d')

    # Bandingkan hanya tanggal (tanpa jam)
    baris = df[df['Date'].dt.date == tanggal_input.date()]

    if baris.empty:
        print("Tanggal tidak ditemukan di data.")
        return None

    return baris.iloc[0]['Close']

# Contoh pemanggilan
harga = ambil_harga_tanggal("data/coin_Bitcoin.csv", "2021-01-01")
if harga:
    print(f"Harga pada 2021-01-01: ${harga:,.2f}")