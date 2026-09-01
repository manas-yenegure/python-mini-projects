# Flash Card — French Vocabulary Flashcards

A simple **French-to-English flashcard learning application** built with Python, Tkinter, and Pandas.

The app displays a French word on a flashcard and automatically flips the card after **3 seconds** to reveal its English meaning. If you know the word, you can mark it as known, and it will be removed from future practice sessions.

## Features

* Displays French vocabulary words
* Reveals the English translation automatically
* Automatically flips the card after 3 seconds
* Randomly selects flashcards
* Removes words that you already know
* Allows you to skip words you don't know
* Saves remaining words for future learning sessions
* Simple graphical interface using Tkinter

## Technologies Used

* **Python**
* **Tkinter** — Graphical User Interface
* **Pandas** — Reading and managing CSV data
* **Random** — Random flashcard selection

---

## Project Structure

```text
Flashy/
│
├── main.py
│
├── data/
│   ├── french_words.csv
│   
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
└── README.md
```

## Vocabulary Data

The vocabulary file contains two columns:

| Column    | Description            |
| --------- | ---------------------- |
| `French`  | French vocabulary word |
| `English` | English translation    |

The provided vocabulary dataset contains **101 French-English word pairs**.

---

## How It Works

### 1. Load Vocabulary

When the application starts, it first tries to load the previously generated `words_to_learn.csv`.

If that file doesn't exist, it loads the original `french_words.csv` file instead.

### 2. Display a Random Card

A random word is selected from the available vocabulary and displayed on the front of the card.

### 3. Flip the Card

After **3 seconds**, the flashcard automatically flips and displays the English translation.

### 4. Mark the Word

There are two options:

* ❌ **Unknown** — Move to another card without removing the current word.
* ✅ **Known** — Remove the word from the learning list.

When a word is marked as known, the updated list is saved to `words_to_learn.csv`.

## How to Run

### Prerequisites

Make sure Python is installed on your computer.

Install Pandas if you don't already have it:

```bash
pip install pandas
```

Tkinter is usually included with standard Python installations.

### Run the Application

Clone or download the project and make sure the folder structure is maintained.

Then run:

```bash
python main.py
```

## How to Use

1. Start the application.
2. A French word appears on the flashcard.
3. Try to remember its English meaning.
4. Wait 3 seconds.
5. The card flips and shows the English translation.
6. Click:

   * ❌ if you didn't know the word.
   * ✅ if you knew the word.
7. Continue practicing until you have learned the vocabulary.

## Progress Tracking

The application automatically creates/updates:

```text
data/words_to_learn.csv
```

When you click the **known (✅)** button, the current word is removed from the learning list and the remaining words are saved.

This means your progress is preserved between sessions.

## User Interface

The application uses Tkinter's `Canvas`, `Button`, and `PhotoImage` components to create the flashcard interface.

The flashcard includes:

* French card front
* English card back
* Vocabulary text
* ❌ Unknown button
* ✅ Known button

## Learning Concept

This project demonstrates the basic concept of **active recall using flashcards**.

Instead of immediately showing the translation, the application gives you a few seconds to recall the English meaning before revealing the answer.

## Possible Improvements

Some possible future improvements include:

* Add more languages
* Allow users to choose the flip duration
* Add pronunciation/audio
* Track learning statistics
* Add difficulty levels
* Add a progress bar
* Add a restart/reset progress option
* Add a custom vocabulary import feature
* Add spaced-repetition scheduling
* Display daily learning goals

## Author

**Manas Yenegure**

Built as a Python GUI project for practicing vocabulary and learning how to work with **Tkinter, Pandas, CSV files, functions, and event-driven programming**.

## License

This project is open for educational and personal use.
