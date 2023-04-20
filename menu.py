import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')

populations = {
    'California': 39538223,
    'New York': 19530351,
    'Texas': 29145505,
    'Washington': 7693612,
    'Pennsylvania': 13002700,
    'Florida': 21538187,
    'Illinois': 12812508,
    'Ohio': 11799448,
    'Michigan': 10077331,
    'Virginia': 8626207,
    'North Carolina': 10611862,
    'Indiana': 6745354,
    'Georgia': 10711908,
    'Kentucky': 4499692,
    'New Jersey': 9288994,
    'Arizona': 7278717,
    'Wisconsin': 5851754,
    'Colorado': 5845526,
    'Tennessee': 6910840,
    'Minnesota': 5706494,
    'Massachusetts': 7029917,
    'Delaware': 989948,
    'Maryland': 6177224,
    'Rhode Island': 1098164,
    'Missouri': 6154913,
    'Oklahoma': 3980783,
    'Alabama': 5024279,
    'Oregon': 4217737,
    'Nevada': 3104614,
    'Connecticut': 3605944,
    'Arkansas': 3011524,
    'Utah': 3271616,
    'Mississippi': 2961279,
    'Louisiana': 4648794,
    'Vermont': 643077,
    'South Carolina': 5118425,
    'Nebraska': 1961504,
    'New Hampshire': 1377529,
    'Montana': 1085407,
    'New Mexico': 2117522,
    'Iowa': 3192406,
    'Idaho': 1826156,
    'Kansas': 2937880,
    'District of Columbia': 689545,
    'Wyoming': 576851,
    'South Dakota': 886667,
    'Maine': 1362359,
    'West Virginia': 1793716,
    'North Dakota': 779094
}


def option1():
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


def option2():
    #a heatmap to show the total profit per month per year
    #converts the date into date and time format
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
    #gets the year in a data frame
    df['Year'] = df['Order Date'].dt.year
    #gets the month in a data frame
    df['Month'] = df['Order Date'].dt.month
    #groups together the year and month with the sum of the profit
    yearAndMonth = df.groupby(['Month', 'Year'])['Profit'].sum().unstack()
    print(yearAndMonth)
    #creates a heat map and plots the data on
    sns.heatmap(yearAndMonth, cmap='afmhot')
    plt.title('Profit per Month and Year')
    plt.xlabel('Year')
    plt.ylabel('Month')

    plt.show()
    print (yearAndMonth)

def option3():
    # a line chart to show total sales compared to total profit through every order day
    # converts order date into a date time format allowing it to be correctly formatted
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
    #gets the sum of the total profit per day
    profitPerDay = df.groupby('Order Date') ['Profit'].sum()
    #gets the sum of the total sales per day
    salesPerDay = df.groupby('Order Date') ['Sales'].sum()

    print (salesPerDay)
    print (profitPerDay)
    #creates a line chart to have lines for sales and profit against the order date
    #plt.plot(df['Sales'].sum(), df.index, label='Sales')
    plt.plot(profitPerDay, label='profit')
    plt.plot(salesPerDay, label='sales')
    plt.title('Total Profit Per Day')
    plt.xlabel('Order Date')
    plt.ylabel('Pounds (£)')
    plt.legend()
    plt.show()

def options():
    print("[0] To leave")
    print("[1] Option 2: Average sales per segment")
    print("[2] Option 2: Highest months per year of profit")
    print("[3] Option 3: Total Sales Compared to Profit Per Day")


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
   