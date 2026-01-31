import csv

# Baca Semua Data Dari CSV

with open("keuangan.csv", newline="5", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)
print("\n")

# 1. Tampilkan semua data

print("Semua Data: ")
for row in data:
    print(f"{row['Tanggal']} | {row['Keterangan']} | {row['Jumlah']}")

# 2. Hitung total pengeluaran

total = sum(int(row['Jumlah']) for row in data)
print(f"Total Pengeluaran: Rp.{total}")
