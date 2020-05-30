import os
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

melborn_file_path = 'data\\melb_data.csv'
melborn_data = pd.read_csv(os.path.join(os.path.dirname(__file__), melborn_file_path))

melborn_data = melborn_data.dropna(axis=0)

y = melborn_data.Price # PREDICTION TARGET, by convention it is called y
melborn_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = melborn_data[melborn_features] # PREDICTIVE FEATURES

melborn_model = DecisionTreeRegressor(random_state=1) # Define the model
melborn_model.fit(X, y) # Fit

predicted_home_prices = melborn_model.predict(X)
print(mean_absolute_error(y, predicted_home_prices))