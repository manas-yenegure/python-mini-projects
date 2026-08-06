# Python Number Guessing Game

A simple command-line Number Guessing Game built with Python. The computer randomly selects a number between **1 and 100**, and the player must guess it before running out of attempts.

This project was created as part of my Python learning journey to practice functions, loops, conditional statements, and random number generation.

## Features

- Random number generated between **1 and 100**
- Two difficulty levels:
  - **Easy** – 10 attempts
  - **Hard** – 5 attempts
- Remaining attempts displayed after each guess
- Feedback if the guess is **Too High**
- Feedback if the guess is **Too Low**
- Winning and losing conditions

## Project Structure

```
python-number-guessing-game/
│
├── main.py
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/manas-yenegure/python-number-guessing-game.git
```

### 2. Navigate to the project folder

```bash
cd python-number-guessing-game
```

### 3. Run the program

```bash
python main.py
```

## Example Gameplay

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Choose a difficulty:
Type 'easy' or 'hard': easy

You have 10 attempts remaining.
Make a guess: 50

Too High.
Guess again.

You have 9 attempts remaining.
Make a guess: 25

Too Low.
Guess again.

...

You got it! The answer was 37.
```

## Technologies Used

- Python 3
- Random Module (`random.randint`)

## Concepts Practiced

- Functions
- While Loops
- Conditional Statements
- User Input
- Variables
- Constants
- Random Number Generation
- Game Logic

## Future Improvements

- Remove the answer preview (currently shown for testing).
- Add input validation.
- Add a replay option.
- Track the player's best score.
- Add multiple difficulty levels.
- Create a GUI version using Tkinter.
- Add colorful terminal output.

## Author

**Manas Yenegure**

If you found this project helpful, consider giving it a ⭐ on GitHub!
