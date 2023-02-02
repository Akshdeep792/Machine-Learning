# -*- coding: utf-8 -*-
"""simple_linear_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ITuKnFjvtOhrc9DnTc4Bbb4P2pA2OYGG

# Simple Linear Regression

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

print(X)

print(Y)

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state = 0)

"""## Training the Simple Linear Regression model on the Training set"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train) #training the model

"""## Predicting the Test set results"""

Y_pred = regressor.predict(X_test)

"""## Visualising the Training set results"""

plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue') # regression line
plt.title('Salary vs Experience (Training Set)' )
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""## Visualising the Test set results"""

plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue') # same regresion line 
plt.title('Salary vs Experience (Test Set)' )
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""# Making a single prediction (for example the salary of an employee with 12 years of experience)"""

print(regressor.predict([[12]]))

"""# Getting the final linear regression equation with the values of the coefficients"""

print(regressor.coef_)
print(regressor.intercept_)