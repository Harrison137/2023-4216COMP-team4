import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')

def option1():
    region_profit = df.groupby('Region')['Profit'].sum().reset_index()

    # Sort the data by profit in descending order
    region_profit = region_profit.sort_values('Profit', ascending=False)

    # Create a bar chart of the profit by region
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Region', y='Profit', data=region_profit, color='blue')
    plt.title('Total Profit by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Profit ($)')
    plt.show()

def option2():
    region_profit = df.groupby('Region')['Profit'].sum().reset_index()
    
    #This calculates the profit margin for each region by dividing total profit by total sales and multiplying by 100
    region_sales = df.groupby('Region')['Sales'].sum().reset_index()
    region_profit_margin = pd.merge(region_profit, region_sales, on='Region')
    region_profit_margin['Profit Margin'] = (region_profit_margin['Profit'] / region_profit_margin['Sales']) * 100
    region_profit_margin = region_profit_margin.sort_values('Profit Margin', ascending=False)

    #This creates a bar chart of the profit margin by region
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Region', y='Profit Margin', data=region_profit_margin, color='green')
    plt.title('Profit Margin by Region')
    plt.xlabel('Region')
    plt.ylabel('Profit Margin (%)')
    plt.show()

def option3():
    
    state_data = df.groupby('State')['Quantity'].sum()

    top_states = state_data.sort_values(ascending=False).head(10)

    #This creates a pie chart to display the data
    plt.pie(top_states.values, labels=top_states.index, autopct='%1.1f%%')
    plt.title('Quantity of items bought - Top 10 States')
    plt.show()


def options():
    print("[0] To leave")
    print("[1] Bar chart of profit by region")
    print("[2] Bar chart of profit margins for each region")
    print("[3] Show quantity of items bought as a pie chart for the top 10 states")


#running code
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
