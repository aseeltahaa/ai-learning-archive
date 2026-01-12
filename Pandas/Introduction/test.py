import pandas as pd

# load csv into dataframe
df = pd.read_csv('Pandas/Introduction/weather.csv')
print(df)

# Quick Lookups
print(df.head())
print(df.tail(3))

# Information 
print("Shape of the DataFrame is:", df.shape)
print(f"The columns are: {df.columns}")
print(f"Number of rows is: {len(df)}")

# Slicing Rows
print(df[2:5]) # 2 till 4

# Selecting Columns
print(df.day)
print(df['day'])
print(df[['day', 'temperature']])

# Types of data 
print(type(df['day']))  #Series

# Maximum, Minimum, mean, Standard Deviation, & Variance
print("Maximum temperature is: ",df['temperature'].max())
print("Minimum temperature is: ",df['temperature'].min())
print("Mean temperature is: ",df['temperature'].mean())
print("Standard Deviation temperature is: ",df['temperature'].std())
print("Variance temperature is: ",df['temperature'].var())
print(df.describe())

# Filtering Data 
print("Days with temperature greater than 32:")
print(df[df.temperature > 32])
print("Days with maximum temperature:")
print(df[df.temperature == df.temperature.max()])

# Set Index : indeces are automatically assigned starting from 0
print(df.index)
df = df.set_index('day') 
# Alteraive: df/set_index('day', inplace=True)
print(df)

print(df.loc['1/3/2017']) #locate row with index '1/3/2017'

# Reset Index
df.reset_index(inplace=True)
print(df)