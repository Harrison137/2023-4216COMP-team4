import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')

#groups by region and sums the discounts
discount_by_highest = df.groupby('Region').sum({'Discount': 'sum'}).sort_values('Discount', ascending=False)
#gives a title
print("\nAmount Given In Discounts By Region (Highest to Lowest):")
#loops through all the regions
for region, row in discount_by_highest.iterrows():
    #prints region and tells the total discount (2 d.p)
    print(f"{region}: ${row['Discount']:.2f} in discounts")
