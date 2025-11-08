class Ucus():
    havayolu = "THY"
    
    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu
ucus1 = Ucus('TK124','IST','ANKARA', 60, 300, 50)        
print(ucus1.varis)
print(ucus1.havayolu)

ucus2 = Ucus('TK184','BOD','ANTEP', 50, 250, 70) 
print(ucus2.varis)

def anons(self):
    return "{} sefer sayılı {}-{} ucusumuz {} dakika sürecektir".format(
    self.kod,
    self.kalkis,
    self.varis, 
    self.sure)                                                                             
ucus2.anons()
print(ucus2.anons())


