a = 9
b =  5
c = 12
if  a == b:
    print("a=b")

print("------------------------------------------------------------")

if a < b:
    print("a<b")

print("------------------------------------------------------------")

if a > b:
    print("a>b")

print("------------------------------------------------------------")

if  a != b:
    print("a b ye eşit değil")

print("------------------------------------------------------------")


if  a == b:
    print("a=b")
else:
    print("bu ikisayı arasında bir eşitlik yoktur")

print("------------------------------------------------------------")

renk = "siyah"

if renk == "beyaz":
    print("beyaz")
elif renk == "sarı":
    print("sarı")
elif renk == "kirmizi":
    print("kırmızı")
else:
    print("hiçbiri")

print("------------------------------------------------------------")

if a < b or c > a:
    print("koşul doğru")
else:
        print("koşul yanlış")

print("------------------------------------------------------------")


liste = [1,2,3,4,5,6,7,8]
a = 6
b = 9

if a in liste:
    print("listede var")
else:
    print("listede yok")

print("------------------------------------------------------------")

if not b in liste:
    print("listede yok")
else:
    print("listede var")

print("------------------------------------------------------------")


x = "YODA"
y = "YOD"
y = y + "A"

print(x)
print(y)

print("------------------------------------------------------------")

if x == y:
    print("koşul doğru")
else:
    print("koşul doğru değil")

print("------------------------------------------------------------")

if x is y:
    print("koşul doğru")
else:
    print("koşul doğru değil")
    print(id(x))
    print(id(y))
