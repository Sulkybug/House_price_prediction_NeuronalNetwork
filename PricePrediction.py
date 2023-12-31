# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rumjM1tqqcOorciJiJ7knOCVa8zRAuaa
"""

import keras
import numpy as np
import pandas as pd

"""# Nueva sección"""

dataHouses = pd.read_csv('Assignment 2_BUSI 651_House Prices.csv')
dataHouses.head()

# x is equal to all values without Sale Price
x = dataHouses.drop(columns= ['SalePrice'])
print(x)
# y is equal to Sale Price
y = dataHouses[['SalePrice']]
print(y)

#Model
model = keras.Sequential()
#adding layers
model.add(keras.layers.Dense(4, activation='relu', input_shape=(4, )))
# we add 4 layers for each data value
#relu is an algo that put values in a scale of 0 to 1
model.add(keras.layers.Dense(4, activation='relu'))
# adding single neurone for the sale price
model.add(keras.layers.Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

#Training model
#epochs number of times it will train
model.fit(x, y, epochs= 100, callbacks=[keras.callbacks.EarlyStopping(patience=5)] )
#keras.callbacks.EarlyStopping will stop the training if ther is not improvement

#Test Model

def runModel(GarageCars, GarageArea, OverallQual, GrLivArea, realValuePrice):
    testHousesData = np.array([GarageCars, GarageArea, OverallQual,  GrLivArea])
    realValuePrice = realValuePrice
    predictionValue = model.predict(testHousesData.reshape(1,4), batch_size=1)
    predictionValueNumber = round(predictionValue[0][0])
    print("Prediction")
    print(predictionValueNumber)
    print("Real Price")
    print(realValuePrice)
    print("Diference with given value")
    print(predictionValueNumber - realValuePrice)


runModel(2, 836, 8, 2198, 250000)
runModel(1, 480, 5, 1362, 143000)
runModel(3, 820, 9, 3140, 485000)
runModel(3, 264, 6, 918, 99500)

model.save('housing_pricing_model.h5')