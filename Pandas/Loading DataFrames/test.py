import pandas as pd

# read from csv file
df = pd.read_csv('Pandas/Loading DataFrames/weather_data.csv')
print(df)

# read from excel file
df2 = pd.read_excel('Pandas/Loading DataFrames/weather_data.xlsx','Sheet1')
print(df2)

# read from python dictionary
data = {
    'day': ['1/1/2020', '1/2/2020', '1/3/2020'],
    'temperature': [32, 35, 28],
    'windspeed': [6, 7, 2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df3 = pd.DataFrame(data)
print(df3)

# read from a tuple list
data_tuples = [
    ('1/1/2020', 32, 6, 'Rain'),
    ('1/2/2020', 35, 7, 'Sunny'),
    ('1/3/2020', 28, 2, 'Snow')
]
df4 = pd.DataFrame(data_tuples, columns=['day', 'temperature', 'windspeed', 'event'])
print(df4)

# read from a dictionary list
data_dicts = [
    {'day': '1/1/2020', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},  
    {'day': '1/2/2020', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},  
    {'day': '1/3/2020', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'} 
]
df5 = pd.DataFrame(data_dicts)
print(df5)