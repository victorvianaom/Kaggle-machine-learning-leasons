### three aproaches to dealing with missing values
### 1) A Simple Option: Drop Columns with Missing Values
### 2) A Better Option: Imputation (give the mean value to the missing field), 
###    usually leads to more accurate models than droping
### 3) An Extension To Imputation
###
### Imputation is the standard approach, and it usually works well.

import os
import pandas as pd
from sklearn.model_selection import train_test_split

path = 'data\\melb_data.csv'
data = pd.read_csv(os.path.join(os.path.dirname(__file__), path))
#print(data.head())

y = data.Price
#print(y.head())
melb_predictors = data.drop(['Price'], axis=1)
X = melb_predictors.select_dtypes(exclude=['object'])

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

### Score from Approach 1 (Drop Columns with Missing Values):
##get name of columns with missing values:
#print(X_train.columns)
cols_with_missing = [col for col in X_train.columns if X_train[col].isnull().any()]
#print(cols_with_missing)
reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)
print('MAE from aproach 1 (Drop columns with missing values): ')
print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))

### Score from aproach 2 (Imputation):
from sklearn.impute import SimpleImputer #we use SimpleImputer to replace missing values with the mean value along each column.
## imputaion
my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.fit_transform(X_valid))
## imputation removed column names, put them back:
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns
print('MAE from aproach 2 (Imputation): ')
print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))

### Score from aproach 3 (An extension to Imputation): 
X_train_plus = X_train.copy()
X_valid_plus = X_valid.copy()
for col in cols_with_missing:
    X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
    X_valid_plus[col + '_was_missing'] = X_valid_plus[col].isnull()
## Imputation
my_imputer = SimpleImputer()
imputed_X_train_plus = pd.DataFrame(my_imputer.fit_transform(X_train_plus))
imputed_X_valid_plus = pd.DataFrame(my_imputer.fit_transform(X_valid_plus))
#putting the column names BACKÇ
imputed_X_train_plus.columns = X_train_plus.columns
imputed_X_valid_plus.columns = X_valid_plus.columns
print('MAE from aproach 3 (An extension to imputation): ')
print(score_dataset(imputed_X_train_plus, imputed_X_valid_plus, y_train, y_valid))

print(X_train.shape)
