# U.S. States Game

A simple **Python Turtle-based quiz game** where the player tries to identify all **50 U.S. states** on a blank map of the United States.

The game displays a blank U.S. map and asks the player to enter state names. When a correct state is entered, its name is displayed at the appropriate location on the map.

## Features

* Interactive blank map of the United States
* 🇺🇸 Guess all **50 U.S. states**
* Correct state names are displayed on the map
* Shows the current score, such as `10/50 States Correct`
* Type **"Exit"** to quit the game
* Generates a `states_to_learn.csv` file containing the states that were not guessed
* Uses CSV data for state names and their map coordinates

## Technologies Used

* **Python**
* **Turtle** – for creating the interactive map and game interface
* **Pandas** – for reading and processing the state data from the CSV file

## Project Files

```text
U.S. States Game/
│
├── main.py
├── 50_states.csv
├── blank_states_img.gif
└── states_to_learn.csv
```

### File Description

* **`main.py`** – Contains the main game logic.
* **`50_states.csv`** – Contains the U.S. state names and their coordinates.
* **`blank_states_img.gif`** – Blank map used as the game background.
* **`states_to_learn.csv`** – Automatically created when the player exits and contains the states they missed.

## How to Run

### 1. Install Python
Make sure Python is installed on your computer.

### 2. Install Pandas
Open your terminal and run:

```bash
pip install pandas
```

### 3. Keep the Project Files Together
Make sure these files are in the same project folder:

```text
main.py
50_states.csv
blank_states_img.gif
```

### 4. Run the Game
```bash
python main.py
```

## How to Play

1.The blank map of the United States will appear.

2.Enter the name of a U.S. state in the input box.

3.If the answer is correct, the state name will appear on the map.

4.Continue guessing until you identify all 50 states.

5.Type **`Exit`** when you want to stop playing.

6.The game will create `states_to_learn.csv` with the states you missed.

## Learning Objectives

This project helps practice:

* Python loops
* Conditional statements
* Lists
* Functions and modules
* File handling with CSV
* Data processing using Pandas
* Turtle graphics
* Working with coordinates
* User input and interactive programs

## Future Improvements

Some possible improvements:

* Add a timer or time limit
* Add a final score screen
* Prevent duplicate guesses from increasing the score
* Add hints for difficult states
* Add different difficulty levels
* Improve the `states_to_learn.csv` output format

## Author

**Manas Yenegure**
