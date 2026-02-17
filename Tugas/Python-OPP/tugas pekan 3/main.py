from datetime import datetime
from kitab import Kitab
from santri import Santri

# Data kitab didefinisikan langsung dalam list (tanpa JSON)
daftar_kitab = [
    Kitab("Tafsir Jalalain", "Tafsir", 3),
    Kitab("Fathul Qorib", "Fiqih", 5),
    Kitab("Aqidahtuna", "Aqidah", 10),
    Kitab("Nabiyuna", "Siroh", 2)
]

# List untuk menyimpan riwayat peminjaman
riwayat_peminjaman = []

def tampilkan_daftar_kitab():
    print("\n--- 📖 DAFTAR KITAB ---\n")
    for i, k in enumerate(daftar_kitab):
        print(f"{i+1}. {k}")

def pinjam_kitab():
    nama_santri = input("Masukkan Nama Santri: ")
    peminjam = Santri(nama_santri)
    
    judul_cari = input("Masukkan Judul Kitab yang mau dipinjam: ")
    
    ketemu = False
    for k in daftar_kitab:
        if judul_cari.lower() in k.judul.lower():
            ketemu = True
            if k.stok > 0:
                k.stok -= 1
                # Mengambil tanggal saat ini
                tgl_sekarang = datetime.now().strftime("%d-%m-%Y")
                
                print(f"✅ Berhasil! {peminjam.nama} meminjam '{k.judul}' pada tanggal {tgl_sekarang}.")
                
                # Menyimpan data peminjaman ke riwayat
                riwayat_peminjaman.append({
                    "nama": peminjam.nama,
                    "judul": k.judul,
                    "tanggal": tgl_sekarang
                })
            else:
                print("❌ Maaf, stok kitab ini sedang kosong.")
            break
    
    if not ketemu:
        print("❌ Kitab tidak ditemukan di rak.")

def kembalikan_kitab():
    judul_kembali = input("Masukkan Judul Kitab yang dikembalikan: ")
    
    ketemu = False
    for k in daftar_kitab:
        if judul_kembali.lower() in k.judul.lower():
            k.stok += 1
            print(f"✅ Terima kasih! Kitab '{k.judul}' sudah dikembalikan.")
            ketemu = True
            break
    
    if not ketemu:
        print("❌ Judul kitab salah atau tidak terdaftar.")

def tampilkan_riwayat():
    print("\n--- 📜 RIWAYAT PEMINJAMAN ---")
    if not riwayat_peminjaman:
        print("Belum ada data peminjaman.")
    else:
        for r in riwayat_peminjaman:
            print(f"- [{r['tanggal']}] {r['nama']} meminjam '{r['judul']}'")

def main():
    print("\n=== 📚 APLIKASI PERPUSTAKAAN SANTRI ===")
    
    while True:
        print("\nMENU:")
        print("1. Lihat Daftar Kitab")
        print("2. Pinjam Kitab")
        print("3. Kembalikan Kitab")
        print("4. Lihat Riwayat Peminjaman")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_daftar_kitab()

        elif pilihan == "2":
            pinjam_kitab()

        elif pilihan == "3":
            kembalikan_kitab()

        elif pilihan == "4":
            tampilkan_riwayat()

        elif pilihan == "5":
            print("\n== ✨ Selamat Datang Kembali! ✨ ==\n")
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()