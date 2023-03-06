# kelas yang digunakan untuk mengimplementasikan kelas Human 
class Human:
    # konstruktor
    def __init__(self):
        self.nik = ""
        self.nama = ""
        self.jenis_kelamin = ""

    # mengeset nilai atribut NIK
    def setNIK(self, nik):
        self.nik = nik

    # mengembalikan nilai atribut NIK
    def getNIK(self):
        return self.nik

    def setNama(self, nama):
        self.nama = nama

    def getNama(self):
        return self.nama

    def setKelamin(self, jenis_kelamin):
        self.jenis_kelamin = jenis_kelamin

    def getKelamin(self):
        return self.jenis_kelamin