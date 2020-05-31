import os
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

melborn_file_path = 'data\\melb_data.csv'
melborn_data = pd.read_csv(os.path.join(os.path.dirname(__file__), melborn_file_path))

melborn_data = melborn_data.dropna(axis=0)

y = melborn_data.Price # PREDICTION TARGET, by convention it is called y
melborn_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = melborn_data[melborn_features] # PREDICTIVE FEATURES

melborn_model = DecisionTreeRegressor(random_state=1) # Define the model
melborn_model.fit(X, y) # Fit

predicted_home_prices = melborn_model.predict(X)
error_1 = mean_absolute_error(y, predicted_home_prices)
print(error_1)

### now doing the split in the sample
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

melborn_model = DecisionTreeRegressor(random_state=1)
melborn_model.fit(train_X, train_y)

y_predicted = melborn_model.predict(val_X)
error_2 = mean_absolute_error(val_y, y_predicted)
print(error_2)

print('Ratio: ', error_2 / error_1)