# Higher or Lower Game

A simple **Python command-line game** where you compare two accounts and guess which one has more followers.

The game randomly selects accounts from a dataset, displays their information, and asks the player to choose **A** or **B**. The score increases for every correct answer and the game ends when the player makes a wrong guess.

## Features

* Randomly selects accounts from a dataset
* Displays account name, description, and country
* Compares follower counts between two accounts
* Interactive command-line gameplay
* Keeps track of the player's score
* Ends automatically when the player guesses incorrectly

## Technologies Used

* **Python 3**
* `random` module
* Python lists and dictionaries
* Functions
* Loops
* Conditional statements
* User input

## Project Structure

```text
Higher-Lower-Game/
│
├── main.py
├── game_data.py
└── README.md
```

### `main.py`

Contains the main game logic, including:

* Selecting random accounts
* Displaying account information
* Taking user guesses
* Comparing follower counts
* Calculating the score

### `game_data.py`

Contains the account dataset used by the game.

Example:

```python
data = [
    {
        "name": "Instagram",
        "description": "Social media platform",
        "country": "United States",
        "Follower_count": 600000000
    }
]
```

## 🎮 How to Play

1. Run `main.py`.
2. The game displays two accounts:

```text
Compare A: Instagram, a Social media platform, from United States
Against B: YouTube, a Video-sharing platform, from United States
```

3. Enter your guess:

```text
Who has more followers? Type 'A' or 'B':
```

4. If your answer is correct, your score increases:

```text
You're right! Current Score is 1
```

5. If your answer is incorrect, the game ends:

```text
Sorry, that's Wrong. Final Score: 1
```

## How the Program Works

### 1. Import the Dataset

```python
from game_data import data
```

The program imports the account information from `game_data.py`.

### 2. Select Random Accounts

```python
account_b = random.choice(data)
```

A random account is selected from the dataset.

During each round, the previous **B account becomes the new A account**, and a new B account is selected.

```python
account_a = account_b
account_b = random.choice(data)
```

### 3. Format Account Information

The `format_data()` function extracts the account's information and displays it in a readable format.

```python
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_descr}, from {account_country}"
```

### 4. Check the User's Answer

The `check_answer()` function compares the follower counts.

```python
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
```

It returns `True` when the player's guess is correct.

### 5. Keep Track of the Score

```python
score = 0
```

Every correct answer increases the score:

```python
score += 1
```

### 6. Continue Until the Player Loses

The game uses:

```python
game_should_continue = True
```

The `while` loop continues running until the player gives an incorrect answer.

## Important Code Fix

Make sure the follower-count dictionary key is written **consistently** in `game_data.py` and `main.py`.

Your current code contains:

```python
a_follower_count = account_a["Follower_count"]
b_follower_count = account_b["Followe_count"]
```

Notice that the second key is:

```text
Followe_count
```

while the first is:

```text
Follower_count
```

If your dataset uses `Follower_count`, the second line should also be:

```python
b_follower_count = account_b["Follower_count"]
```

Otherwise, Python will raise a `KeyError`.

## How to Run

Make sure Python is installed, then open the project directory in your terminal.

Run:

```bash
python main.py
```

## Concepts Practiced

This project is useful for practicing:

* Functions
* Parameters and return values
* Lists
* Dictionaries
* `random.choice()`
* `while` loops
* `if/else` conditions
* Boolean values
* User input
* String formatting
* Modular Python files

## Possible Improvements

Future versions could include:

* Add ASCII art/logo
* Display the actual follower counts after each round
* Add a high-score system
* Add a replay option
* Prevent duplicate account selection more robustly
* Add difficulty levels
* Save high scores to a file

## 👨‍💻 Author

**Manas Yenegure**

⭐ If you found this project useful, consider giving the repository a star!
