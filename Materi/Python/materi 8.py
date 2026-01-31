print("MATERI 8C - FUNCTION BASIC")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
# buat fungsi dengan 'def' lalu nama fungsi nya
def halo_dunia(nama):
    print("Selamat Datang !")
    print("Hello Mr.", nama)
    print("---------------->")
# panggil nama fungsi disertai ( )
halo_dunia("Utsman")
halo_dunia("Ridho")
halo_dunia("Bilal")
halo_dunia("Imam")

# fungsi luas persegi panjang 
def luas_persegi_panjang(panjang, lebar):
    print("P =", panjang)
    print("L =", lebar)
    rumus = panjang * lebar
    print("Hasil luas persegi panjang = ", rumus)

luas_persegi_panjang(10, 5)
luas_persegi_panjang(8, 100)
# def luas_segitiga(alas, tinggi):
 # 1/2 * alas * tinggi

def luas_segitiga(alas, tinggi):
    print("A =", alas)
    print("T =", tinggi)
    rumus = alas * tinggi
    print("Hasil alas segitiga = ", rumus)

luas_segitiga(1/2, 5)
luas_segitiga(10, 50)

def luas_jajar_genjang(alas, tinggi):
    print("Alas =", alas)
    print("Tinggi =", tinggi)
    rumus = alas * tinggi
    print("Hasil luas jajar genjang =", rumus)

luas_jajar_genjang(10, 5)
luas_jajar_genjang(10, 60)
