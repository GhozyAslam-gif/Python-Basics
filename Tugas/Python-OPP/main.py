from prettytable import PrettyTable

data = []

def tampilkan_menu():
    print("\n=== MENU ===")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("5. Keluar")

def cari_data(id_siswa):
    for d in data:
        if d["id"] == id_siswa:
            return d
    return None

def tambah_data():
    id_siswa = input("Masukkan ID: ")

    if cari_data(id_siswa):
        print("ID sudah ada! Gunakan ID lain.")
        return

    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")

    data.append({
        "id": id_siswa,
        "nama": nama,
        "kelas": kelas
    })

    print("Data siswa berhasil ditambahkan.")

def tampilkan_data():
    if not data:
        print("Data masih kosong.")
        return

    table = PrettyTable()
    table.title = "DAFTAR SISWA"
    table.field_names = ["ID", "Nama", "Kelas"]

    for d in data:
        table.add_row([d["id"], d["nama"], d["kelas"]])

    print(table)

def ubah_data():
    id_cari = input("Masukkan ID yang ingin diubah: ")
    siswa = cari_data(id_cari)

    if not siswa:
        print("Data tidak ditemukan.")
        return

    print("Data ditemukan. Masukkan data baru:")
    siswa["nama"] = input("Nama baru: ")
    siswa["kelas"] = input("Kelas baru: ")

    print("Data berhasil diperbarui.")

def hapus_data():
    id_cari = input("Masukkan ID yang ingin dihapus: ")
    siswa = cari_data(id_cari)

    if not siswa:
        print("Data tidak ditemukan.")
        return

    data.remove(siswa)
    print("Data berhasil dihapus.")


while True:
    tampilkan_menu()
    pilihan = input("\nPilih menu (1-5): ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1-5.")
