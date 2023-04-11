import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')

def option1():
    region_profit = df.groupby('Region')['Profit'].sum().reset_index()

    #Sorts the data by profit in descending order
    region_profit = region_profit.sort_values('Profit', ascending=False)

    #Creates a bar chart of the profit by region
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

def option4():
    
    #Create a pivot table using profit and category and then plot the pivot table as a bar chart and sort the data in descending order
    pivot_table = pd.pivot_table(df, values='Profit', index='Sub-Category', aggfunc='sum').sort_values(by='Profit', ascending=False)
    
    #Use 'barh' to rotate the graph rather than using 'bar'
    ax = pivot_table.plot(kind='barh')

    #Set the title and axes and display the plot
    plt.title('Total Profit by Sub category')
    plt.xlabel('Profit($)')
    plt.ylabel('Sub Category')
    
    #Add annotations to each bar
    for i, v in enumerate(pivot_table['Profit']):
        ax.annotate('$' + str(round(v, 2)), xy=(v, i), va='center')
    
    plt.show()
    
def option5():
    #Calculates the total profit for each ship mode and then the percentage for each ship mode
    total_profit = df.groupby('Ship Mode')['Profit'].sum()
    percent_profit = total_profit / total_profit.sum() * 100

    #Plots the percentage of total profit for each ship mode as a pie chart and set the plot title
    ax = percent_profit.plot(kind='pie', autopct='%.2f%%', textprops={'fontsize': 12})
    ax.set_title('Percentage of Total Profit by Ship Mode')

    plt.show()

def options():
    print("[0] To leave")
    print("[1] Bar chart of profit by region")
    print("[2] Bar chart of profit margins for each region")
    print("[3] Show quantity of items bought as a pie chart for the top 10 states")
    print("[4] Chart that shows the profits for each sub category")
    print("[5] pie chart that shows which shipping mode takes in the most profit")


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
    elif option == 4:
        option4()
    elif option == 5:
        option5()
