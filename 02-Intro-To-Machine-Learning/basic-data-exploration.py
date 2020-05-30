import pandas as pd
import os

# melborn_file_path = 'C:\\Users\\Rotciv\\Desktop\\Projects\\Kaggle-machine-learning-leasons\\02-Intro-To-Machine-Learning\\data\\melb_data.csv'
melborn_file_path = 'data\\melb_data.csv'
#melborn_data = pd.read_csv(melborn_file_path)
melborn_data = pd.read_csv(os.path.join(os.path.dirname(__file__), melborn_file_path))

print(melborn_data.describe())
#help(melborn_data)
print(dir(melborn_data.describe))