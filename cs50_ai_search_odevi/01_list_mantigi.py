veriler = []

veriler.append("A")
veriler.append("B")
veriler.append("C")

print("Liste:", veriler)

son_eleman = veriler.pop()
print("pop ile çıkan =", son_eleman)
print("Kalan liste =", veriler)

ilk_eleman = veriler.pop(0)
print("pop(0) ile çıkan =", ilk_eleman)
print("son durum =", veriler)