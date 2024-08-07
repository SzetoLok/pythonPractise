import pandas as pd
from pandas import DataFrame
# cars = pd.read_csv('/Users/szetolok/Desktop/Coding/pythonPractise/pandasEx/Automobile_data.csv')
cars = pd.read_csv('pandasEx/Automobile_data.csv')
filter = cars[(cars['company'] == 'audi')]
# cars = cars.filter(like='c')
# cars = cars.where(filter)
print(filter)
cars = cars.rename(columns = {'company':'firm'})
print(cars)
# pd.options.display.max_rows = 1
# pd.set_option("display.min_rows", 9)
# print(type(cars))
# print(cars.describe())
# a = cars.describe()
# print(type(a))
# print(cars.values)
# print(cars.head(5))
# print(cars.tail(5))
# print(cars.at[0, 'company'])
# print(cars.iat[0, 2])
# print(cars.get('wheel-base'))

# name_dict = {
#     'name':['lucas', 'carol'],
#     'age':[23,22],
#     'gender':['m','f']
# }

# name_df = pd.DataFrame(name_dict)
# name_df.insert(loc=2, column='Address', value=['hong kong island', 'kowloon'])
# print(name_df)
# name_df = name_df.drop(columns='age')
# print(name_df)

# name_df.info()
# print(name_df.describe())