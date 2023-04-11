import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

def option9():
    #Average discount rate compared to average sales
    avg_discount = df.groupby('Region')['Discount'].mean()
    avg_sales = df.groupby('Region')['Quantity'].mean()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    ax1.plot(avg_discount)
    ax1.set_title('Average Discount by Region')
    ax2.plot(avg_sales)
    ax2.set_title('Average Quantity by Region')
    plt.show()

def option10():
    #Average discount rate compared to average sales
    avg_discount = df.groupby('State')['Discount'].mean()
    avg_sales = df.groupby('State')['Quantity'].mean()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.plot(avg_discount)
    ax1.set_title('Average Discount by State')
    #The following 2 lines adjust the code so that the names of the states are flipped
    ax1.set_xticks(range(len(avg_discount)))
    ax1.set_xticklabels(avg_discount.index, rotation=90)
    ax2.plot(avg_sales)
    ax2.set_title('Average Sales by State')
    ax2.set_xticks(range(len(avg_sales)))
    ax2.set_xticklabels(avg_sales.index, rotation=90)
    plt.show()
    



    
    

def options():
    print("[0] To leave")
    print("[1] Option 1: Average sales per region")
    print("[8] Option 8: Total Sales by State with Populations")
    print("[9] Option 9: Average sales per region compared to average discount per region")
    print("[10] Option 10: Average sales per state compared to average discount per state")



while True:
    options()
    option = int(input())
    if option == 0:
        break
    elif option == 1:
        option1()

    elif option == 9: 
        option9()
    elif option == 10: 
        option10()
