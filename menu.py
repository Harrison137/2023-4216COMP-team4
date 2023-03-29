import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')

def option1():
    #bar chart to display average sales per region
    df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')
    #calculate the average sales per region
    avg_sales = df.groupby('Region')['Quantity'].mean()

    #plot the results as a bar chart
    avg_sales.plot(kind='bar')
    plt.title('Average Sales per Region')
    plt.xlabel('Region')
    plt.ylabel('Average Sales')
    plt.show()

def option2():
    #the average profit per segment
    df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')
    #calculate the average profit per segment
    avgSegmentProfit = df.groupby('Segment')['Profit'].mean()
    avgSegProfit = pd.DataFrame(avgSegmentProfit)
    print (avgSegProfit)
    #creates pie chart for the data
    avgSegProfit.plot(kind='pie', subplots = True, colors=['r', 'g', 'b'], autopct='%.2f', fontsize=20)
    plt.title('Average Profit Per Segment')
    plt.ylabel('Profit')
    plt.show()

def option3():
    # Top 5 products by sales
    top_sales = df.groupby('Product Name').agg({'Sales': 'sum', 'Profit': 'sum'}).sort_values('Sales', ascending=False).head(5)
    print("\nTop 5 products by sales:")
    for index, row in top_sales.iterrows():
        print(f"{index}, Total sales = ${row['Sales']:.2f}, Total Profit = ${row['Profit']:.2f}")
    print()

    # Bottom 5 products by sales
    bottom_sales = df.groupby('Product Name').agg({'Sales': 'sum', 'Profit': 'sum'}).sort_values('Sales').head(5)
    print("Bottom 5 products by sales:")
    for index, row in bottom_sales.iterrows():
        print(f"{index}, Total sales = ${row['Sales']:.2f}, Total Profit = ${row['Profit']:.2f}")
    print()

    # Top 5 products by profit
    top_profit = df.groupby('Product Name').agg({'Sales': 'sum', 'Profit': 'sum'}).sort_values('Profit', ascending=False).head(5)
    print("Top 5 products by profit:")
    for index, row in top_profit.iterrows():
        print(f"{index}, Total sales = ${row['Sales']:.2f}, Total Profit = ${row['Profit']:.2f}")
    print()

    # Bottom 5 products by profit
    bottom_profit = df.groupby('Product Name').agg({'Sales': 'sum', 'Profit': 'sum'}).sort_values('Profit').head(5)
    print("Bottom 5 products by profit:")
    for index, row in bottom_profit.iterrows():
        print(f"{index}, Total sales = ${row['Sales']:.2f}, Total Profit = ${row['Profit']:.2f}")
    print()
    
def option4():
    # Calculate the number of products available
    num_products = df['Product ID'].nunique()

    # Calculate the average sale price and profit per product
    avg_sale_price = df['Sales'].mean()
    avg_profit = df['Profit'].mean()

    # Print the results
    print("\nAverage Product Sales Information:")
    print("Number of Products Available:", num_products)
    print("Average Sale price per Product: ${:.2f}".format(avg_sale_price))
    print("Average Profit per Product: ${:.2f}\n".format(avg_profit))

def option5():
    # group the data by category and calculate total sales and profit
    category_group = df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'})

    # print the total sales and profit for each category
    print('\nTotal sales and profit for each product category:')
    for index, row in category_group.iterrows():
        category_name = index
        total_sales = '${:,.2f}'.format(row['Sales'])
        total_profit = '${:,.2f}'.format(row['Profit'])
        print(f'{category_name}: Total sales = {total_sales}, Total profit = {total_profit}')
    print("")

def options():
    print("[0] To leave")
    print("[1] Option 1")
    print("[2] Option 2")
    print("[3] Option 3: Top and Bottom performing Products")
    print("[4] Option 4: Average Product Sales Information")
    print("[5] Option 5: Total Sales and Profits by Category")
    


while True:
    options()
    option = int(input())
    if option == 0:
        break
    elif option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5: 
        option5()