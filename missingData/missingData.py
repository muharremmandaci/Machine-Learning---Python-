# -*- coding: utf-8 -*-
"""
Created on 20.07.2018

@author: Muharrem Mandacı
"""
# import libraries
import pandas as pd
from sklearn.preprocessing import Imputer

# import data
data = pd.read_csv('missingData.csv')

# completing missing datas
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)

missingData = data.iloc[:, 1:4].values
imputer = imputer.fit(missingData)               # missingDatas[:,0:3]
completedData = imputer.transform(missingData)   # missingDatas[:,0:3]

data.iloc[:, 1:4] = completedData

# print completed data
print(data)
