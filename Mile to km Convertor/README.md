# Mile to Kilometer Converter

A simple **GUI-based Mile to Kilometer Converter** built using **Python and Tkinter**.
The application allows users to enter a distance in miles and instantly convert it into kilometers.

## Project Overview

The **Mile to Kilometer Converter** is a beginner-friendly Python project designed to practice **Tkinter GUI development**, user input handling, functions, and basic mathematical calculations.

The conversion is performed using the standard conversion factor:

**1 Mile = 1.60934 Kilometers**

## Features

* Simple and clean graphical user interface
* Accepts distance in miles as user input
* Converts miles into kilometers
* Displays the result up to 2 decimal places
* Button-based calculation
* Built entirely with Python's built-in Tkinter library

## Technologies Used

* **Python 3**
* **Tkinter** — GUI development
* **Python Functions**
* **Basic Arithmetic Operations**

## How It Works

1. The user enters a value in miles.
2. The program reads the value using Tkinter's `Entry` widget.
3. The `convert()` function is called when the **Calculate** button is clicked.
4. The entered miles are multiplied by `1.60934`.
5. The converted value is displayed in kilometers.

### Conversion Formula

```text
Kilometers = Miles × 1.60934
```

### Example

```text
Input: 10 miles

10 × 1.60934 = 16.09 km
```

## Getting Started

### Prerequisites

Make sure **Python 3** is installed on your computer.

You can check your Python version with:

```bash
python --version
```

Tkinter usually comes bundled with standard Python installations.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/manas-yenegure/mile-to-kilometer-converter.git
```

2. Navigate to the project directory:

```bash
cd mile-to-kilometer-converter
```

3. Run the Python program:

```bash
python main.py
```

## Usage

1. Launch the application.
2. Enter the number of miles in the input field.
3. Click the **Calculate** button.
4. The equivalent distance in kilometers will appear beside **Kilometers**.

## Project Structure

```text
Mile-to-Kilometer-Converter/
│
├── main.py
└── README.md
```

## Concepts Practiced

This project helped practice:

* Importing Tkinter
* Creating a GUI window
* Using `Label`, `Entry`, and `Button` widgets
* Tkinter `grid()` layout manager
* Getting user input with `.get()`
* Updating widgets using `.config()`
* Creating and calling functions
* Type conversion using `float()`
* F-string formatting
* Basic mathematical calculations
* Running a Tkinter application with `mainloop()`

## Learning Outcome

By completing this project, I practiced building a basic desktop GUI application with Python and learned how to connect **user input → Python logic → GUI output**.

## Future Improvements

Possible improvements for future versions:

* Add **Miles → Kilometers** and **Kilometers → Miles** modes
* Add input validation for invalid values
* Add a **Clear** button
* Add keyboard shortcuts
* Improve the GUI design
* Add more unit conversions such as meters, feet, and yards
* Add dark/light mode

## 👨‍💻 Author

**Manas Yenegure**