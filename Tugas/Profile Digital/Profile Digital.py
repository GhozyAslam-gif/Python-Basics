print("===== PROFIL DIGITAL KAMU =====")
nama = input("Masukkan Nama Lengkap : ")
umur = int(input("Masukkan Umur : "))
hitung_tahun = 2025 - umur
kelas = input("Masukkan Kelas : ")
cita_cita = input("Masukkan Cita-cita : ")
hobi = input("Masukkan Hobi : ")
belajar_it = input("Belajar paling enak pagi / malam : ")

print("" \
"")

print("=== TIPE DIGITAL ===")
print("Pilih kategori kamu:")
print("1. Wibu (Anak anime banget)")
print("2. Gamer (Ranked jalan terus)")
print("3. K-Popers (Ngikutin gaya Korea)")
print("4. Anak konten (Tiktoker/Youtuber wannabe)")
print("5. Anak nongki (Yang penting ngumpul)")

pilihan = input("Masukkan nomor pilihan kamu (1-5): ")

print(""
"")

if pilihan == '1':
    wibu = input("Siapa waifu atau husbando kamu? ")
    print("Kamu memilih Waifu!",wibu,"! Waalaah! 😅")
elif pilihan == '2':
    gamer = input("Game favorit kamu apa? ")
    print("Wih, kamu pasti jago main", gamer, "sambil ngoding. GG gaming! 🎮🔥")
elif pilihan == '3':
    kpopers = input("Siapa bias kamu? ")
    print("Kamu memilih K-Popers", kpopers, "! Pasti Seru 👍")
elif pilihan == '4':
    anak_konten = input("Platform favorit kamu? TikTok? YouTube? ")
    print("Kamu Menonton video", anak_konten ,"Pasti Video-nya bermanfaat bagimu! ")
elif pilihan == '5':
    anak_nongki = input("Nongkrong paling sering di mana? ")
    print("Waaaah", anak_nongki ,"Kamu pasti sering keluar rumah 🤔")
else:
    print("Pilihan tidak valid.")

print("" \
"")
print("=== FUN CHECK ===")
jawaban = input("Apakah Teman Di Sebelah mu Bau? (Ya/Tidak): ").strip().lower()

if jawaban == 'ya':
    print("Aduuh.... Kasih pewangi darurat, Bisa jadi masalah Dunia ini mah 😁")
elif jawaban == 'tidak':
    print("Kamu harus bersyukur, coba kalau bau 😖")
else:
    print("Jawaban tidak dikenali. Silakan jawab dengan 'Ya' atau 'Tidak'.")

print("" \
"")

print("===== PROFIL DIGITAL KAMU =====")
print(f"Nama : {nama}")
print(f"Tahun Kelahiran : {hitung_tahun}" )
print(f"Kelas : {kelas}")
print(f"Cita-cita : {cita_cita}")
print(f"Hobi : {hobi}")
print(f"Belajar paling enak pas : {belajar_it}")

print("" \
"")

print("=== TIPE DIGITAL ===")

if pilihan == '1':
    print("Tipe : Wibu")
    print("Wifu favorit :", wibu)
    print("Komentar : iihh, bau bawang niih!! 😋")
elif pilihan == '2':
    print("Tipe : Gamer")
    print("Game favorit :", gamer)
    print("Komentar : Wih, kamu pasti jago main ML sambil ngoding. GG gaming! 🎮🔥")
elif pilihan == '3':
    print("Tipe : Penggemar K-Popers")
    print("K-Popers / Stan favorit :", kpopers)
    print("Komentar : pasti kamu sudah dapat tanda tangan nya ya 😁")
elif pilihan == '4':
    print("Tipe : Anak Konten")
    print("Video / Film favorit :", anak_konten)
    print("Komentar : Pasti kamu sudah nonton spider-man No Way Home 🧐")
elif pilihan == '5':
    print("Tipe : Anak nongkrong")
    print("Tempat Nongkrong favorit :", anak_nongki)
    print("pasti kamu nongkrong sambil minum kopi ☕")

print("" \
"")

print("=== FUN CHECK ===")
print("Teman di sebelah mu bau ?", jawaban)
if jawaban == 'ya':
    print("Aduuh.... Kasih pewangi darurat, Bisa jadi masalah Dunia ini mah 😁")
elif jawaban == 'tidak':
    print("Kamu harus bersyukur, coba kalau bau 😖")
else:
    print("Jawaban tidak dikenali. Silakan jawab dengan 'Ya' atau 'Tidak'.")

print("" \
"")

print("=============SELESAI!=============")