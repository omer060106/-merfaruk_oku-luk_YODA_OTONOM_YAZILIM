mat = "yoda ders notu"
mat2 = "vize haftası geliyo"
isim = "cafer"
boy = "1.10"

print("ingilizce\nÇok zor")

print("------------------------------------------------------------")

print(mat.upper())
print(mat)

print("------------------------------------------------------------")

mat = mat.lower()
print(mat)

print("------------------------------------------------------------")

mat2 = mat2.capitalize()
print(mat2)

print("------------------------------------------------------------")

print(mat.startswith("y"))
print(mat2.endswith("yor"))

print("------------------------------------------------------------")

print(len(mat))
print(len(mat + mat2))

print("------------------------------------------------------------")

print("geçen haftalar hiç çalışmadım" * 5)

print("------------------------------------------------------------")

print ("benim adım {} boyum {}".format(isim,boy))
print (f"benim adım {isim} boyum {boy}")