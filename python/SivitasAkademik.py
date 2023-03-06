from Human import Human

class SivitasAkademik(Human):
    def __init__(self):
        self.asal_universitas = ""
        self.email_edu = ""
        self.fakultas = ""

    def setUniv(self, asal_universitas):
        self.asal_universitas = asal_universitas

    def getUniv(self):
        return self.asal_universitas

    def setEmail(self, email_edu):
        self.email_edu = email_edu

    def getEmail(self):
        return self.email_edu

    def setFakultas(self, fakultas):
        self.fakultas = fakultas

    def getFakultas(self):
        return self.fakultas

    # def getProdi(self):
    #     return self.fakultas.getNamaProdi()
