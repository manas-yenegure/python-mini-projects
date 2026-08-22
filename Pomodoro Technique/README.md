# Pomodoro Timer

A simple **Pomodoro Timer desktop application** built with **Python and Tkinter**.
It helps users manage focused work sessions by automatically alternating between work periods, short breaks, and longer breaks.

The application features a graphical user interface with a tomato-themed timer, countdown display, Start and Reset buttons, and check marks to track completed work sessions.


## Features

* Simple and clean Pomodoro-style interface
* Countdown timer
* Work session tracking
* Short break after each work session
* Long break after multiple work sessions
* Automatic transition between work and break sessions
* Check marks for completed work sessions
* Reset button to restart the timer
* Desktop GUI built with Tkinter

## Technologies Used

* **Python 3**
* **Tkinter** — Graphical User Interface
* **Math** — Time calculation and session tracking

The project uses Tkinter's `after()` method to repeatedly update the countdown without freezing the GUI.

## Pomodoro Cycle

The timer follows this basic cycle:

```text
Work
  ↓
Short Break
  ↓
Work
  ↓
Short Break
  ↓
Work
  ↓
Short Break
  ↓
Work
  ↓
Long Break
  ↓
Repeat
```

### Default Timer Settings

| Session        |   Duration |
| -------------- | ---------: |
| 🟢 Work        |   1 minute |
| 🌸 Short Break |  5 minutes |
| 🔴 Long Break  | 20 minutes |

These values are defined at the beginning of the program and can be modified according to your preference.

> **Note:** The work duration is currently set to **1 minute** for testing/practice purposes. A traditional Pomodoro timer commonly uses a longer work period.

---

## Project Structure

```text
Pomodoro-Timer/
│
├── main.py
├── tomato.png
└── README.md
```

### Files

**`main.py`**
Contains the complete Python application, including the timer logic, countdown mechanism, GUI, buttons, and session tracking.

**`tomato.png`**
Image displayed in the center of the timer interface. The program loads this image using Tkinter's `PhotoImage`.

**`README.md`**
Project documentation.

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pomodoro-timer.git
```

### 2. Navigate to the Project

```bash
cd pomodoro-timer
```

### 3. Make Sure Python Is Installed

Check your Python version:

```bash
python --version
```

### 4. Run the Application

```bash
python main.py
```

The Pomodoro Timer window should open.

---

## How to Use

### Start

Click the **Start** button to begin the timer.

The application automatically determines whether the next session should be a work period, short break, or long break.

### Reset

Click the **Reset** button to:

* Stop/reset the current countdown
* Reset the timer display
* Reset the title
* Remove completed-session check marks
* Start the Pomodoro cycle again from the beginning

The reset functionality is implemented through the `reset_timer()` function.

### Check Marks

After completing work sessions, the application displays check marks to indicate the number of completed work sessions.

---

## How It Works

The application keeps track of the number of sessions using a variable called `reps`.

```python
reps += 1
```

The program then uses the session count to determine the appropriate timer:

```python
if reps % 8 == 0:
    # Long break
elif reps % 2 == 0:
    # Short break
else:
    # Work session
```

This allows the timer to automatically switch between work and break periods.

---

## Countdown Mechanism

The countdown is handled by the `count_down()` function.

It:

1. Converts seconds into minutes and seconds.
2. Updates the timer displayed on the canvas.
3. Waits one second.
4. Calls itself again with one second removed.
5. Starts the next session when the countdown reaches zero.

The program uses:

```python
window.after(1000, count_down, count - 1)
```

to schedule the next countdown update.

---

## User Interface

The application uses Tkinter widgets including:

* `Tk()` — Main application window
* `Label` — Displays the timer title and check marks
* `Canvas` — Displays the tomato image and countdown
* `Button` — Start and Reset controls

The interface uses a tomato-inspired color scheme defined through constants such as `PINK`, `RED`, `GREEN`, and `YELLOW`.

---

## What I Learned From This Project

This project is useful for practicing several Python concepts:

* Tkinter GUI development
* Functions
* Global variables
* Conditional statements
* Loops
* Mathematical calculations
* Modulo operator
* Event-driven programming
* Tkinter `after()` method
* Canvas widgets
* GUI layout using `grid()`
* Basic state management

---

## Possible Improvements

Future versions could include:

* Custom work/break durations
* Sound notification when a session ends
* Pause/Resume button
* Daily productivity statistics
* Dark mode
* Save completed sessions
* Task list integration
* Desktop notifications
* Daily Pomodoro goals
* Improved responsive interface

---

## Important

Make sure `tomato.png` is located in the **same directory as `main.py`**.

Otherwise, Tkinter may not be able to load the image:

```python
tomato_img = PhotoImage(file="tomato.png")
```

---

## Author

**Manas Yenegure**

---

## License

This project is available for educational and personal use.
