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

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
forest_model_prediction = forest_model.predict(val_X)
print(mean_absolute_error(val_y, forest_model_prediction))

## now I put the 2 models side by side (Decision Tree and Random Forest)
from sklearn.tree import DecisionTreeRegressor
decision_tree_model = DecisionTreeRegressor(random_state=1)
decision_tree_model.fit(train_X, train_y)
decision_tree_model_prediction = decision_tree_model.predict(val_X)
print(mean_absolute_error(val_y, decision_tree_model_prediction))

### Random Forests performed much better