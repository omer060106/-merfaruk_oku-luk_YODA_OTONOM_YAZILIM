Git ve GitHub Nedir

Git= Özellikle yazılım geliştiriciler tarafından kullanılan dağıtık  bir sürüm kontrol sistemidir. Kodun geçmişini saklar, kim neyi ne zaman değiştirmiş takip eder ve gerektiğinde önceki hâle dönmeni sağlar.Bu sayede ana kod bozulmaya uğramaz karmaşıklıklar çıkmaz geliştirmek ve takip daha kolay hale gelir

GitHub: Git ile yönetilen depoları internette barındıran bir hizmettir. Yazılım geliştiricilerin kodlarını internet üzerinden paylaşabildiği, saklayabildiği ve birlikte geliştirebildiği bir platformdur

GitHub Temel Özellikleri

Depolar (Repositories)= 

Her proje bir repo olarak adlandırılır.
Repo içinde proje dosyaları, sürüm geçmişi ve proje ile ilgili dökümantasyon bulunur.

Versiyon Kontrolü =

Git ile entegre çalışır.
Kodda yapılan değişiklikler commit adı verilen kayıtlarla saklanır.
Eski sürümlere geri dönme veya farklı sürümler üzerinde çalışma imkanı sağlar.

Branch (Dal) Yönetimi =

Projede farklı branch ler oluşturularak, yeni özellikler geliştirilirken ana kod akışı korunur.
Daha sonra branch ler birleştirilerek proje güncellenir.

Pull Request ve Kod İncelemesi =

Başka bir geliştiricinin yaptığı değişiklikleri projeye eklemeden önce inceleme ve onay süreci uygulanabilir.
Bu yöntem, hataları azaltır ve işbirliğini kolaylaştırır.

GitHub Pages =

Projeler için statik web siteleri oluşturma imkanı sağlar.
Genellikle dokümantasyon veya portföy siteleri için kullanılır.

Issues ve Project Boards =

Hata takibi, görev yönetimi ve proje planlaması için kullanılır.
Ekipler için iş takibi ve organizasyonu kolaylaştırır.




-Repository, commit, branch, stage, merge, pull, push

1 Repository = Bir projeye ait depo alanıdır. Geçmiş değişiklikleri dalları commitleri içinde barındırır.
 
git cd C:/Users/ömer/Desktop/otonom yazılım 2.hafta

git init 


2 Commit = dosyadaki değişikleri kaydetme yaptığın bir değişikliği önce ekler sonra commit işlemiyle mesajınla birlikte kaydedilir.


git add YODA.txt

git commit -m "-bilgi vermek amaçlı buraya mesajınızı yazıyorsunuz"


3 Stage = Commite dahil etmek istediğin değişiklikleri geçici olarak koyduğun yer. Staging alanı hangi değişikliklerin bir sonraki commite dahil edileceğini kontrol etmene yarar. bu sayede ddirekt değişiklikleri ana daldan yapmadan kontrollü şekilde yapıp commitleme işlemini yapılabilir

git add YODA.txt ( bu txt te değişiklik yapıldı varsayalım)

git status (değişiklikleri görmek)

git commit -m "YODA.txt dosyasında değişiklik yapıldı"



Branch = Ana projeyi bozma korkusu olmadan, yeni bir özelliği denemek veya bir hatayı düzeltmek için oluşturduğun projenin bağımsız bir kopyası. Bu ayrı yolda işin bittiğinde yaptığın değişiklikleri ana projeyle birleştirebilir veya beğenmezsen tamamen silebilirsin.

git branch (mevcut branch i görürsün)

git branch YODAyenidal (yeni branch oluşturmanı sağlar) 

git checkout main (ana branch e geçersin)
git merge YODAyenidal (yeni branch i ana branch ile birleştirmeyi sağlar)

git branch -d YODAyenidal ( merge edilmiş branch i silmeyi sağlar merge edilmediyse -D kullanılmalıdır)




Merge = Yeni bir özellik eklediğinde veya bir hatayı düzelttiğinde bu değişiklikleri ana projeye dahil etmek istediğinde merge kullanırsın.

git checkout main (ana branch e geçersin)
git merge YODAyenidal (yeni branch i ana branch ile birleştirmeyi sağlar)


Pull = Projeni GitHub veya başka bir uzak depodan güncel tutmak istediğinde pull kullanırsın bu komut uzak depodaki değişiklikleri yerel bilgisayarına getirir ve otomatik olarak birleştirmeye çalışır.

git pull origin main ( değişiklikleri yerel main branch e getirir)


Push = Yerel bilgisayarda yaptığın değişiklikleri uzak depoya göndermek için push kullanırsın böylece ekip arkadaşların da senin yaptığın değişiklikleri görebilir.



bunlar temel bilgilerdi git in bir çok kullanım şekli mevcut bunların hepsini burada veremeyebilirim ancak pratik ve çalışmayla bunları  ben ve ekip arkdaşlarımız öğreneceğini düşünüyorum.Bu süreçte öğrenme sırasındaki denemelerimi de ek bir pdf olacak şekilde repoma koyacağım 