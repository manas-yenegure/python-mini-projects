# Arcade Game

A simple **Arcade Game** built with Python using the built-in **Turtle Graphics** library.

The game features two paddles, a bouncing ball, collision detection, and a scoreboard. Two players can control their paddles and compete to score points.

This project was created as part of my Python learning journey to practice **Object-Oriented Programming, classes, functions, keyboard controls, collision detection, and game loops**.

## Features

* Two-player Pong game
* Player-controlled paddles
* Ball movement and bouncing
* Collision detection with walls and paddles
* Automatic score tracking
* Ball speed increases after paddle collisions
* Simple black-and-white game interface
* Clean separation of game components using Python classes

## Controls

### Left Paddle

* **W** → Move Up
* **S** → Move Down

### Right Paddle

* **↑ Arrow** → Move Up
* **↓ Arrow** → Move Down

## Technology Used

* **Python**
* **Turtle Graphics**
* **Tkinter**
* **Object-Oriented Programming (OOP)**

## Project Structure

```text
Pong Game/
│
├── main.py
├── ball.py
├── paddle.py
├── scoreboard.py
└── README.md
```

### `main.py`

Contains the main game loop, screen setup, keyboard controls, collision detection, scoring logic, and game execution.

### `ball.py`

Handles the ball's appearance, movement, bouncing, speed, and reset position. The ball starts with equal X and Y movement and reverses direction when it hits a wall or paddle.

### `paddle.py`

Defines the paddle class and handles paddle positioning and movement.

### `scoreboard.py`

Manages both players' scores and displays them on the game screen.

## How to Run

1. Make sure **Python** is installed on your computer.
2. Download or clone this project.
3. Open the project folder in your code editor or terminal.
4. Run:

```bash
python main.py
```

5. Use the keyboard controls to play.

## Game Logic

The game continuously updates the screen and moves the ball inside a game loop. The ball bounces when it reaches the top or bottom boundaries and changes direction when it collides with a paddle.

When a player misses the ball, the ball returns to the center and the opponent receives a point.

The ball also becomes faster after successful paddle collisions, making the game progressively more challenging.

## Learning Outcomes

Through this project, I practiced:

* Python Classes and Objects
* Object-Oriented Programming
* Functions and Methods
* Inheritance
* Turtle Graphics
* Keyboard Event Handling
* Game Loops
* Collision Detection
* Score Management
* Basic Game Development Logic

## Future Improvements

* Add a winning score limit
* Add a start/restart screen
* Add sound effects
* Add different difficulty levels
* Add pause functionality
* Add better collision detection
* Add a single-player mode with AI
* Improve the game interface

## Author

**Manas Yenegure**

A Python project created as part of my learning and practice journey.
