# Snake Game

A simple **Snake Game** built with Python using the **Turtle graphics module**.

The player controls the snake using the arrow keys, collects food to increase the score, and tries to avoid hitting the walls or the snake's own tail.

This project was created as part of my **Python learning journey** to practice classes, functions, loops, keyboard controls, collision detection, and working with multiple Python files.

## Features

* Classic Snake gameplay
* Arrow-key controls
* Randomly placed food
* Snake grows after eating food
* Score increases with each food collected
* Wall collision detection
* Tail collision detection
* Game Over message
* Modular project structure

## Controls

| Key            | Movement   |
| -------------- | ---------- |
| ⬆️ Up Arrow    | Move Up    |
| ⬇️ Down Arrow  | Move Down  |
| ⬅️ Left Arrow  | Move Left  |
| ➡️ Right Arrow | Move Right |

## Project Structure

```text
Snake Game/
│
├── main.py
├── snake.py
├── food.py
└── scoreboard.py
```

### File Description

* **main.py** – Contains the main game loop, controls, and collision detection.
* **snake.py** – Creates the snake and handles its movement and direction.
* **food.py** – Creates the food and places it at random positions.
* **scoreboard.py** – Displays and updates the player's score and Game Over message.

The snake is initially created with three segments and moves continuously across the screen.

## How It Works

1. The game starts with a snake consisting of three segments.
2. The snake moves continuously in the selected direction.
3. Food appears at a random position on the screen.
4. When the snake eats the food:

   * The food moves to a new position.
   * The snake grows.
   * The score increases.
5. The game ends when the snake:

   * Hits the wall.
   * Hits its own tail.

## Technologies Used

* **Python**
* **Turtle Graphics**
* **Object-Oriented Programming**

## How to Run

### 1. Clone the Repository

```bash
git clone <https://github.com/manas-yenegure/python-mini-project>
```

### 2. Open the Project Folder

```bash
cd Snake-Game
```

### 3. Run the Game

```bash
python main.py
```

Make sure all four Python files are present in the same folder.

## What I Learned

Through this project, I practiced:

* Creating and using Python classes
* Working with objects
* Using functions and methods
* Handling keyboard events
* Using loops and conditional statements
* Detecting collisions
* Creating a game loop
* Splitting a project into multiple Python modules
* Using the `turtle` module

## Future Improvements

Possible improvements for the project:

* Add a high-score system
* Add different difficulty levels
* Increase the snake's speed as the score increases
* Add sound effects
* Add a restart option
* Add different types of food

## Author

**Manas Yenegure**

A Python project created while learning and practicing Python programming.

⭐ If you like this project, consider giving the repository a **star**!
