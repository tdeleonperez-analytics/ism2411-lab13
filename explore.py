# ---SELF ASSESSMENT QUESTIONS ---
#1) A boolean filter is a way to filter data in a DataFrame using True/False conditions.
#2) df[revenue] is a single column selection, meaning it only brings back the 'revenue' column (Series). df[['revenue']] is a double bracket selection, meaning it brings back a ***DataFrame*** with the 'revenue' column, not a Series.
#3) I can perform the same task for thousands of rows in Pandas, even when the data itself is not always the same. This saves me loads of time and effort, as I can write a single line of code to filter or manipulate large datasets instead of doing it manually.

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

print()
#EXCERCISE 5: A New Column
df['per_unit'] = df['revenue'] / df['quantity']
print("DataFrame with New Column:")
print(df.head())
print(df['per_unit'].mean())

print()
#EXCERCISE 6: Unique Values
print("Unique Values in 'region' Column:")
print(df['region'].unique())
print(df['region'].value_counts())

print()
#EXCERCISE 7: Select Columns
new_df = df[['region', 'product', 'revenue']]
print("New DataFrame with Selected Columns:")
print(new_df.shape)

print()
#EXCERCISE 8: Save
df.to_csv('data/explored.csv', index=False)