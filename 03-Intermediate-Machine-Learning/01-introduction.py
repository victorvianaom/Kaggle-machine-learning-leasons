### Pipelines,
### Cross-validation
### XGBoost
### Leakage
import os
import pandas as pd
from sklearn.model_selection import train_test_split

path_train = os.path.join(os.path.dirname(__file__), 'data\\train.csv')
path_test = os.path.join(os.path.dirname(__file__), 'data\\test.csv')
X_full = pd.read_csv(path_train)
X_test_full = pd.read_csv(path_test)

y = X_full.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = X_full[features].copy() ##Modifications to the data or indices of the copy will not be reflected in the original object
X_test = X_test_full[features].copy()

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

print(X_train.head())
#print(help(pd.DataFrame.copy))

## defining various models:
from sklearn.ensemble import RandomForestRegressor

model_1 = RandomForestRegressor(n_estimators=50, random_state=0)
model_2 = RandomForestRegressor(n_estimators=100, random_state=0)
model_3 = RandomForestRegressor(n_estimators=100, criterion='mae', random_state=0)
model_4 = RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0)
model_5 = RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0)

models = [model_1, model_2, model_3, model_4, model_5]

## The best model will obtain the lowest MAE:
from sklearn.metrics import mean_absolute_error

def score_model(model, X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    model.fit(X_t, y_t)
    preds = model.predict(X_v)
    return mean_absolute_error(y_v, preds)

for i in range(0, len(models)):
    mae = score_model(models[i])
    print("Model %d MAE: %d" % (i+1, mae))
