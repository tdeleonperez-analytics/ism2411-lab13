
#EXCERCISE 1: Load It
import pandas as pd

df = pd.read_csv('data/retail_sales.csv')
print("DataFrame Basic Information:")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print()
#EXCERCISE 2: Filter By Region
print("Filtered by Region: SOUTH")
south = df[df['region'] == 'South']
print(len(south))
print(south.head())

print()
#EXCERCISE 3: Top 5 By Revenue
print("Filtered by Revenue: TOP 5")
top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)

print()
#EXCERCISE 4: Two-Condition Filter
print("TWO CONDITION FILTER")
big_south = df[(df['region']=='South') & (df['revenue']>1000)]
print(len(big_south))
print(big_south.head())