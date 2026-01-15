import pandas as pd

'''
1- fillna() Method:
  Used to fill missing values with a specified value or method.

2- interpolate() Method:
  Used to fill missing values using interpolation techniques.

3- dropna() Method:
  Used to remove rows or columns with missing values.
'''

df = pd.read_csv('Pandas/Handling Missing Values/Part 1/weather_data.csv', parse_dates=['day'])
df.set_index('day', inplace=True)
print(df)

temp = df.fillna(0)
print("After using fillna: ")
print(temp)

temp2 = df.fillna({
  'temperature' : 0,
  'windspeed' : 0,
  'event' : 'no event'
})
print("After using custom fillna: ")
print(temp2)

temp3 = df.fillna(method = "ffill") # forward fill
print("After using forward fill: ")
print(temp3)

temp4 = df.fillna(method = "bfill") # backward fill
print("After using backward fill: ")
print(temp4)

# limit the filled values to x times 
temp5 = df.fillna(method = "ffill", limit = 1)
print("After using forward fill with limit: ")
print(temp5)

# linear interpolation
temp6 = df.interpolate()
print("After using interpolate: ")
print(temp6)

# time interpolation
temp7 = df.interpolate(method = "time")
print("After using time interpolate: ")
print(temp7)

# drop rows with any missing values
temp8 = df.dropna()
print("After using dropna to remove rows with any missing values: ")
print(temp8)

# threshold to drop rows with at least x non-missing values
temp9 = df.dropna(thresh = 2)
print("After using dropna with threshold: ")
print(temp9)
