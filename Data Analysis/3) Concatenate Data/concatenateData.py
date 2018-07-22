# -*- coding: utf-8 -*-
"""
Created on 22.07.2018

@author: Muharrem Mandacı
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

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
