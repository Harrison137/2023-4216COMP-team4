import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')

def option1():
    df['Order Date'] = pd.to_datetime(df['Order Date']).dt.strftime('%Y')
    


def options():
    print("[0] To leave")
    print("[1] Option 18: Show sales vs profit")
#Running code
while True:
    options()
    option = int(input())
    if option == 0:
        break
    elif option == 1:
        option1()

