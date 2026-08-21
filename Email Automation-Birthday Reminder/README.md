# Birthday Wisher – Automated Birthday Email Sender

A simple Python automation project that automatically sends a personalized **Happy Birthday email** to people whose birthday matches today's date.

The program reads birthday information from a CSV file, selects a random birthday message template, personalizes it with the recipient's name, and sends the email using SMTP.

## Features

* Automatically checks today's date
* Finds people whose birthday is today
* Reads birthday information from a CSV file
* Sends personalized birthday emails automatically
* Randomly selects one of multiple birthday letter templates
* Replaces `[NAME]` with the recipient's actual name
* Uses email credentials for SMTP authentication

## Technologies Used

* **Python**
* `datetime` – for getting today's date
* `pandas` – for reading and processing the CSV file
* `random` – for selecting a random birthday template
* `smtplib` – for sending emails through SMTP

##  Project Structure

```text
Birthday-Wisher/
│
├── main.py
├── birthdays.csv
│   Readme.md
└── letter_templates/
    ├── letter_1.txt
    ├── letter_2.txt
    └── letter_3.txt
```

## CSV File Format

The `birthdays.csv` file should contain the following columns:

```csv
name,email,year,month,day
John,john@example.com,1999,8,21
Sarah,sarah@example.com,2001,12,15
```

### Required Columns

| Column  | Description                 |
| ------- | --------------------------- |
| `name`  | Name of the birthday person |
| `email` | Recipient's email address   |
| `year`  | Birth year                  |
| `month` | Birth month                 |
| `day`   | Birth day                   |

The program uses the `month` and `day` values to determine whether today is someone's birthday.

## Letter Templates

Create a folder named:

```text
letter_templates
```

Inside it, add three text files:

```text
letter_1.txt
letter_2.txt
letter_3.txt
```

Each template should contain:

```text
Dear [NAME],

Wishing you a very Happy Birthday!

Have a wonderful day!
```

The program randomly selects one of these templates and replaces:

```text
[NAME]
```

with the recipient's name.

---

## How It Works

### 1. Get today's date

The program gets the current date using Python's `datetime` module.

```python
today = datetime.now()
today_tuple = (today.month, today.day)
```

### 2. Read the birthday data

The program loads `birthdays.csv` using pandas.

```python
data = pandas.read_csv("birthdays.csv")
```

### 3. Check for today's birthday

The birthdays are converted into a dictionary using the month and day as the key.

```python
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}
```
The program then checks whether today's date exists in the dictionary.

### 4. Select a birthday template

If someone has a birthday today, one of the three templates is selected randomly.

```python
file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
```

### 5. Personalize the message

The `[NAME]` placeholder is replaced with the birthday person's name.

```python
contents = contents.replace("[NAME]", birthday_person["name"])
```

### 6. Send the email

The personalized message is sent using Python's `smtplib`.

```python
connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=birthday_person["email"],
    msg=f"Subject:Happy Birthday!\n\n{contents}"
)
```

##  Email Configuration

Before running the program, update these values in `main.py`:

```python
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"
```

You also need to configure the SMTP server for your email provider.

For example:

```python
with smtplib.SMTP("YOUR SMTP SERVER ADDRESS") as connection:
```

The SMTP address must match your email provider. The original project instructions also identify updating the email credentials and SMTP address as required setup steps.

---

## Important Security Note

**Never upload your real email password to GitHub.**

Do NOT commit:

```python
MY_PASSWORD = "your-real-password"
```

Instead, use environment variables in a real project.

For example:

```python
import os

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
```

Then store your credentials locally in environment variables rather than directly inside the Python source code.

You should also add sensitive configuration files to `.gitignore` when necessary.

## How to Run

### Step 1 – Clone the repository

```bash
git clone <your-repository-url>
```

### Step 2 – Open the project

```bash
cd Birthday-Wisher
```

### Step 3 – Install dependencies

The project uses pandas.

```bash
pip install pandas
```

### Step 4 – Configure your email

Update your email configuration and SMTP server.

### Step 5 – Add birthday information

Update:

```text
birthdays.csv
```

with the required birthday details.

### Step 6 – Add letter templates

Make sure the following files exist:

```text
letter_templates/letter_1.txt
letter_templates/letter_2.txt
letter_templates/letter_3.txt
```

### Step 7 – Run the program

```bash
python main.py
```

If today's date matches a birthday in the CSV file, the program will send a personalized birthday email.

## Example

Suppose `birthdays.csv` contains:

```csv
name,email,year,month,day
Manas,manas@example.com,2003,8,21
```

If today's date is **August 21**, the program detects the birthday and generates a message such as:

```text
Subject: Happy Birthday!

Dear Manas,

Wishing you a very Happy Birthday!

Have a wonderful day!
```

The email is then sent automatically to the person's email address.

---

## What I Learned

This project helped practice:

* Working with CSV files
* Using **Pandas DataFrames**
* Reading and processing structured data
* Working with Python dictionaries
* Using `datetime`
* File handling with `open()`
* Random selection with `random`
* String replacement
* Email automation with `smtplib`
* SMTP authentication
* Python automation concepts
* Managing sensitive credentials

---

## Possible Future Improvements

Some improvements that could make this project more production-ready:

* Use environment variables for credentials
* Add better email formatting using HTML
* Create an email delivery log
* Add error handling for failed emails
* Support multiple birthdays on the same day
* Automatically schedule the program to run every day
* Support different email providers
* Create a simple GUI for managing birthdays
* Replace CSV storage with a database
* Add notifications when an email is successfully sent

## Project Purpose

The main purpose of this project is to demonstrate how Python can be used for **real-world automation**.

Instead of manually checking birthdays and writing individual emails, the program performs the entire process automatically.

## Author

**Manas**

## ⭐ If You Like This Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub!
