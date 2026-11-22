
#EXCERCISE 1: Load It
import pandas as pd

df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print()
#EXCERCISE 2: Top 5 By Revenue
south = df[df['region'] == 'South']
print(len(south))
print(south.head())