# -*- coding: utf-8 -*-
"""
Created on 21.07.2018

@author: Muharrem Mandacı
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

"""
------------------------VERİ TİPLERİ------------------------------------------

Karegorik: sınıflandırılmaya uygun bilgi(erkek mi kadın mı gibi)
    Nominal: ne sıralanabilen ne de ölçülebilen veriler.(araba markası ...)
binomial (evet hayır gibi iki durum), polynomial(tr,us,en,fr...)
    Ordinal: Sıraya sokulabilen, büyüklük küçüklük ilişkisi olabilen ama
ölçülemeyen veriler.(kapı no, plaka no)
    Sayısal: (insan sayısı, ev büyüklüğü vb.)
    Oransal(ratio): birbirine göre orantılanabilen,çarpıp bölünebilen veriler
(yaş) birbirine orantılanabilecek anlamında.
    Aralık(interval): belirli bir aralıkta olan değerler.(sıcaklık!)
------------------------------------------------------------------------------
sayı tipindeki verilerle çalışan bir makine öğrenmesi algoritmasına yazısal
verileri de verebilmek için bu tipler arasında geçişler yapabilmek gerekecek.
------------------------------------------------------------------------------
tr,us,fr olana 1,2,3 gibi sayılar vermek bu değerlerin sıralanabilir olmasından
dolayı sorun olabilir bunun yerine bu üçünü ek birer sütun haline getirebiliriz
tr=1 olanda diğer ikisi 0 olacak şekilde.
------------------------------------------------------------------------------

"""

data = pd.read_csv('data.csv')

# separate different data
country = data.iloc[:, 0:1].values
gender = data.iloc[:, -1:].values
numericInfo = data.iloc[:, 1:4].values

# two different Encoder types
labelEncoder = LabelEncoder()

country[:, 0] = labelEncoder.fit_transform(country[:, 0])
gender[:, 0] = labelEncoder.fit_transform(gender[:, 0])

# OneHotEncoder needs numerical data
oneHotEncoder = OneHotEncoder(categorical_features='all')

country = oneHotEncoder.fit_transform(country).toarray()

# create data frames
dfCountry = pd.DataFrame(data=country, index=range(22),
                         columns=['fr', 'tr', 'us'])
dfNumber = pd.DataFrame(data=numericInfo, index=range(22),
                        columns=['height', 'weight', 'age'])
dfGender = pd.DataFrame(data=gender, index=range(22), columns=['gender'])

# concatenate data frames
result = pd.concat([dfCountry, dfNumber, dfGender], axis=1)

# print result
print(result)
