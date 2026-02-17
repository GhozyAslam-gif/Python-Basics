class User:
    def __init__(self, nama: str) -> None:
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama

    @nama.setter
    def nama(self, nama_baru: str) -> None:
        self._nama = nama_baru

    def __str__(self) -> str:
        return f"Nama: {self._nama}"