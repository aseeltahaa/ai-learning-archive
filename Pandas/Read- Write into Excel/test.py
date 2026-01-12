import pandas as pd

# converter function
def convert_people_cell(cell):
    if cell == "n.a.":
        return "jane doe"
    return cell

# read Excel file
df = pd.read_excel(
    'Pandas\Read- Write into Excel\stock_data.xlsx',
    'Sheet1',
    converters={
        'people': convert_people_cell
    }
)

print(df)

df.to_excel("Pandas/Read- Write into Excel/new.xlsx", sheet_name = "stocks", startrow = 1, startcol= 2, index = False)


# Another example using custom dfs 
df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

# Note: if this file already exists, it gets over-written
with pd.ExcelWriter('Pandas\Read- Write into Excel\stock_data.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")