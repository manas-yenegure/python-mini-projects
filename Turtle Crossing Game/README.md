# Turtle Crossing Game

A simple **Turtle Crossing Game** built with Python's built-in `turtle` module. The player controls a turtle and must cross the road while avoiding moving cars.

Each time the turtle successfully reaches the finish line, the level increases and the cars move faster, making the game more challenging.

This project was created as part of my Python learning journey to practice **Object-Oriented Programming (OOP), classes, loops, collision detection, keyboard events, and the Turtle graphics library**.

## Features

* Player-controlled turtle
* Randomly generated moving cars
* Keyboard control using the **Up Arrow key**
* Collision detection between the player and cars
* Finish-line detection
* Level increases after successfully crossing the road
* Car speed increases with each level
* Scoreboard displaying the current level
* Game Over screen when the player hits a car

## How the Game Works

1. The turtle starts at the bottom of the screen.
2. Use the **Up Arrow** key to move the turtle forward.
3. Cars appear randomly on the road and move from right to left.
4. Avoid colliding with the cars.
5. Reach the finish line to complete the level.
6. After reaching the finish line:

   * The turtle returns to the starting position.
   * The car speed increases.
   * The level increases.
7. If the turtle collides with a car, the game ends.

The player movement, starting position, and finish-line detection are handled by the `Player` class.

## Technologies Used

* **Python 3**
* **Turtle Graphics**
* **Object-Oriented Programming (OOP)**
* **Random Module**
* **Time Module**

## Project Structure

```text
Turtle Crossing Game/
│
├── main.py
├── player.py
├── car_manager.py
└── scoreboard.py
```

### `main.py`

The main game file. It:

* Creates the game screen
* Creates the Player, CarManager, and Scoreboard objects
* Handles keyboard input
* Runs the main game loop
* Detects collisions
* Detects successful crossings
* Controls level progression

The game screen is configured as **600 × 600 pixels**, and the game loop updates the screen continuously.

### `player.py`

Contains the `Player` class, which manages the turtle character.

The player:

* Starts at `(0, -280)`
* Moves upward by 10 pixels
* Returns to the starting position after completing a level
* Detects when it reaches the finish line

### `car_manager.py`

Contains the `CarManager` class responsible for creating and moving cars.

Cars:

* Are created randomly
* Have randomly selected colors
* Start from the right side of the screen
* Move toward the left
* Become faster when the player reaches a new level

The initial car speed is `5`, and the speed increases by `10` for each new level.

### `scoreboard.py`

Contains the `Scoreboard` class.

It:

* Starts at Level 1
* Displays the current level
* Updates the level after successful crossings
* Displays **GAME OVER** when the player loses

## Controls

| Key         | Action              |
| ----------- | ------------------- |
| ⬆️ Up Arrow | Move Turtle Forward |

## Installation

Python's `turtle`, `random`, and `time` modules are used in this project, so no external packages are required.

Make sure Python 3 is installed on your computer.

## How to Run

1. Download or clone this project.
2. Open the project folder in your code editor or terminal.
3. Run the main file:

```bash
python main.py
```

4. Use the **Up Arrow** key to control the turtle.
5. Try to reach the finish line without hitting any cars.

## Game Logic

The main game loop continuously:

* Creates cars
* Moves cars
* Checks for collisions
* Checks whether the player reached the finish line
* Updates the level and car speed

Collision detection ends the game when the player's distance from a car is less than `20`.

When the player reaches the finish line, the turtle returns to the starting position, the car speed increases, and the scoreboard level is updated.

## Learning Outcomes

Through this project, I practiced:

* Python classes and objects
* Object-Oriented Programming
* Inheritance
* Turtle graphics
* Keyboard event handling
* Game loops
* Collision detection
* Random number generation
* Managing multiple objects
* Level progression
* Basic game development concepts

## Future Improvements

Some possible improvements include:

* Add left, right, and downward movement
* Add a lives system
* Add a high-score system
* Add sound effects
* Add different types of vehicles
* Add a start/restart screen
* Add increasing car spawn frequency
* Add background graphics
* Add difficulty modes

## Author
**Manas Yenegure**
