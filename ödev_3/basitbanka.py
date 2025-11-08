class hesap: 
# hesap adında bir sınıf oluşturuyoruz

    def __init__(self, hesap_sahibi, hesap_no, bakiye=0):
        self.hesap_sahibi = hesap_sahibi
        self.hesap_no = hesap_no
        self.bakiye = bakiye
 #self o nesnenin kendisini temsil eder
 #self.sahip ile bu nesneye ait bir özellik oluşturuyorum
 #başlangıç bakiyesini tanımlıyorum varsayılan olarak 0 TL yapıyorum
    def parayat(self, miktar):
# Kullanıcı negatif ya da sıfır miktar girmesin diye kontrol ekliyorum
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL yatırıldı mevcut bakiye= {self.bakiye}TL")
        else:
            print("işlem geçersizdir")

    def paracek(self,miktar):
#kullanıcı negatif ya da sıfır miktar girmesin diye kontrol ediyorum
        if miktar <= 0 :
            print("işem geçrsizdir")
        elif miktar > self.bakiye :
            print("yetersiz bakiye")
#kullanıcı yeterli çekebilecek bakiyesi var mı diye kontrol ediyorum
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi yeni bakiye = {self.bakiye}TL")
#son durum bakiye görüntüsü alıyorum
    def  bakiyegörüntü(self):
        print(f"güncel bakiyeniz: {self.bakiye} TL")       
# kullanıcıdan bilgi alıyorum ve bu sayede bu bilgiler sınıflara parametre olarak gönderiliyor
hesap_sahibi = input("hesap sahibinn adı = ")
hesap_no = input("hesap numarınızı giriniz = ")
bakiye = float(input("hesap başlangıç bakiyenizi giriniz"))

#yukarıdan alınan bilgilerle hesap nesnesi oluşturdum
hesap = hesap(hesap_sahibi,hesap_no,bakiye)

# burda sonsuz döngüyle birlikte hesapişlemleri yapılmaktadır
while True:

    print("--- İŞLEM MENÜSÜ ---")
    print("1 - para Yatır")
    print("2 - para Çek")
    print("3 - bakiye Görüntüle")
    print("4 - çıkış")

    secim = input("bir işlem numarası seçin =")

    if secim == "1":
        miktar = float(input("yatırılacak miktar: "))
        hesap.parayat(miktar)
    elif secim == "2":
        miktar = float(input("çekilecek miktar: "))
        hesap.paracek(miktar)
    elif secim == "3":
        hesap.bakiyegörüntü()    
    elif secim == "4":
        print("çıkış yapılıyor gene beklerim")
        break
    else:
        print("geçersiz eleman yeniden giriniz")