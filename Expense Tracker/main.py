import csv
import os

#create csv fie if it doen't exits

if not os.path.isfile("expenses.csv"):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

    print("expenses.csv created successfully!")

#Set Daily Budget

budget = float(input("Enter Today's Budget:"))

#Add Expenses

def add_expense():
    date = input("Enter Date(DD-MM-YYYY):")
    category = input("Enter Category:")
    amount = float(input("Enter Amount:"))

    with open("expenses.csv","a",newline="")as file:
        writer=csv.writer(file)
        writer.writerow([date,category,amount])

    print("\nExpense Added Successfully! \n")

#view Expenses

def view_expenses():
    print("\n----------Expense List---------")
    with open("expenses.csv","r") as file:
        reader=csv.reader(file)

        for row in reader:
            print("{:<15}{:<15}{:<10}".format(row[0],row[1],row[2]))
    print()

#Dispaly End Day Summary

def end_day_summary():
    total_expense = 0

    with open("expenses.csv","r") as file:
        reader = csv.reader(file)

        next(reader) 

        for row in reader:
            total_expense+= float(row[2]) 

    remaining = budget-total_expense

    print("\n===========Today's Summary===========") 

    print(f"Budget:{budget}")
    print(f"Total Expenses:{total_expense}")

    if remaining >= 0:
        print(f"Remaining Money:{remaining}")
        print(f"Todays's savings:{remaining}")
        print("\n Great! You Stayed Within your Budget.")

    else:
        print("Remaining Money:0")
        print(f"Overspent By:{-remaining}") 
        print("\n You Spent More than your budget toady.")

    print()

while True:

    print("===========Expenses Tracker============")
    print("1.Add Expense")
    print("2.View Expense")
    print("3.End Day Summary")
    print("4.Exit")

    choice = input("\n Enter Your Choice:") 

    if choice== "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        end_day_summary()

    elif choice == "4":
        print("\nThank You for Using Expense Tracker")
        break

    else:
        print("\nInvaild Choice! Please Try again.\n") 