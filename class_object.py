# Class dan Object
class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        return f"Halo, saya {self.nama} dari kelas {self.kelas}"


siswa = Siswa("Carnesih", "X")
print(siswa.perkenalan())
