# -*- coding: utf-8 -*-
"""
Created on 22.07.2018

@author: Muharrem Mandacı
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# read data from excel
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

# convert to data frame from numpy array
dfCountry = pd.DataFrame(data=country, index=range(22),
                         columns=['fr', 'tr', 'us'])
dfNumber = pd.DataFrame(data=numericInfo, index=range(22),
                        columns=['height', 'weight', 'age'])
dfGender = pd.DataFrame(data=gender, index=range(22), columns=['gender'])

# concatenate data frames
data = pd.concat([dfCountry, dfNumber], axis=1)
output = dfGender

# separate to data as train and test data
xTrain, xTest, yTrain, yTest = train_test_split(data, output,
                                                test_size=0.33, random_state=0)
"""
Standardisation : Z = (x-mean)/(standard deviation)
    verilerin birbirleri ile olan farkını bozmadan orta değerden ne kadar
  saptıklarını gösterecek şekilde indirgenmesi

Normalisation : Z = (x-min(x))/(max(x)-min(x))
    birebir bir alana indirgenmesi. marjinal değerler olduğunda sıkıntılıdır.
"""

# scale train and test data
sc = StandardScaler()
scaledXTrain = sc.fit_transform(xTrain)
scaledXTest = sc.fit_transform(xTest)
