

while True:
    c = input("bir işlem seçiniz örneğin * / + - =  ")
    a = int(input("birinci sayıyı giriniz =  "))
    b = int(input("ikinci sayıyı giriniz =  "))

    if c == "+":
      sonuc = a + b
      print(f"{a} + {b} = {sonuc}")
    elif c == "-":
       sonuc = a - b
       print(f"{a} - {b} = {sonuc}")
    elif c == "*":
       sonuc = a * b
       print(f"{a} * {b} = {sonuc}")
    elif c == "/":
       if b == 0:
          print("işlem geçersizdir ")
       else:
          sonuc = a / b
          print(f"{a} / {b} = {sonuc}")
    k = input("işlemlere devam etmek istiyor musnuz evet için evet hayır için hayır yazınız")
    if k == "hayır":
       print("iyi günler")
       break
    elif k == "evet":
       print("yeni sayılarınızı hazırlayınız")