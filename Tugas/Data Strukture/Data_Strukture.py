print("Bismillah...")
jadwal_Adzan = [
    "Abdullaoh",
    "Bilal",
    "Dihyah",
]
print("Jadwal Adzan Hari ini :", jadwal_Adzan)
print("Jadwal Adzan Hari ini :")

for item in jadwal_Adzan :
    print("-",item)
print("" \
"")
print("Rukun Iman :")

rukun_iman = (
    "Iman kepada Allah",
    "Iman kepada Malaikat-malaikat-Nya",
    "Iman kepada Kitab-kitab-Nya",
    "Iman kepada Nabi dan Rasul-Nya",
    "Iman kepada Hari Qiamat",
    "Iman kepada Takdir baik maupun buruk",
)
for index in range(len(rukun_iman)) :
    print(f"{index + 1}. {rukun_iman[index]}")

print("" \
"")

print("Kitab-kitab yang Di pelajari :")
kitab_dipelajari = {"Kitab Tauhid", "Kitab Tafsir", "Kitab Fiqih"}

for item in kitab_dipelajari :
    print("-", item)

print("" \
"")

biodata = {'Nama ': 'Utsman', 'kelas': 'X-C', 'Hafalan_Juz': '10'}

for key, value in biodata.items():
    print(f"{key} : {value}")

