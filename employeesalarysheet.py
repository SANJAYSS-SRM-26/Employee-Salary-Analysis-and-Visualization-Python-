import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("C:\\Users\\sanja\\OneDrive\\Documents\\EMPLOYEE.CSV")

name = df["NAME OF EMPLOYEE"]
total = df["TOTAL"]

def mainmenu():
    print("-- MAIN MENU --")
    print("1. Display DataFrame")
    print("2. Data Analysis")
    print("3. Visualizing the Data")
    print("4. Exit")
    
    ch = int(input("Enter your required choice: "))
    
    while ch != 4:
        if ch == 1:
            DataFrame()
        elif ch == 2:
            DataAnalysis()
        elif ch == 3:
            graphs()
        else:
            print("Invalid choice")
        ch = int(input("\nEnter your required choice: "))

def DataFrame():
    print(df)

def DataAnalysis():
    print("-- DATA ANALYSIS MENU --")
    print("1. Min Salary")
    print("2. Max Salary")
    print("3. Sum of Salaries")
    
    cha = int(input("Enter your required choice: "))
    
    while cha != 4:
        if cha == 1:
            Min()
        elif cha == 2:
            Max()
        elif cha == 3:
            Am()
        else:
            print("Invalid choice")
        cha = int(input("\nEnter your required choice: "))

def Max():
    print("Maximum salary among employees:")
    print(df["TOTAL"].max())

def Min():
    print("Minimum salary among employees:")
    print(df["TOTAL"].min())

def Am():
    print("Sum of salaries:")
    print(df["TOTAL"].sum())

def graphs():
    print("-- GRAPHS --")
    print("1. Line Graph")
    print("2. Vertical Bar Graph")
    print("3. Exit")
    
    chg = int(input("Enter your required choice: "))
    
    while chg != 3:
        if chg == 1:
            line()
        elif chg == 2:
            barvertical()
        else:
            print("Invalid choice")
        chg = int(input("\nEnter your required choice: "))

def line():
    plt.plot(name, total, color="r", linewidth=7)
    plt.xlabel("NAME")
    plt.ylabel("TOTAL")
    plt.title("EMPLOYEE SALARY SHEET")
    plt.show()

def barvertical():
    plt.bar(name, total, linewidth=4)
    plt.xlabel("NAME")
    plt.ylabel("TOTAL")
    plt.title("EMPLOYEE SALARY SHEET")
    plt.xticks(rotation=90)
    plt.show()

mainmenu()
