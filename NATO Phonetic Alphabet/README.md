# NATO Phonetic Alphabet

A simple Python program that converts the letters of a word into their corresponding **NATO Phonetic Alphabet** codes.

For example, entering `HELLO` produces:

```text
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

This project was created as part of my Python learning journey to practice **Pandas, CSV files, dictionaries, functions, list comprehension, exception handling, and user input**.

## Features

* Converts words into NATO Phonetic Alphabet codes
* Reads phonetic alphabet data from a CSV file
* Uses a dictionary for quick letter-to-code conversion
* Handles invalid characters using exception handling
* Accepts user input from the command line

## Technologies Used

* **Python**
* **Pandas**
* **CSV**

## Project Structure

```text
NATO-Phonetic-Alphabet/
│
├── main(7).py
├── nato_phonetic_alphabet.csv
└── README.md
```

## How It Works

1. The program reads the `nato_phonetic_alphabet.csv` file using Pandas.
2. The CSV data is converted into a Python dictionary.
3. The user enters a word.
4. Each letter is converted to uppercase.
5. The program finds the corresponding NATO phonetic code for each letter.
6. The phonetic codes are displayed as a list.

## Example

**Input:**

```text
Enter a word: PYTHON
```

**Output:**

```text
['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
```

## Error Handling

If the user enters a character that is not a letter of the alphabet, the program displays:

```text
Sorry, only letters in the alphabet please.
```

The program then asks for another word.

## Concepts Practiced

* Reading CSV files
* Pandas DataFrames
* Dictionaries
* Functions
* User input
* `try-except-else`
* `KeyError` handling
* List comprehension
* String methods
* Iterating through data

## How to Run

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Folder

```bash
cd NATO-Phonetic-Alphabet
```

### 3. Install Pandas

```bash
pip install pandas
```

### 4. Run the Program

```bash
python "main(7).py"
```

## Requirements

Make sure **Python** and **Pandas** are installed on your system.

## Learning Outcome

This project helped me understand how to work with **external CSV data**, convert data into a useful dictionary structure, and use **exception handling and list comprehension** to build a practical Python program.

## Author

**Manas Yenegure**
