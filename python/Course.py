class Course:
    def __init__(self):
        self.nama_matakuliah = ""
        self.kode_matakuliah = ""

    def setMatkul(self, nama_matakuliah):
        self.nama_matakuliah = nama_matakuliah

    def getMatkul(self):
        return self.nama_matakuliah

    def setKodeM(self, kode_matakuliah):
        self.kode_matakuliah = kode_matakuliah

    def getKodeM(self):
        return self.kode_matakuliah