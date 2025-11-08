**STRİNGLER**

Stringler metin verilerini temsil etmek için kullanılan bir veri türüdür sıralıdır yani her karakterin belirli bir sırası vardır değiştirilemez yani bir string oluşturulduktan sonra içindeki karakterler sonradan değiştirilemez

### 1\. Harf Büyüklüğü / Küçüklüğü Metotları

* upper() (String deki tüm harfleri büyük harfe çevirir)  
* lower() (String deki tüm harfleri küçük harfe çevirir)  
* capitalize() (Stringin sadece ilk harfini büyük, geri kalanını küçük yapar)  
* title() (String deki her kelimenin ilk harfini büyük, geri kalanını küçük yapar)  
* swapcase() (Büyük harfleri küçük, küçük harfleri büyük yapar)  
* casefold() (lower() gibidir ancak uluslararası karakterler için daha güçlü bir küçük harfe çevirme yapar)  
   

  ### 2\. Kontrol Metotları (True/False Döndürenler)

* startswith() (Belirtilen metinle başlıyor mu?)  
* endswith() (Belirtilen metinle bitiyor mu?)  
* isupper() (Tüm harfler büyük mü?)  
* islower() (Tüm harfler küçük mü?)  
* istitle() (String, title() formatına uygun mu?)  
* isalpha() (Tüm karakterler alfabe harfi mi?)  
* isdigit() (Tüm karakterler rakam mı?)  
* isdecimal() (isdigit() gibidir ancak sadece onluk tabandaki rakamları kabul eder)  
* isnumeric() (Rakamları, kesirleri, üst simgeleri vb. de içeren geniş bir sayı kontrolü yapar)  
* isalnum() (Tüm karakterler harf veya rakam mı?)  
* isspace() (Tüm karakterler boşluk karakteri mi? )  
* isprintable() (String Deki tüm karakterler basılabilir karakterler mi?)  
* isidentifier() (String  geçerli bir Python değişken/fonksiyon adı mı?)

  ### 3\. Bulma, Sayma ve Değiştirme Metotları

* find() (Arananı bulur, ilk indeksi verir, bulamazsa \-1 döndürür)  
* rfind() (Aramayı sağdan  başlayarak yapar, bulamazsa \-1 döndürür)  
* index() (Arananı bulur, ilk indeksi verir, bulamazsa hata verir)  
* rindex() (Aramayı sağdan yapar, bulamazsa hata verir)  
* count() (Bir karakterin/metnin string içinde kaç kez geçtiğini sayar)  
* replace() (Metnin bir bölümünü, başka bir metinle değiştirir)

  ### 4\. Bölme ve Birleştirme Metotları

* split() (Stringi belirtilen ayıraca göre böler, liste yapar)  
* rsplit() (split gibidir ancak bölmeye sağdan başlar)  
* splitlines() (Stringi satır satır böler, liste yapar)  
* partition() (Stringi belirtilen ayıraca göre 3 parçalık bir tuple yapar: ayraçtan öncesi, ayraç, ayraçtan sonrası)  
* rpartition() (partition gibidir ancak aramaya sağdan başlar)  
* join() (Bir string listesini, araya bu stringi koyarak tek bir stringe birleştirir)

  ### 5\. Hizalama ve Temizleme Metotları

* strip() (Baştaki ve sondaki boşlukları (veya belirtilen karakterleri) siler)  
* rstrip() (Sadece sağdaki (sondaki) boşlukları siler)  
* lstrip() (Sadece soldaki (baştaki) boşlukları siler)  
* center() (Stringi belirtilen genişliğe göre ortalar)  
* ljust() (String'i sola yaslar)  
* rjust() (Stringi sağa yaslar)  
* zfill() (Belirtilen genişliğe ulaşana kadar stringin soluna sıfır ekler)  
* format() (String'i formatlamak, içine değer yerleştirmek için kullanılır

**İNTEGER**

Ondalık kısmı olmayan sayılardır pozitif, negatif veya sıfır olabilirler matematikteki tam sayılar kümesine karşılık gelirler.

Float  
Ondalık kısmı olan sayılardır. Matematikteki  reel sayılar  kümesini temsil ederler.

*   
* abs() (Bir sayının mutlak değerini, yani pozitif halini döndürür)  
* round() (Bir ondalıklı sayıyı en yakın tam sayıya yuvarlar)  
* pow() (Bir sayının kuvvetini (üssünü) alır  
* type() (Verinin tipini söyler)  
* float() (Başka bir tipi ondalıklı sayıya çevirir)


  
**LIST**

Verileri sıralı bir şekilde bir arada tutan bir koleksiyondur en önemli özelliği değiştirilebilir olmasıdır elemanları sonradan eklenebilir, silinebilir veya güncellenebilir.

* append() (Listenin sonuna eleman ekler)  
* insert() (Belirli bir konuma  eleman ekler)  
* remove() (Değeri bilinen ilk elemanı listeden siler)  
* extend() (Listeyi, başka bir liste ile genişletir)  
* pop() (Belirli bir konumdaki elemanı siler ve onu döndürür)  
* reverse() (Listenin sırasını kalıcı olarak ters çevirir)  
* sort() (Listeyi kalıcı olarak sıralar)  
* sorted() (Listeyi sıralar ancak orjinali bozmaz, yeni liste verir)  
* max() (Bir koleksiyondaki en büyük elemanı bulur)  
* min() (Bir koleksiyondaki en küçük elemanı bulur)  
* sum() (Sayı listesindeki elemanları toplar)  
* list() (Başka bir veri tipini listeye çevirir)  
* enumerate() (Bir koleksiyonu numaralandırır (indeks, eleman çifti verir))  
* join() (Bir string listesini, tek bir string e birleştirir)  
* split() (Bir stringi bölerek string listesi yapar)


### **Tuple** 

Verileri sıralı bir şekilde bir arada tutan bir koleksiyondur en önemli özelliği değiştirilemez olmasıdır oluşturulduktan sonra elemanları asla değiştirilemez veya silinemez.

* count() (Bir elemanın tuple içinde kaç kez geçtiğini sayar)  
* index() (Bir elemanın tuple içindeki ilk konumunu  bulur)  
* max() (Bir koleksiyondaki en büyük elemanı bulur)  
* min() (Bir koleksiyondaki en küçük elemanı bulur)  
* sum() (Sayı tuple'ındaki elemanları toplar)  
* tuple() (Başka bir veri tipini tuple'a çevirir)  
* sorted() (Tuple ı sıralar ancak orijinali bozmaz, yeni bir liste verir)

---

### **Set** 

Verileri sırasız bir şekilde tutan ve tekrarsız elemanlardan oluşan bir koleksiyondur elemanları eklenebilir ve silinebilir ancak sıralı olmadıkları için konumları yoktur.

* add() (Set'e tek bir eleman ekler, eğer zaten varsa bir şey yapmaz)  
* update() (Set i başka bir koleksiyonun elemanlarıyla günceller)  
* remove() (Değeri bilinen elemanı siler bulamazsa hata verir)  
* discard() (Değeri bilinen elemanı siler bulamazsa hata vermez)  
* pop() (Setten rastgele bir elemanı siler ve onu döndürür)  
* clear() (Set in tüm elemanlarını siler)  
* union() (İki kümenin birleşimini yeni bir set olarak verir)  
* intersection() (İki kümenin kesişimini verir)  
* difference() (İki kümenin farkını verir)  
* issubset() (Bir küme, diğerinin alt kümesi mi?)  
* issuperset() (Bir küme, diğerini kapsıyor mu?)  
* max() (Bir koleksiyondaki en büyük elemanı bulur)  
* min() (Bir koleksiyondaki en küçük elemanı bulur)  
* sum() (Sayı setindeki elemanları toplar)  
* set() (Başka bir veri tipini sete çevirir, tekrarları siler)

### **Dictionaries** 

Verileri anahtar:değer  çiftleri olarak saklayan fonksiyondur. En önemli özelliği değiştirilebilir olması ve anahtarların benzersiz olmasıdır. 

* len() (Sözlükteki anahtar:değer çifti sayısını verir)  
* dict() (Başka bir veri tipini (genellikle çiftleri) sözlüğe çevirir)  
* max() (Sözlükteki en büyük anahtarı (key) bulur)  
* min() (Sözlükteki en küçük anahtarı (key) bulur)  
* sum() (Anahtarlar numerik ise toplamlarını verir)  
* sorted() (Sözlüğün anahtarlarını sıralı bir liste olarak verir)  
* get() (Anahtarla değer arar bulamazsa hata vermez none veya varsayılan değeri döndürür)  
* keys() (Tüm anahtarları verir)  
* values() (Tüm değerleri verir)  
* items() (Tüm anahtar \= değer çiftlerini verir)  
* pop() (Belirtilen anahtarı ve değerini siler silinen değeri döndürür)  
* popitem() (Son eklenen anahtar \= değer çiftini siler ve döndürür)  
* update() (Sözlüğü başka bir sözlük/koleksiyon ile günceller veya eleman ekler)  
* clear() (Sözlüğün tüm içeriğini siler)  
* copy() (Sözlüğün sığ bir kopyasını oluşturur)  
* setdefault() (Anahtar varsa değerini verir, yoksa anahtarı varsayılan değerle ekler)

**IF-ELIF-ELSE**

Pythonda koşullu durumları veya karar yapılarını oluşturmak için kullanılır programın akışını belirli bir koşulun `True` (Doğru) veya `False` (Yanlış) olmasına göre yönlendirirler.

* `if` (Koşul bloğunu başlatan ana anahtar kelimedir. Belirtilen koşul `True` ise `if` bloğu çalışır `False` ise atlanır)  
* `elif` (Açılımı "else if"tir Önceki `if` veya `elif` koşulu `False` ise yeni bir koşulu kontrol etmek için kullanılır isteğe bağlıdır)  
* `else` (Yukarıdaki `if` ve `elif` koşullarından hiçbiri `True` olmadığında çalışacak olan son bloktur isteğe bağlıdır)

**WHILE VE FOR**

Python da döngü  yani tekrar eden işlemler oluşturmak için kullanılan iki temel yapıdır.

* for \= Bir koleksiyon veya aralıktaki  her bir eleman üzerinde sırayla gezinerek  içindeki kod bloğunu çalıştıran döngü yapısıdır  
* while \= Belirli bir koşul Doğru olduğu sürece içindeki kod bloğunu tekrar tekrar çalıştıran döngü yapısıdır. Koşul Yanlış olduğunda döngü durur

**FONKSİYONLAR**

Fonksiyonlar belirli bir işi yapmak için yazılan ismi olan ve programın farklı yerlerinde tekrar kullanılabilen kod parçalarıdır Programı bölümlere ayırarak hem okunmasını hem de yönetilmesini kolaylaştırırlar Fonksiyonlar dışarıdan parametre alabilir ve işlemlerini tamamladıktan sonra return ifadesiyle bir değer geri döndürebilirler.

**CLASS** 

 Pythonda Nesne Yönelimli Programlamanın (OOP) temel taşıdır belirli özelliklere (attributes) ve davranışlara (methods) sahip olacak nesneler (objects) oluşturmak için kullanılan bir plan, kalıp veya şablondur.

* class (Bir sınıf oluşturmak, yani yeni bir nesne planı tanımlamaya başlamak için kullanılan anahtar kelimedir)  
* def (Sınıfın içinde o nesnenin davranışlarını, yani metotlarını (fonksiyonlarını) tanımlamak için kullanılır)  
* self (Metotların içinde, o an oluşturulan veya kullanılan nesnenin *kendisine* atıfta bulunmak için kullanılan zorunlu bir parametredir)  
* \_\_init\_\_() (Bir sınıftan yeni bir nesne oluşturulduğu anda otomatik olarak çalışan özel metottur, genellikle nesnenin başlangıç özelliklerini ayarlamak için kullanılır)

bu açıklamaların 100% eksiksiz bilgi diyemem ama aynı zamanda attığım deneme py. dosyalarında öğrenme süreci içinde kullandığım kodların çoğunluğu burda bilgi olarak verilmektedir neyin ne işe yaradığını  hem bu yazı ve py. çalışmalarımın bana faydası oldu. ÖDEVİ VE DENEMELERİ VISUAL STUDIO CODE ile birlikte yaptım

ömer faruk okuşluk 24011076

