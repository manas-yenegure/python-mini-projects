# Daily Expense Tracker

A simple **Command-Line Interface (CLI)** application built with **Python** to help users track their daily expenses, monitor their budget, and view their end-of-day savings.

This project was created as a Python mini project while learning Python fundamentals.

## Features

* Set a daily budget
* Add new expenses
* View all recorded expenses
* Display end-of-day summary
* Automatically create and store data in a CSV file
* Calculate:

  * Total Expenses
  * Remaining Budget
  * Daily Savings
  * Overspending (if any)

## 🛠️ Technologies Used

* Python 3
* CSV Module
* OS Module

## Project Structure

```text
Expense-Tracker/
│
├── main.py
├── expenses.csv
└── README.md
```

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/manas_yenegure/Expense-Tracker.git
```

2. Open the project folder.

3. Run the program:

```bash
python main.py
```

4. Enter your daily budget and start tracking your expenses.

## Menu

```text
====== Expense Tracker ======

1. Add Expense
2. View Expenses
3. End Day Summary
4. Exit
```

## Sample Output

```text
Enter Today's Budget: 1000

====== Expense Tracker ======

1. Add Expense
2. View Expenses
3. End Day Summary
4. Exit

Enter Your Choice: 1

Enter Date (DD-MM-YYYY): 02-08-2026
Enter Category: Food
Enter Amount : 250

Expense Added Successfully!
```

## End Day Summary

```text
========== Today's Summary ==========

Budget          : ₹1000
Total Expense   : ₹250
Remaining Money : ₹750
Today's Savings : ₹750

Great! You stayed within your budget.
```

## Concepts Practiced

* Functions
* Loops
* Conditional Statements (`if-elif-else`)
* File Handling
* CSV File Operations
* Modules
* User Input
* Basic Calculations

## Future Improvements

* Edit an expense
* Delete an expense
* Search expenses
* Filter by category
* Monthly summary
* Charts using Matplotlib
* Store data using SQLite
* GUI using Tkinter

## Author

**Manas Yenegure**
Feedback and suggestions are always welcome!
