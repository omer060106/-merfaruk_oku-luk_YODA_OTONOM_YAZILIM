demet = ("ömer", "faruk", "okuşluk", "YODA", "OTONOM", "YAZILIM")
print(type(demet))

print("------------------------------------------------------------")

print(len(demet))

print("------------------------------------------------------------")

print(demet)

print("------------------------------------------------------------")

küme = {"sarı", "kırmızı", "siyah", "yeşil"}
print(type(küme))

print("------------------------------------------------------------")

print(len(küme))

print("------------------------------------------------------------")

print(küme)

print("------------------------------------------------------------")

küme.add("pembe")
print(küme)

print("------------------------------------------------------------")

küme.remove("yeşil")
print(küme)

print("------------------------------------------------------------")

küme.discard("gri")


küme1 = ("kırmızı", "siyah", "turkuaz", "kahverengi")


print(küme.intersection(küme1))

print("------------------------------------------------------------")

print(küme.union(küme1))

print("------------------------------------------------------------")

print(küme.difference(küme1))

print("------------------------------------------------------------")

print("sarı" in küme)
print("gri" in küme.union(küme1))

print("------------------------------------------------------------")

kümeayirmayapisi = set("OKUŞLUK")
print(kümeayirmayapisi)
