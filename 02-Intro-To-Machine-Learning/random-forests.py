import os
import pandas as pd

path = 'data\\melb_data.csv'
melborn_data = pd.read_csv(os.path.join(os.path.dirname(__file__), path))
melborn_data = melborn_data.dropna(axis=0)

y = melborn_data.Price
features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = melborn_data[features]

from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)