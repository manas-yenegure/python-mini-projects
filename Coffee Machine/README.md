# Coffee Machine

A simple **Python Coffee Machine Simulator** that allows users to order drinks, insert virtual coins, receive change, and manage coffee machine resources.

This project was created as a Python practice project to demonstrate **functions, dictionaries, loops, conditional statements, user input, resource management, and basic transaction processing**.

## Features

* Order **Espresso, Latte, or Cappuccino**
* Accepts virtual coins:

  * Quarters
  * Dimes
  * Nickels
  * Pennies
* Calculates the total amount inserted
* Calculates and returns change
* Validates whether the payment is sufficient
* Checks whether enough ingredients are available
* Deducts ingredients after a successful purchase
* Provides a machine **report** showing:

  * Remaining water
  * Remaining milk
  * Remaining coffee
  * Total money earned
  *`off` command to shut down the coffee machine

## Available Drinks

| Drink      |  Water |   Milk | Coffee |  Cost |
| ---------- | -----: | -----: | -----: | ----: |
| Espresso   |  50 ml |      — |   18 g | $1.50 |
| Latte      | 200 ml | 150 ml |   24 g | $2.50 |
| Cappuccino | 250 ml | 100 ml |   24 g | $3.00 |

## How It Works

### 1.Select a Drink

When the program starts, you can choose:

```text
What would you like? (espresso/latte/cappuccino):
```

Enter one of the available drink names.

### 2.Resource Check

Before accepting payment, the machine checks whether it has enough ingredients to prepare the selected drink.

For example, if there isn't enough water:

```text
Sorry there is not enough water.
```

The transaction will not continue if the required resources are unavailable.

### 3.Insert Coins

If enough resources are available, the machine asks for coins:

```text
Please insert coins
How Many Quarters?:
How many Dimes?:
How many Nickels?:
How many cents?:
```

The program calculates the total value of the inserted coins.

### 4.Payment Validation

The machine checks whether the inserted amount is enough to purchase the drink.

If the customer pays too little:

```text
Sorry that's not enough Money. Money Refunded.
```

If the payment is sufficient, the machine calculates the change:

```text
Here is $0.50 in change
```

The drink's cost is then added to the machine's total profit.

### 5.Prepare the Coffee

After a successful payment, the required ingredients are deducted from the machine's resources.

The machine then displays:

```text
Here is your latte. Enjoy!
```

## Machine Report

The **`report` command** allows you to check the current status of the coffee machine.

Enter:

```text
report
```

The machine displays the remaining resources and total money earned:

```text
water:250ml
Milk:50ml
Coffee:76g
Money:$2.5
```

The report helps the operator monitor:

* Remaining water
* Remaining milk
* Remaining coffee
* Total money earned

The report is especially useful for checking the machine's resources after multiple coffee orders.

## Turn Off the Machine

To stop the program, enter:

```text
off
```

The coffee machine will shut down.

## Project Structure

```text
Coffee-Machine/
│
├── main.py
└── README.md
```

## How to Run

### Prerequisites

Make sure **Python 3.x** is installed on your computer.

Check your Python version:

```bash
python --version
```

### Run the Program

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd Coffee-Machine
```

Run the program:

```bash
python main.py
```

## Python Concepts Practiced

This project demonstrates several fundamental Python concepts:

* Variables
* Dictionaries
* Nested dictionaries
* Functions
* `for` loops
* `while` loops
* `if / elif / else`
* User input
* String formatting (f-strings)
* Global variables
* Boolean values
* Arithmetic operations
* Resource management
* Basic transaction processing

## Example Workflow

```text
What would you like? (espresso/latte/cappuccino): latte

Please insert coins
How Many Quarters?: 10
How many Dimes?: 0
How many Nickels?: 0
How many cents?: 0

Here is $0.00 in change
Here is your latte. Enjoy!
```

Checking the machine afterward:

```text
What would you like? (espresso/latte/cappuccino): report

water:100ml
Milk:50ml
Coffee:76g
Money:$2.5
```

## Future Improvements

Possible improvements for future versions:

* Add more coffee varieties
* Improve input validation for invalid drink names
* Handle invalid/non-numeric coin input
* Add a refill resources feature
* Add a graphical user interface (GUI)
* Add an administrator mode for machine management
* Store sales history
* Add daily sales reports

## Author

**Manas Yenegure**
