print("Materi 6C - Python Data ")
print("-----------------------")
# List 
daftar_belanja = [
    "pisang kembung", # index 0
    "gabin", # index 1
    "es teh desa", # index 2
    ]
print("Tas Belanja :", daftar_belanja)
# akses item dengan index
print(daftar_belanja[1])
# append() untuk menambah item ke akhir list
daftar_belanja.append("tahu golek")
# insert() untuk menambah item ke index tertentu
daftar_belanja.insert(1, "batagor")
# remove() untuk menghapus item
daftar_belanja.remove("es teh desa")
daftar_belanja.append("siomay")
daftar_belanja.insert(3, "cilok")
print("Tas belanja Skrg:", daftar_belanja)
jajanan_bilal = ["olive chicken", "batagor", "gorengan"]
jajanan_ishaq = ["naspad kawan lamo", "indomie", "roma kelapa"]
for item in daftar_belanja:
    print(item)
titip_belanjaan = jajanan_bilal + jajanan_ishaq
print("Titipan belanja :", titip_belanjaan)
# menggandakan item list dengan *
print("Bilal nambah:", jajanan_bilal * 3)

daftar_menu = [
    ["Kopi", "Teh", "Susu Jahe"], # baris 0
    ["Jus Apel", "Jus Jeruk", "Jus Alpukat", "Jus Mangga"], # baris 1
    ["Es Teler", "Es Dawet"] # baris 2
]

print("DAFTAR MENU : ",daftar_menu)
print(daftar_menu[1][2])

print("-----------------------------")
# Tuple -> ( ) -> berurutan, tidak berubah, boleh duplikat
ttl = ("Purworejo", 21, "Januari", 2009)
print("TTL:", ttl)
print("Bulan lahir ujang:", ttl[2])
# unpacking varable (mengekstrak tuple ke variable baru)
tempat_lahir, tgl_lahir, bln_lahir, thn_lahir = ttl
print("Thn lahir: ", thn_lahir)