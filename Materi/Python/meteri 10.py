import csv

print("MATERI 10 - FILE HANDLING")
print("=========================")
# fle extention/ekstensi yg membedakan
# jenis file suatu  dan lainnya 
# .py (python), .doc (document), .txt (text file)
# cari posisi detail file yg mau dibuka
file_path = r"C:\Users\user\Documents\Python\pesan.txt"
# buka file target dengan mode tertentu
file_pesan = open(file_path, "r") # r = read only
# fungsi read() = membaca semua isi file
baca_pesan = file_pesan.read()
print(f"Isi pesannya : {baca_pesan}")
# tutup file
file_pesan.close() 

print('----- OPEN CSV -----')
csv_alamat_path = r"C:\Users\user\Documents\Python\alamat.csv"
with open(csv_alamat_path, "r", newline='') as file_alamat:
    baca_alamat = csv.reader(file_alamat)
    list_alamat = list(baca_alamat) # ubah csv objeck ke list
    print(f"Daftar alamat: {list_alamat}")

print('----- ADD ROW CSV -----')
alamat_khalid = [9, "Khalid","Sukabumi"]
print(f"Alamat baru: {alamat_khalid}")
# buka file dengan mode "a" (append/tambah)
# beserta newline/baris barunya kosong atau ""
with open(csv_alamat_path, "a", newline="") as file_alamat:
    tulis_alamat = csv.writer(file_alamat) # targetkan file
    tulis_alamat.writerow(alamat_khalid) # tamabah baris baru
    print("-----> selesai menambah baris baru ke csv")

print('----- UPDATE ROW CSV -----')
# open -> baca file -> ambil datanya, jadikan list
# olah data (edit/hapus)
# buat ulang semua baris file csv dengan mode 'w'
print('----- OPEN CSV -----')
csv_alamat_path = r"C:\Users\user\Documents\Python\alamat.csv"
# buat list kosong untuk menampung data dari csv
data_alamat = []
with open(csv_alamat_path, "r") as file_alamat:
    baca_alamat = csv.reader(file_alamat)
    print(f"Daftar alamat: {list_alamat}t")
    for item_alamat in baca_alamat:
        data_alamat.append(item_alamat)

# ekstrak list data alamat dengan for loop
for item in data_alamat:
    # cek kolom nama (index 1)
    if item[1] == 'Surya':
        print("Data surya telah ditemukan, ganti alamatnya...")
        item[2] = "Bandung" # index 2 (kolom alamat)
    else:
        print("Skip... bukan data surya!!")

# ubah data dari csv berdasarkan index
del data_alamat[4]
# ubah data alamat (index2)
print(f"List data alamat: {data_alamat}")

# buka file dengan 'w' (write) -> menulis ulang semua
# beserta newline/baris baru nya kosong atau ""
with open(csv_alamat_path, "w", newline="") as file_alamat:
    tulis_alamat = csv.writer(file_alamat) # targetkan file
    tulis_alamat.writerows(data_alamat) # tambah baris baru
    print("--> selesai membuat ulang data csv")
