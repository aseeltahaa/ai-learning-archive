import pandas as pd
import numpy as np

'''
 replace() function is used to replace specific values in a DataFrame with other values.
'''

df = pd.read_csv('Pandas\Handling Missing Values\Part 2\weather_data.csv')
print("Original DataFrame:")
print(df)

temp1 = df.replace({-99999, 0}, np.nan)
print("DataFrame after replacing -99999 with NaN:")
print(temp1)

temp2 = df.replace(
  {
    # column name, nan value
    'temperature': -99999,
    'windspeed': -99999,
    'event': '0'
  }, 
  np.nan
)
print("DataFrame after replacing specific values with NaN:")
print(temp2)

# regex for unit of measure conversions
temp3 = df.replace(
  {
    'temperature': '[A-Za-z]' ,
    'windspeed':  '[A-Za-z]'
  },
  # replace these values with a blank string
   '', regex=True
  )
print("DataFrame after removing alphabetic characters:")
print(temp3)

# Another data frame
print("\n\n\nAnother DataFrame Example:")
df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})

print("Original DataFrame:")
print(df)

df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4], inplace=True)
print("DataFrame after vectorized replacement:")
print(df)
