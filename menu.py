import pandas as pd
import matplotlib.pyplot as plt

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


    


def options():
    print("[0] To leave")
    print("[1] Option 1")
    print("[2] Option 2")
    


while True:
    options()
    option = int(input())
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 0:
        break