liste = [1,2,3,4,5,6]
isim = "ömer"

for i in liste:
    print(i)

print("------------------------------------------------------------")

for i in isim:
    print(i)

print("------------------------------------------------------------")

for i in range(1,6):
    print(i)
    
print("------------------------------------------------------------")

for i in range(0,19,3):
    print(i)

print("------------------------------------------------------------")
sonuc = 1
for i in range(0,10):
    sonuc = sonuc * 2

print(sonuc)

print("------------------------------------------------------------")

liste1 = ["a", "b", "c"]

for i in liste1:
    for x in liste:
        print(i,x)
print("------------------------------------------------------------")

for i in liste:
    if i == 4:
        continue
    print(i)


print("------------------------------------------------------------")

for i in liste:
    if i == 4:
        break
    print(i)

print("------------------------------------------------------------")

liste2 = range(103)

for i in liste2:
    if i %3 != 0:
        continue
    if i == 66:
        break
    print(i)


print("------------------------------------------------------------")

x = 2

while x < 10:
    print(x)
    x = x + 2
print(x)


print("------------------------------------------------------------")

x = 2
while True:
    print(x)
    x = x + 5
    if x > 1000:
        print("sayıya ulaştın")
        break