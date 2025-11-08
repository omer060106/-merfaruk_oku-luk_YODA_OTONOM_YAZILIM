kisi = {"isim" : "ömer" , "yas" : 2 , "cinsşyet" : "erkek" , "hobiler" : ["YODA" , "OTONOM", "YAZILIM"]  }

print(kisi["isim"])
print(kisi["hobiler"])

print("------------------------------------------------------------")

print(kisi)

kisi["isim"] = "faruk"
print(kisi)

print("------------------------------------------------------------")

kisi.update({"isim" : "alparslan", "yas" : 19})
print(kisi)

print("------------------------------------------------------------")

kisi["soyisim"] = "okuşluk"
print(kisi["soyisim"])

print("------------------------------------------------------------")

del kisi["soyisim"]
print(kisi)

for i in kisi :
    print(kisi[i]) 

for i in kisi :
    print(i) 

print("------------------------------------------------------------")

print(kisi.keys())

print("------------------------------------------------------------")

print(kisi.values())

print("------------------------------------------------------------")

print(kisi.items())

print("------------------------------------------------------------")

for i,x in kisi.items():
    print(i,x)

print(kisi.get("soyisim","bulunamadı"))