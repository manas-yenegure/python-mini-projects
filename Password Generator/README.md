# 🔐 PyPassword Generator

A simple Python project that generates a random password based on the number of letters, symbols, and numbers specified by the user. This project demonstrates the use of Python's `random` module, loops, user input, and string manipulation.

> **Note:** This version generates a password by placing all letters first, followed by symbols, and then numbers. It is intended as a beginner learning project.

## Features

- Generate a custom password based on user input.
- Supports:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special symbols (!, #, $, %, &, (, ), *, +)
- Easy to understand and beginner-friendly code.
- Uses Python's built-in `random` module.

## Technologies Used

- Python 3.x
- `random` module

## Project Structure

```
PyPassword-Generator/
│
├── main.py        # Main Python program
└── README.md      # Project documentation
```

##  Getting Started

### Prerequisites

- Python 3.x installed on your computer.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/PyPassword-Generator.git
```

2. Navigate to the project folder:

```bash
cd PyPassword-Generator
```

3. Run the program:

```bash
python main.py
```

## Example Output

```text
Welcome to the PyPassword Generator!

How many letters would you like in your password?:
6

How many symbols would you like?:
2

How many numbers would you like?:
3

Generated Password:
AbdKmn!#527
```

## How It Works

1. The user enters:
   - Number of letters
   - Number of symbols
   - Number of numbers
2. The program randomly selects characters from predefined lists.
3. All selected characters are combined into a single password.
4. The generated password is displayed on the screen.

## Learning Concepts

This project helps beginners understand:

- Variables
- Lists
- Loops (`for`)
- User Input
- String Concatenation
- Random Number Generation
- Python Standard Library (`random`)

## Limitations

- Characters are **not shuffled** after generation.
- Password always follows this pattern:

```
Letters → Symbols → Numbers
```

For stronger security, the characters should be shuffled before displaying the final password.

## Future Improvements

- Shuffle the password characters for better randomness.
- Allow users to exclude confusing characters (e.g., O, 0, l, I).
- Copy password directly to clipboard.
- Add password strength indicator.
- Save generated passwords securely.
- Create a graphical user interface (GUI).
- Build a web version using Flask.

## Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it for educational and personal purposes.

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!