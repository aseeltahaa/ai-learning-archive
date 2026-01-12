import pandas as pd

# read csv file
'''
df = pd.read_csv('Pandas/Read- Write into CSV/stock_data.csv', skiprows=1) # skip first row
print(df)
'''

# read csv file with header at specific row
'''
df = pd.read_csv('Pandas/Read- Write into CSV/stock_data.csv', header = 1) # headers are at row 1
print(df)
'''

# what if our csv has no headers?
# add custom headers
df = pd.read_csv('Pandas/Read- Write into CSV/stock_data.csv', skiprows=2, header=None, names = ["tickers", "eps", "revenue", "price", "people"])
print(df)

# read only specific number of rows
'''
df = pd.read_csv('Pandas/Read- Write into CSV/stock_data.csv', nrows=2)
print(df)
'''

# n.a. values
df = pd.read_csv('Pandas/Read- Write into CSV/stock_data.csv', na_values = ["not available", "n.a."])
print(df)

# custom na values for specific columns
df = pd.read_csv('Pandas/Read- Write into CSV/stock_data.csv', na_values = {
  "eps": ["not available", "n.a."], 
  "revenue": ["not available", "n.a.", -1],
  "people": ["not available", "n.a."]
  })
print(df)

# write dataframe to csv
df.to_csv("Pandas/Read- Write into CSV/test.csv", index=False)

# write dataframe to csv (specific columns)
df.to_csv("Pandas/Read- Write into CSV/test.csv", columns=["tickers", "price"], index=False)

