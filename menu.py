import pandas as pd
import matplotlib.pyplot as plt

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

def salesAndProfits():
    category_data = df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'})

    # create the bar chart
    fig, ax = plt.subplots()
    ax.bar(category_data.index, category_data['Sales'], label='Sales')
    ax.bar(category_data.index, category_data['Profit'], label='Profit')

    # add labels and title
    ax.set_xlabel('Category')
    ax.set_ylabel('Amount ($)')
    ax.set_title('Total Sales and Profit by Category')

    # rotate the x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right')

    # add legend
    ax.legend()

    # display the chart
    plt.show()

def plot_sales_per_capita(filename, populations):
    # Load the sales data from the CSV file using pandas
    sales_data = pd.read_csv(filename, encoding='iso-8859-1')

    # Calculate sales per capita and add it to the data
    sales_data['Sales per Capita'] = sales_data['Sales'] / sales_data['State'].map(populations)

    # Sort the data by sales per capita
    sales_data = sales_data.sort_values(by='Sales per Capita', ascending=False)

    # Plot the sales per capita data as a bar chart
    plt.bar(sales_data['State'], sales_data['Sales per Capita'])
    
    # Rotate the x-axis labels by 90 degrees to make them more readable
    plt.xticks(rotation=90)

    # Add labels and title to the chart
    plt.xlabel('State')
    plt.ylabel('Sales per Capita')
    plt.title('Sales per Capita by State')

    # Show the chart
    plt.show()

def options():
    print("[0] To leave")
    print("[1] Option 1: Average sales per region")
    print("[2] Option 2: Average sales per segment")


while True:
    options()
    option = int(input())
    if option == 0:
        break
    elif option == 1:
        salesAndProfits()
    elif option == 2:
        plot_sales_per_capita("Sample - Superstore.csv", populations)
    