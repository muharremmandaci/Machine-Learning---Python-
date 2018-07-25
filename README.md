# Machine Learning - Python (Beginner)


## Dummy Variable(Kukla Değişken)

  bazı özellikler(feature) birbiri ile korelasyon içindedir. İl bilgisi ve plaka bilgisi birlikte verilmesi bu duruma örnektir. Bu şekildeki verilerin birlikte data setinde bulunması sorun teşkil edebilir.

> gender = m m w m w w m
> m      = 1 1 0 1 0 0 1
> w      = 0 0 1 0 1 1 0

  gender m ve w olacak şekilde ayarlandıktan sonra bunlardan biri alınması yeterli olacaktır. Yoksa bu özelliğinin etkisi diğerlerinden fazla olacaktır.


## P-Değeri

H0 : null hypothesis : temelde kabul edilen hipotez
H1 : alternative hypothesis

p-değeri küçüldükçe H0 hatalı olma ihtimali artar.
p-değeri büyüdükçe H1 hatalı olma ihtimali artar.

## Değişken(Özellik/Feature) Seçimi

Bazı değişkenler sisteme olumsuz etki yapabilirler. Bu yüzden çok değişkenli modellerde değişken seçimi de önemlidir.

### Bütün Değişkenler
* Daha öncedene bir seçim yapılmışsa veya değişkenlerin kalitesinden eminsek tüm değişkenleri kullanabiliriz.
* Zorunluluk var, projede kullanılmaları zorunlu koşulmuş olabilir.
* Diğer yöntemleri kullanmadan önce fikir edinmek amacıyla tüm değişkenler kullanılabilir.

### Geriye Eleme(Back Elimination)
* Signifance Level seçilir(genelde 0.05)
* Bütün değişkenler kullanılarak model inşa edilir.
* En yükse p-value değerine sahip olan değişken ele alınır ve şayet P>SL ise 4. adıma, değilse son adıma(6. adım) gidilir.
* 3. adımda seçilen ve en yüksek p-değerine sahip değişken sistemden kaldırılır.
* Makine öğrenmesi güncellenir ve 3.adıma geri dönülür.
* Makine öğrenmesi sonlandırılır.

### İleriye Seçim(Forward Selection)
* SL seçilir(genelde 0.05)
* Bütün değişkenler kullanılarak model inşa edilir.
* En düşük p-değerine sahip olan değişken ele alınır.
* 3. aşamadaki değişken sabit tutularak yeni bir değişken seçilir ve sisteme eklenir.
* Makine öğrenmesi güncellenir ve 3.adıma geri dönülür. Şayet en düşük p-değerine sahip değişken için P<SL şartı sağlanıyor 3.adıma geri dönülür, sağlanmıyorsa biter
* Makine öğrenmesi sonlandırılır.

### İki Yönlü Eleme(bidirectional elimination)
* SL seç(genel 0.5)
* Bütün değişkenlerle bir model inşa et
* en düşük p-değerine sahip değişkeni ele al.
* 3.adımda seçilen değişkeni sabit tutularak diğer bütün değişkenler sisteme dahil edilir. Ve en düşük p değerine sahip olan sistemde kalır.
* SL değerinin altında olan değişkenler sistemde kalır ve eski değişkenlerden hiçbiri sistemden çıkarılamaz.
* makina öğrenmesi sonlandırılır.

### Bütün Yöntemler(custom)
* Başarı kriteri belirlenir.
* Bütün olası regresyon modelleri inşa edilir.(ikili seçim olur.)
* Başta belirlenen kriteri en iyi sağlayan yöntem seçilir.
* makina öğrenmesi sonlandırılır.
