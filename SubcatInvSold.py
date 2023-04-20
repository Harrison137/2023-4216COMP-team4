import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')

#groups by sub categorys and sums the quantity
QuantityofSubcat = df.groupby('Sub-Category').sum({'Quantity': 'sum'}).sort_values('Quantity', ascending=False)
#title
print("\nAmount of Quantity by Sub-Category")
#loops through until all subcats are mentioned
for SubCat, row in QuantityofSubcat.iterrows():
    #print statement for sub cat name and the quantity sold (0 d.p)
    print(f"{SubCat}: {row['Quantity']:.0f} Units sold")
