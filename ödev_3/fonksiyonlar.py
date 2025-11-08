def fonksiyonöğreniyorum():
    print("YODA OTONOM YAZILIM ÖDEVİ3")
fonksiyonöğreniyorum()
fonksiyonöğreniyorum()
fonksiyonöğreniyorum()
fonksiyonöğreniyorum()
fonksiyonöğreniyorum()
fonksiyonöğreniyorum()
fonksiyonöğreniyorum()


print("------------------------------------------------------------")

def selam(isim):
    print("selam " + isim )

selam("ömer")


print("------------------------------------------------------------")

def topla(x,y):
    print(f"x + y = {x + y}") 

topla(8,9)

print("------------------------------------------------------------")

def ortalamaheasbı(liste):
    toplam = sum(liste)
    adet = len(liste)
    ortalama = toplam / adet
    print(f"girilen sayı ortalaması {ortalama}") 

ortalamaheasbı([1,5,6,22,5,8,1,2,6,7,8,1])

print("------------------------------------------------------------")

def büyükharf(metin):
    metin = metin.upper()
    print(metin)

büyükharf("vbsfbss")

print("------------------------------------------------------------")

def ortalamaheasbı(x,y):
    return (x + y) / 2

ortalamaheasbı(9,5)
print(ortalamaheasbı(9,8))