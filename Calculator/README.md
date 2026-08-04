# Python Calculator

A simple command-line calculator built with Python that performs basic arithmetic operations. The calculator allows users to continue calculations using the previous result or start a new calculation whenever they want.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Continue calculations with the previous answer
- Start a new calculation without restarting the program
- Built using Python functions and dictionaries

## Project Structure

```
Python-Calculator/
│
├── main.py          # Main calculator program
└── README.md        # Project documentation
```

## How It Works

1. Enter the first number.
2. Choose an arithmetic operation:
   - `+` Addition
   - `-` Subtraction
   - `*` Multiplication
   - `/` Division
3. Enter the second number.
4. View the result.
5. Choose whether to:
   - Continue calculating with the current result (`y`)
   - Start a new calculation (`n`)

## Example Output

```
What is the first number?
10

+
-
*
/

Pick an operation: *
What is the next number?
5

10.0 * 5.0 = 50.0

Type 'y' to continue calculating with 50.0,
or type 'n' to start a new calculation:
y

Pick an operation: +

What is the next number?
20

50.0 + 20.0 = 70.0
```

## Technologies Used

- Python 3
- Functions
- Dictionaries
- Loops
- User Input
- Conditional Statements

## Concepts Practiced

This project helped practice:

- Defining and calling functions
- Returning values from functions
- Dictionary mapping
- Function references
- While loops
- User interaction
- Program flow control
- Recursive function calls

## Learning Objectives

This project demonstrates how dictionaries can store functions as values, making it easy to call different operations dynamically based on user input. It also introduces building an interactive command-line application with reusable code.

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/manas-yenegure/Python-Calculator.git
```

2. Navigate to the project folder:

```bash
cd Python-Calculator
```

3. Run the program:

```bash
python main.py
```

## Future Improvements

- Add percentage (%) operation
- Add exponent (^) operation
- Support parentheses using expression evaluation
- Improve input validation
- Handle division by zero
- Display calculation history
- Add a graphical user interface (GUI) using Tkinter

## Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Open a Pull Request

## License

This project is open-source and available under the **MIT License**.

## Author

**Manas Yenegure**

If you found this project helpful, consider giving it a ⭐ on GitHub!
