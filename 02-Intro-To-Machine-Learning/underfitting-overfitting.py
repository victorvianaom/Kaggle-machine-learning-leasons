import os
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

path = 'data\\melb_data.csv'
melborn_data = pd.read_csv(os.path.join(os.path.dirname(__file__), path))
melborn_data = melborn_data.dropna(axis=0)

y = melborn_data.Price
features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = melborn_data[features]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0) # balaceia o under com overfitting
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae

leaf_set = [2, 3, 4, 5, 10, 20, 50, 100, 250, 500, 5000, 50000]
mae_list = []
for max_leaf_nodes in leaf_set:
    mae_list.append(get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y))
    #print("Max leaf nodes: %d \t\t Mean Absolute Error: %d" %(max_leaf_nodes, my_mae))
print(mae_list)
best_tree_size = leaf_set[mae_list.index(min(mae_list))]
print('Best tree size: ', best_tree_size)

## now I know the best_tree_size I should use all the data for my final model
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=0)
final_model.fit(X, y)


