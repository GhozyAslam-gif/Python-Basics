import requests
# pip --version (cek versi pip)
# pip install requests (install modul)
target_url = "https://api.aladhan.com/v1/timingsByCity/09-12-2025?city=Jakarta&country=Indonesia&method=20"
print(f"Target URL: {target_url}")

# HTTP GET (ambil data)
response = requests.get(target_url)
# Konversi data ke JSON
data_json = response.json()
# print(f"Response Data: {data_json}")
print("JADWAL SHOLAT")
print("=" * 20)
jadwal = data_json['data']['timings']
shubuh = jadwal['Fajr']
dzuhur = jadwal['Dhuhr']
print(f"- Shubuh: {shubuh}")
print(f"- Dzuhur: {dzuhur}")
