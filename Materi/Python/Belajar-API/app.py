import requests

# Tangal = 28-08-2025
tanggal = input("Masukkan tanggal: ")
kota = input("Masukkan kota: ")
url = "https://api.aladhan.com/v1/timingsByCity/{tanggal}?city={kota}&country=Indonesia&method=5"
print(f"Target URL: {url}")
response = requests.get(url)  # HTTP GET
data_json = response.json()   # Konversi ke JSON
jadwal_sholat = data_json['data']['timings']
tgl_hijri = data_json['data']['date']['hijri']['date']
print(f"Tgl Hijriah: {tgl_hijri}")
print("Jadwal Sholat:")
print(f"-> Shubuh: {jadwal_sholat['Fajr']}")
print(f"-> Maghrib: {jadwal_sholat['Maghrib']}")
