import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')

def option1():
    #makes orderdate into a date time object
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    #groups the columns we want to compare and sums up the Quantity
    quantityDate = df.groupby('Order Date')['Quantity'].sum()
    #creates bar chart and title and names of axis'
    plt.bar(quantityDate.index, quantityDate.values)
    plt.title('Quantity Over Time')
    plt.xlabel('Date')
    plt.ylabel('Quantity')

    # Set the x-axis writing to 45 degrees so its readable
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()

def option2():
    #groups columns we want to compare and sums up the Discounts
    RegionDiscounts = df.groupby('Region')['Discount'].sum()
    #creates bar chart and title and names of axis'
    plt.bar(RegionDiscounts.index, RegionDiscounts.values)
    plt.title('Discounts Per Region')
    plt.xlabel('Discounts')
    plt.ylabel('Region')
    #Show the plot
    plt.show()

def option3():
    #groups columns we want to compare and sums up the Profits
    profitData = df.groupby('Category')['Profit'].sum()
    #This creates a pie chart to display the data// autopct used to display percentage of pie chart
    plt.pie(profitData.values, labels=profitData.index, autopct='%1.1f%%')
    plt.title('Percentage of profits each Category Owns')
    plt.show()

def option4():
    #converts the date into date and time format and into only the years
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
    df['Year'] = df['Order Date'].dt.year
    #grouping the year column with the sum of the discounts for the year
    gbYear = df.groupby(['Year'])['Discount'].sum()

    #creates plot graph and title and names of axis'
    plt.plot(gbYear.index, gbYear.values)
    plt.title('Discount Per Year')
    plt.xlabel('Date')
    plt.ylabel('Discount')

    # Set the x-axis writing to 45 degrees so its readable
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()
#prints oprions to the user
def options():
    print("[0] To leave")
    print("[1] Option 1: Quantity by Month")
    print("[2] Option 2: Regional Discounts")
    print("[3] Option 3: Catagory Profit Percentage")
    print("[4] Option 4: Discounts Per Year")
#Running the code
while True:
    options()
    option = int(input())
    if option == 0:
        break
    elif option == 1:
        option1()
    elif option== 2:
        option2()
    elif option==3:
        option3()
    elif option==4:
        option4()

