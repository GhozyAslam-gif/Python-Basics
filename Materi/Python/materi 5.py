print("---MATERI 5---")
jumlahRentang = 4
# item (vatiabel baru) adalah index
# range (jumlahRentang) adalah target nya 
for item in range(jumlahRentang):
    print("Halo Bro:", item)

# huruf (variabel baru) adalah index
# kataKu adalah target nya
kataKu = "coding"
for huruf in kataKu:
    print(huruf) 

# perulangan while (samapai terpenuhi / true)
jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
  jawab = input("Ulang lagi nggak?")
  hitung += 1

print("program di ulangi sebanyak: ", hitung)

# simulasi flowchart uji sim
print("--mulai--")
tanyaUmur = input("Berapa umur mu?")
# konversi string ke integer
angkaUmur = int(tanyaUmur)
print("Umur mu :", angkaUmur, "tahun")
if (angkaUmur >= 18):
   print("Boleh memuat sim")
else:
   print("Tidak Boleh membuat sim")
print("---selesai---")