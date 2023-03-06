from SivitasAkademik import SivitasAkademik

class Mahasiswa(SivitasAkademik):
    def __init__(self):
        self.nim = ""

    def setNIM(self, nim):
        self.nim = nim

    def getNIM(self):
        return self.nim