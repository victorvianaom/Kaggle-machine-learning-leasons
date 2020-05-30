import pandas as pd
import os
from sklearn.tree import DecisionTreeRegressor
import logging

# melborn_file_path = 'C:\\Users\\Rotciv\\Desktop\\Projects\\Kaggle-machine-learning-leasons\\02-Intro-To-Machine-Learning\\data\\melb_data.csv'
melborn_file_path = 'data\\melb_data.csv'
# melborn_data = pd.read_csv(melborn_file_path)
melborn_data = pd.read_csv(os.path.join(os.path.dirname(__file__), melborn_file_path))

y = melborn_data.Price # PREDICTION TARGET, by convention it is called y
melborn_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melborn_data[melborn_features] # PREDICTIVE FEATURES
print(X.describe())
print(X.head())

melborn_model = DecisionTreeRegressor(random_state=1)
melborn_model.fit(X, y)
print(melborn_model)
print(melborn_model.fit(X, y))
#logging.info(melborn_model.fit(X, y))
#logging.debug(melborn_model.fit(X, y))

print('Making Predictions for the following 5 houses: ')
print(X.head())
print('The predictions are: ')
print(melborn_model.predict(X.head()))
print(melborn_data.Price.head())