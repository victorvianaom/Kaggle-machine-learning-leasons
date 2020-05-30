import pandas as pd
import os
from sklearn.tree import DecisionTreeRegressor
import logging

# melborn_file_path = 'C:\\Users\\Rotciv\\Desktop\\Projects\\Kaggle-machine-learning-leasons\\02-Intro-To-Machine-Learning\\data\\melb_data.csv'
melborn_file_path = 'data\\melb_data.csv'
#melborn_data = pd.read_csv(melborn_file_path)
melborn_data = pd.read_csv(os.path.join(os.path.dirname(__file__), melborn_file_path))

print(melborn_data.describe())
help(melborn_data)
#print(dir(melborn_data))
print(melborn_data.columns)
#print(help(melborn_data.dropna))
melborn_data = melborn_data.dropna(axis=0)
print(melborn_data)
print(melborn_data.Price)
print(help(melborn_data.Price))
print('type of melborn_data:', type(melborn_data))
print('type of melborn_data.Price', type(melborn_data.Price))