# Blackjack Game

A simple **command-line Blackjack (21) game** built using Python. Challenge the computer, draw cards strategically, and try to reach **21** without going over!

This project was created to practice Python programming concepts such as functions, loops, conditionals, lists, and the `random` module.

## Features

- Interactive command-line gameplay
- Random card dealing
- Ace automatically changes from **11** to **1** when needed
- Computer follows Blackjack rules (draws until score reaches 17)
- Detects Blackjack (21 with two cards)
- Play multiple rounds without restarting the program
- Displays final scores and winner

## Technologies Used

- Python 3
- Random Module

## Project Structure

```
Python-Blackjack-Game/
│
├── main.py
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/manas-yenegure/Python-Blackjack-Game.git
```

### 2. Navigate to the project folder

```bash
cd Python-Blackjack-Game
```

### 3. Run the program

```bash
python main.py
```

## How to Play

- You and the computer each receive **2 cards**.
- The computer reveals only its **first card**.
- Choose:
  - **y** → Draw another card
  - **n** → Keep your current hand
- The computer keeps drawing until its score reaches **17**.
- The player closest to **21** wins.
- Going over **21** results in a loss.
- A score of **21 with exactly two cards** is considered **Blackjack**.

## Card Values

| Card | Value |
|------|------:|
| Ace | 11 (or 1 if needed) |
| 2–10 | Face Value |
| Jack | 10 |
| Queen | 10 |
| King | 10 |

## Example Gameplay

```
Your cards: [10, 7]
Your score: 17
Computer's first card: 9

Type 'y' to get another card, 'n' to pass: n

============= Final Result =============

Your cards: [10, 7]
Your final score: 17

Computer cards: [9, 8]
Computer final score: 17

It's a Draw!
```

## Concepts Practiced

- Functions
- Lists
- Loops
- Conditional Statements
- Random Module
- Game Logic
- User Input
- Code Organization

## Future Improvements

- Use a full 52-card deck
- Prevent duplicate cards
- Add betting system
- Multiple players
- Difficulty levels
- Colorful terminal interface
- Card ASCII art
- Statistics (Wins/Losses)
- Save game history

## Contributing

Contributions, suggestions, and improvements are welcome!

Feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License.

## ⭐ Show Your Support

If you found this project helpful or enjoyed playing the game, consider giving it a ⭐ on GitHub!
