# libraries
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# read data from csv
data = pd.read_csv('data.csv')

# separate data
country = data.iloc[:, 0:1].values
gender = data.iloc[:, -1:].values
numericInfo = data.iloc[:, 1:4].values

# Encode string features
labelEncoder = LabelEncoder()
oneHotEncoder = OneHotEncoder(categorical_features="all")

country[:, 0] = labelEncoder.fit_transform(country[:, 0])
gender[:, 0] = labelEncoder.fit_transform(gender[:, 0])

country = oneHotEncoder.fit_transform(country).toarray()

# convert to data frame from numpy array
dfCountry = pd.DataFrame(data=country, index=range(22),
                         columns=['fr', 'tr', 'us'])
dfNumber = pd.DataFrame(data=numericInfo, index=range(22),
                        columns=['height', 'weight', 'age'])
dfGender = pd.DataFrame(data=gender, index=range(22), columns=['gender'])

# concat encoded data
data = pd.concat([dfCountry, dfNumber, dfGender], axis=1)

# multiple linear regression for predicting gender

# train data
trainData = pd.concat([dfCountry, dfNumber], axis=1)

# output
output = dfGender

# determine test and train datas
xTrain, xTest, yTrain, yTest = train_test_split(trainData, output,
                                                test_size=0.33, random_state=0)

# fit model
linearRegression = LinearRegression()
linearRegression.fit(xTrain, yTrain)

# prediction
predict = linearRegression.predict(xTest)

# multiple linear regression for predicting height

# train data
leftOfHeight = data.iloc[:, :3]
rightOfHeight = data.iloc[:, 4:]

# output
height = data.iloc[:, 3:4].values

trainDataForHeight = pd.concat([leftOfHeight, rightOfHeight], axis=1)

# determine test and train datas
xTrainH, xTestH, yTrainH, yTestH = train_test_split(trainDataForHeight, height,
                                                    test_size=0.33,
                                                    random_state=0)

# fit model
linearRegressionH = LinearRegression()
linearRegressionH.fit(xTrainH, yTrainH)

# prediction
predictH = linearRegression.predict(xTestH)
