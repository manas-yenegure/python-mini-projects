# 🔐 Caesar Cipher - Python

A simple **Caesar Cipher Encryption and Decryption** program built with Python. This project allows users to encrypt and decrypt messages by shifting letters in the alphabet while keeping numbers, spaces, and special characters unchanged.

## Features

- Encrypt text using the Caesar Cipher algorithm
- Decrypt encrypted messages
- Supports any shift value (automatically wraps around the alphabet)
- Preserves numbers, spaces, and special characters
- Run multiple encryptions/decryptions without restarting the program
- Handles invalid menu choices

## Technologies Used

- Python 3

## Project Structure

```
Caesar-Cipher/
│
├── main.py
└── README.md
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/Caesar-Cipher.git
```

2. Navigate to the project folder:

```bash
cd Caesar-Cipher
```

3. Run the program:

```bash
python main.py
```

## Example

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode

Type your message:
hello world!

Type the shift number:
5

Here is the encoded result: mjqqt btwqi!

Type 'yes' if you want to go again. Otherwise type 'no':
yes
```

## How It Works

The Caesar Cipher is one of the oldest encryption techniques. Each letter in the message is shifted by a fixed number of positions in the alphabet.

Example with a shift of **3**:

```
Original: abcxyz
Encoded : defabc
```

For decoding, the program shifts the letters in the opposite direction.

## Learning Outcomes

This project helped me practice:

- Functions
- Loops
- Conditional Statements
- Lists
- String Manipulation
- Modulo Operator (`%`)
- User Input Handling
- Basic Cryptography Concepts

## Future Improvements

- Add uppercase letter support
- Random key generation
- File encryption and decryption
- Graphical User Interface (GUI)
- Support for multiple encryption algorithms

## 👨‍💻 Author

**Manas Yenegure**

## ⭐ If you found this project useful, consider giving it a Star!