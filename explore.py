
#EXCERCISE 1: Load It
import pandas as pd

df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print()
#EXCERCISE 2: Filter By Region
south = df[df['region'] == 'South']
print(len(south))
print(south.head())

print()
#EXCERCISE 3: Top 5 By Revenue
top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)