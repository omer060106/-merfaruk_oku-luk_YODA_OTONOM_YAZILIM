class Kutu:
    def __init__(self):
        self.esyalar = []

    def ekle(self, esya):
        self.esyalar.append(esya)

    def goster(self):
        print("eşyalar", self.esyalar)


kutu1 = Kutu()
kutu1.ekle("kalem")
kutu1.ekle("defter")
kutu1.goster()