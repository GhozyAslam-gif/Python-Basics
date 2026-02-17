class Kitab:
    def __init__(self, judul: str, kategori: str, stok: int):
        self.judul = judul
        self.kategori = kategori
        self.__stok = stok

    @property
    def stok(self) -> int:
        return self.__stok

    @stok.setter
    def stok(self, nilai_baru: int):
        if nilai_baru >= 0:
            self.__stok = nilai_baru
        else:
            print("❌ Eror: Stok tidak boleh kurang dari 0!")

    def ke_dictionary(self):
        return {
            "judul": self.judul,
            "kategori": self.kategori,
            "stok": self.__stok
        }

    def __str__(self):
        return f"[{self.kategori}] {self.judul} - Sisa: {self.__stok}"

    