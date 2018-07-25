import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv('satislar.csv')

months = data[['Aylar']]
sales = data[['Satislar']]

xTrain, xTest, yTrain, yTest = train_test_split(months, sales, test_size=0.33,
                                                random_state=0)
"""
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)
Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)
"""

lr = LinearRegression()
lr.fit(xTrain, yTrain)

predicts = lr.predict(xTest)

xTrain = xTrain.sort_index()
yTrain = yTrain.sort_index()

plt.plot(xTrain, yTrain)
plt.plot(xTest, predicts)

plt.title("Aylara göre satış")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")