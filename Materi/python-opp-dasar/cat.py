# diawali class NamaClass
class Cat:
    # self = dirinya sendiri / internal class
    # __init__ = constructor = fungsi yang pertama kali di panggil
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    
    # method = fungsi di dalam class
    def sleep(self,duration):
        print(f"turu {duration} menit")
# buat objek dari class Cat
belang = Cat("mix", 5)
oyen = Cat("orange", 3)
print("obj belang", belang)
print("obj oyen", oyen)
# print ("obj belang:", belang)
# print ("obj oyen:", oyen)
belang.sleep(10)
oyen.sleep(5)
print(f"belang warna {belang.color}")
print(f"belang berat {belang.weight}")
print(f"oyen warna {oyen.color}")
print(f"oyen berat {oyen.weight}")