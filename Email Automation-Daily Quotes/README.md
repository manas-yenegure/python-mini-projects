# Daily Motivation Email

A simple Python automation project that sends a **daily motivational quote via email** using Gmail's SMTP server.

The program randomly selects a motivational quote from a local `quotes.txt` file and sends it to the configured email address with the subject **"Daily Motivation"**.

This project was created as part of my Python learning journey and demonstrates practical use of **Python, SMTP, file handling, random selection, and email automation**.

## Features

* Reads motivational quotes from a text file
* Selects a random quote automatically
* Sends the selected quote through Gmail
* Supports Gmail App Password authentication
* Simple and lightweight Python automation
* Uses an external `quotes.txt` file for storing quotes

## Technologies Used

* **Python 3**
* `smtplib` – sending emails through SMTP
* `datetime` – working with date and time
* `random` – selecting a random quote
* Gmail SMTP Server

## Project Structure

```text
Daily-Motivation-Email/
│
├── main.py
├── quotes.txt
├── .gitignore
└── README.md
```

### Files

| File         | Description                                  |
| ------------ | -------------------------------------------- |
| `main.py`    | Main Python program                          |
| `quotes.txt` | Collection of motivational quotes            |
| `.gitignore` | Prevents sensitive files from being uploaded |
| `README.md`  | Project documentation                        |

---

## How It Works

The program follows these basic steps:

```text
Start
  ↓
Read quotes.txt
  ↓
Load all quotes
  ↓
Select a random quote
  ↓
Connect to Gmail SMTP
  ↓
Start TLS encryption
  ↓
Authenticate with Gmail
  ↓
Send motivational email
  ↓
Close connection
```

The quote database is stored separately in `quotes.txt`, and the program randomly selects one quote before sending the email.

## Gmail App Password Setup

This project uses Gmail SMTP authentication.

**Do not use your normal Gmail password.**

Instead, create a **Google App Password** for the application.

General process:

1. Enable **2-Step Verification** on your Google Account.
2. Open your Google Account security settings.
3. Create an **App Password**.
4. Generate a password for this project.
5. Store the App Password securely.
6. Never commit the App Password to GitHub.

> **Never put your Gmail password or App Password directly in `main.py`, README.md, screenshots, or GitHub commits.**

---

## Recommended Secure Configuration

Instead of writing credentials directly in the Python file:

```python
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"
```

use environment variables:

```python
import os

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
```

Then configure the variables on your computer.

For example:

```text
MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_gmail_app_password
```

The actual values should **never be committed to GitHub**.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/manas-yenegure/Daily-Motivation-Email.git
```

### 2. Navigate into the project

```bash
cd Daily-Motivation-Email
```

### 3. Run the program

```bash
python main.py
```

No external Python packages are required for the basic version.

## Email Configuration

The project uses Gmail's SMTP server:

```text
SMTP Server: smtp.gmail.com
Port: 587
Security: STARTTLS
```

The Python program establishes a secure SMTP connection, authenticates, and sends the selected quote.

---

## Example Email

**Subject:**

```text
Daily Motivation
```

**Example message:**

```text
You don't have to be great to start,
but you have to start to be great.

- Zig Ziglar
```

The actual quote is selected randomly from `quotes.txt`.

## Learning Outcomes

Through this project, I practiced:

* Python file handling
* Reading data from text files
* Random selection using Python
* Working with dates and times
* SMTP and email automation
* Gmail authentication
* Secure handling of credentials
* Python automation concepts

## Future Improvements

Possible improvements for future versions:

* [ ] Automatically send emails every morning
* [ ] Add a scheduler using Python
* [ ] Send emails to multiple recipients
* [ ] Create an HTML-formatted email
* [ ] Add a graphical user interface
* [ ] Add a database for storing quotes
* [ ] Track previously sent quotes
* [ ] Add different quote categories
* [ ] Add logging and error handling
* [ ] Move configuration to environment variables

---

## Security Notice

This project requires email authentication.

**Never commit the following to GitHub:**

* Gmail password
* Gmail App Password
* API keys
* `.env` files containing secrets
* Private credentials

If a password or App Password is accidentally pushed to GitHub, **revoke it immediately and generate a new one**.

## 👨‍💻 Author

**Manas Yenegure**
