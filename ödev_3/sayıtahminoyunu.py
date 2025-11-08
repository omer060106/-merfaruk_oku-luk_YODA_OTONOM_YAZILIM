import random
# bunu araştırıp öğrendim bu modul benim içinde yeni anladığım kadarıyla random komutunu kullanmak için gerkli bir modül
kume = set(range(1,101))
# 1den 100e kadar sayı kümesi
randomsayı = random.choice(list(kume))
# bir random sayı seçildi 
print("1 ile 100 arasından 1 ve 100 dahil bir sayı seçildi bunu bulmaya çalışınız")

while True:
    tahmin = int(input("tahmininizi giriniz = "))
    #bir sonsuz döngü açarak tahmin alıyoruz
   
    uzaklıkayarı = tahmin - randomsayı
    x = uzaklıkayarı
    uzaklıkayarı = abs(uzaklıkayarı)
#burada bu değişkenleri verme nedenim  uzaklık ayarı ile sayının uzaklığını bularak sıcaklık soğukluk ayarı yapıyorum bunun için mutlak değer alıyorum aynı zamanda mutlak değeri alınmadan önceki değeri de elimde tutuyorum ki sayıyı artırıp veya azaltacağımı kontrol etmek istedim
    if uzaklıkayarı <= 15 and x < 0 :
        print("çok sıcak ve daha büyük bir sayı deneyiniz") 
    elif uzaklıkayarı <= 15 and x > 0 :
        print("çok sıcak ve daha küçük bir sayı deneyiniz") 
    elif uzaklıkayarı <= 25 and x < 0  :
        print("sıcak ve daha büyük bir sayı deneyiniz")
    elif uzaklıkayarı <= 25 and x > 0  :
        print("sıcak ve daha küçük bir sayı deneyiniz")
    elif uzaklıkayarı >= 60 and x < 0 :
        print("çok soğuk ve daha büyük sayı deneyiniz")
    elif uzaklıkayarı >= 60 and x > 0 :
        print("çok soğuk ve daha küçük sayı deneyiniz")
    elif uzaklıkayarı > 25 and x < 0 :
        print("soğuk ve daha büyük sayı deneyiniz")
    elif uzaklıkayarı > 25 and x > 0 :
        print("soğuk ve daha küçük sayı deneyiniz")
    elif x == 0:
        print(f"tebrikler doğru tahmin = {randomsayı}")
        break
#burda da elif ve if komutlarını kullanrak ve and fonksiyonunu kullnarak hem uzaklık derecesini hemde artırılıp veya azaltılacağını söylüyorum
#istediğin sadece artırıp azaltamamızdı ama kendimi denemek istedim