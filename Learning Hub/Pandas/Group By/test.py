import pandas as pd

df = pd.read_csv('Pandas/Group By/weather_by_cities.csv')
print(df)

'''
  Group by is used for grouping data based on certain columns and performing aggregate functions on them.
'''
g = df.groupby('city')
for city, city_df in g:
    print(city)
    print(city_df)

# Maximum temperature in each city
print("Maximum temperature in each city:")
for city, city_df in g:
    print(f"{city}: {city_df['temperature'].max()}")

'''

  alternative:
print(g['temperature'].max())

'''

# average wind speed per city
print("Average wind speed in each city:")
for city, city_df in g:
    print(f"{city}: {city_df['windspeed'].mean()}")


# describe
print(g.describe())