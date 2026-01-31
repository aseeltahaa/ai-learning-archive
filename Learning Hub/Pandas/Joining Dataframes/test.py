import pandas as pd

'''
Merging Dataframes VS Concatenating Dataframes

Merging Dataframes:
- Combines DataFrames based on common columns or indices.
- Similar to SQL JOIN operations.
- Allows for more complex data relationships.

Concatenating Dataframes:
- Stacks DataFrames either vertically (row-wise) or horizontally (column-wise).
- Does not require common columns or indices.
'''

# Lebanon weather data
lebanon_weather = pd.DataFrame({
    'city': ['Beirut', 'Tripoli', 'Sidon'],
    'temperature': [30, 28, 32],
    'humidity': [70, 65, 75]
})
print("Lebanon Weather DataFrame:\n", lebanon_weather)

# Syria weather data
syria_weather = pd.DataFrame({
    'city': ['Damascus', 'Aleppo', 'Homs'],
    'temperature': [35, 33, 34],
    'humidity': [60, 55, 65]
}, index = [0,1,2])
print("\nSyria Weather DataFrame:\n", syria_weather)

# Concatenates as rows
df = pd.concat([lebanon_weather, syria_weather], ignore_index=True)
print("\nConcatenated Dataframe: \n", df)

# Concatenates with keys (MultiIndex)
df2 = pd.concat([lebanon_weather, syria_weather], keys=['Lebanon', 'Syria'])
print("\nConcatenated Dataframe with Keys: \n", df2)

# Accessing data using keys
print("\nLebanon Data:\n", df2.loc['Lebanon'])
print("\nSyria Data:\n", df2.loc['Syria'])

# Syria windspeed data
syria_windspeed = pd.DataFrame({
    'city': ['Aleppo', 'Homs'],
    'windspeed': [15, 20]
}, index = [1, 2])
print("\nSyria Windspeed DataFrame:\n", syria_windspeed)

# Concatenates as columns
df4 = pd.concat([syria_weather, syria_windspeed], axis=1)
print("\nConcatenated Dataframe along Columns: \n", df4)

# Using index
df5 = pd.concat([syria_weather, syria_windspeed], axis=1)
print("\nConcatenated Dataframe along Columns: \n", df5)

# Inner join (default): Only common cities
merged_df_inner = pd.merge(syria_weather, syria_windspeed, on='city')
print("\nInner Joined- Merged Dataframe on 'city' column: \n", merged_df_inner)

# Outer join: All cities from both DataFrames
merged_df_outer = pd.merge(syria_weather, syria_windspeed, on='city', how='outer', indicator=True)
print("\nOuter Joined- Merged Dataframe on 'city' column: \n", merged_df_outer)

# Left join: All cities from syria_weather
merged_df_left = pd.merge(syria_weather, syria_windspeed, on='city', how='left')
print("\nLeft Joined- Merged Dataframe on 'city' column: \n", merged_df_left)

# Right join: All cities from syria_windspeed
merged_df_right = pd.merge(syria_weather, syria_windspeed, on='city', how='right')
print("\nRight Joined- Merged Dataframe on 'city' column: \n", merged_df_right)
