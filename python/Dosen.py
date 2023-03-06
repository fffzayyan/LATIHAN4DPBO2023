from SivitasAkademik import SivitasAkademik

class Dosen(SivitasAkademik):
    def __init__(self):
        self.nip = ""
        self.pend_terakhir = ""
        self.keahlian = ""

    def setNIP(self, nip):
        self.nip = nip

    def getNIP(self):
        return self.nip

    def setPend(self, pend_terakhir):
        self.pend_terakhir = pend_terakhir

    def getPend(self):
        return self.pend_terakhir

    def setAhli(self, keahlian):
        self.keahlian = keahlian

    def getAhli(self):
        return self.keahlian