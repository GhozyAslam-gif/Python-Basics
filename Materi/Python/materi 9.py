print("MATERI 9 - PYTHON FUNCTION")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
# def -> fungsi lebih dari 1 baris
def halo_dek(nama):
    # f (formatting string), gunakan {} untuk variable
    print(f"Halo dek {nama}")
    print(f"Apa Kabar dek? {nama}")
# lambda -> fungsi anonim yang 1 baris saja
halo_kak = lambda nama: print(f"Halo kak {nama}")
# fungsi tidak akan berguna jika tidak di panggil
halo_dek("Nezuko")
halo_dek("Anya")
print("------------")
halo_kak("Bilal")
halo_kak("Tegar")
print("------------")
# hiher order function (map, sorted, filter)
uang_jajan = [100000,200000,10000,50000,75000]
# map() -> mentransformasi data item
kurangi_jajan =map(lambda uang: uang - 10000,
uang_jajan)
list_kurangi_jajan = list(kurangi_jajan)
print(f"Uang jajan: {uang_jajan}")
print(f"Kurangi jajan: {list_kurangi_jajan}")
print("------------")
# sorted() -> mengurutkan data
urutkan_uang = sorted(uang_jajan)
balik_uang = sorted(uang_jajan, reverse=True)
print(f"Urutkan Uang: {urutkan_uang}")
print(f"Urutkan Uang terbalik: {balik_uang}")
print("------------")
# filter() -> menyaring data sesuai kondisi
filter_uang_gede = filter(lambda uang: uang > 50000, uang_jajan)
list_uang_gede = list(filter_uang_gede)
print(f"Filter uang gede: {list_uang_gede}")

