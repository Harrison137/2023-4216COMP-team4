import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')
#this makes sure that only categorys that are technolgy are counted
onlyTechnologyCata = df[df['Category'] == 'Technology']
#groups the tech catagory by state and calculates the sum of the quantity for each group
groupedWithAll = onlyTechnologyCata.groupby(['State', 'Category']).agg({'Quantity': 'sum'}).reset_index()
#sort the data by decending order by quantity (the top 10 states)
groupedAndSorted = groupedWithAll.sort_values('Quantity', ascending=False).head(10)
# Tit;e + Print the best selling category (by quantity) for each state
print("\n Top 10 Best states that sold the most technology")
print(groupedAndSorted[['State', 'Category', 'Quantity']])
