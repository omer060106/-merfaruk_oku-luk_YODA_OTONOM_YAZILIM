renkler = ["siyah", "beyaz", "mavi", "pembe", "yeşil"]

print (type(renkler))

print("------------------------------------------------------------")

print(len(renkler))

print("------------------------------------------------------------")

print(renkler)

print("------------------------------------------------------------")

print(renkler[2])
print(renkler[2:])
print(renkler[2:4])
print(renkler[::2])

print("------------------------------------------------------------")

renkler.append("sarı")
print(renkler)

print("------------------------------------------------------------")

renkler.insert(1,"kırmızı")
print(renkler)

print("------------------------------------------------------------")

renkler.remove("pembe")
print(renkler)

print("------------------------------------------------------------")

renkler2 = ["turuncu", "pembe", "lila"]
renkler.extend(renkler2)
print(renkler)

print("------------------------------------------------------------")

silinen = renkler.pop(6)
print(renkler)
print(silinen)
print(renkler.pop(7))

print("------------------------------------------------------------")

renkler.reverse()
print(renkler)

print("------------------------------------------------------------")

renkler.reverse()
print(renkler)

print("------------------------------------------------------------")

renkler.sort()
print(renkler)

print("------------------------------------------------------------")

renkler.sort(reverse=True )
print(renkler)

print("------------------------------------------------------------")

renk3 = ["siyah", "beyaz", "mavi", "pembe", "yeşil"]
list2 = sorted(renk3)
print(renk3)
print(list2)

print("------------------------------------------------------------")

sayilar = [1,3,9,21,4,96,42,11,22,8,9,32]
print(max(sayilar))
print(max(renkler))
print(min(sayilar))
print(min(renkler))

print("------------------------------------------------------------")

print(sum(sayilar))

print("------------------------------------------------------------")

print(list(enumerate(renkler,start=100)))

print("------------------------------------------------------------")

print("kırmızı" in renkler)
print("turkuaz" in renkler)

print("------------------------------------------------------------")

birleştirme = "-".join(renkler)
print(birleştirme)
print(type(birleştirme))


