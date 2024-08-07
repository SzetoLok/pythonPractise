# import sys
# print(sys.path)
import pandas as pd
from sklearn.tree import DecisionTreeClassifier\

melbourne_data = pd.read_csv('./melb_data.csv')
melbourne_data.reset_index(inplace=True)
# melbourne_data.head()
# y = melbourne_data.Price
# melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
# X = melbourne_data[melbourne_features]
# X.head()
print(melbourne_data)