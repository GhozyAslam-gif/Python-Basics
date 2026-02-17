from user import User

class Santri(User):
    def __init__(self, nama: str):
        super().__init__(nama)
        self.peran = "Santri"

    def __str__(self):
        return f"Nama: {self.nama}, Peran: {self.peran}"