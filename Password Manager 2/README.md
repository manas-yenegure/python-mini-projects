# MyPass — Password Manager

A simple desktop **Password Manager built with Python and Tkinter**.  
MyPass allows you to generate strong passwords, save login credentials locally, search saved accounts, and manage password visibility through a clean graphical interface.

This project is an upgraded version of the basic Password Generator I built earlier, taking the password-generation concept and turning it into a complete desktop application.

## Features

- **Password Generator**
  - Generates random passwords using letters, numbers, and symbols.
  - Automatically shuffles the generated password.
  - Copies the generated password to the clipboard.

- **JSON Password Storage**
  - Saves credentials in a structured `data.json` file.
  - Stores website/app name, email/username, and password.
  - Automatically creates the JSON file when needed.

- **Search Saved Passwords**
  - Search for an exact website/app.
  - Supports partial website searches.
  - Displays multiple matching accounts when applicable.
  - Retrieved passwords are copied to the clipboard.

- **Show / Hide Password**
  - Passwords are hidden by default.
  - Toggle password visibility with a button.

- **Input Validation**
  - Checks for empty fields.
  - Validates email format when an email is entered.
  - Requires passwords to contain at least 8 characters.
  - Warns when a saved website already exists.
  - Allows the user to confirm before replacing existing credentials.

- **Modern Tkinter UI**
  - Uses `ttk` widgets.
  - Clean layout with sections, buttons, labels, and spacing.
  - Includes the custom **MyPass** logo.

- **Clear Fields**
  - Quickly clears the website and password fields.


## Preview

Add a screenshot of your application here after taking one:

```text
![MyPass Screenshot](screenshot.png)
```


## Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Tkinter / ttk** | Desktop graphical user interface |
| **JSON** | Local credential storage |
| **Pyperclip** | Copy passwords to clipboard |
| **Pathlib** | File and path handling |


## Project Structure

```text
MyPass-Password-Manager/
│
├── Password_Manager_Upgraded.py
├── logo.png
├── README.md
├── requirements.txt
├── .gitignore
│
└── data.json              # Created automatically (local only)
```

> ⚠️ `data.json` contains saved credentials and should **not** be uploaded to GitHub.



## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/MyPass-Password-Manager.git
```

### 2. Navigate to the project

```bash
cd MyPass-Password-Manager
```

### 3. Install the dependency

```bash
pip install pyperclip
```

Tkinter is included with most standard Python installations.

### 4. Run the application

```bash
python Password_Manager_Upgraded.py
```

---

## How to Use

### Generate a Password

1. Enter a website/app name.
2. Enter your email/username.
3. Click **Generate Password**.
4. A random password will be generated.
5. The generated password is automatically copied to your clipboard.
6. Click **Save Password** to store it.

### Save a Password

1. Enter the website/app name.
2. Enter your email/username.
3. Enter or generate a password.
4. Click **Save Password**.
5. Confirm the details when prompted.
6. The credentials are saved to `data.json`.

### Search a Password

1. Enter the website/app name in the website field.
2. Click **Search Saved Password**.
3. If an account exists, its saved details are displayed.
4. If multiple accounts match, select the required account.
5. The saved password is copied to the clipboard.

### Show / Hide Password

Click the **Show** / **Hide** button beside the password field to toggle password visibility.


## Data Storage

MyPass stores credentials locally in:

```text
data.json
```

Example structure:

```json
{
    "example.com": {
        "email": "user@example.com",
        "password": "ExamplePassword123!"
    }
}
```

The application uses JSON because it provides a simple structured format that is easier to read and search than the original text-file approach.


## Security Note

**This project is intended for learning and portfolio purposes.**

Passwords are currently stored as **plain text inside the local `data.json` file**. The application does not currently use encryption or a master password.

For real-world password management, sensitive credentials should be protected using proper encryption and secure authentication mechanisms.

### Planned security improvements

- Master password
- Encrypted password storage
- Secure password hashing where appropriate
- Encryption key management
- Automatic session locking
- Secure credential deletion


## Requirements

Create a `requirements.txt` file containing:

```text
pyperclip
```

Python's `tkinter`, `json`, `random`, `pathlib`, and `re` modules are part of the standard library.

---

## Recommended `.gitignore`

To prevent accidentally uploading saved passwords, add:

```gitignore
# Saved credentials
data.json

# Python cache
__pycache__/
*.py[cod]

# Virtual environments
venv/
.venv/

# IDE files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
```

## Learning Outcomes

Through this project, I practiced:

- Python functions
- Tkinter GUI development
- Event-driven programming
- File handling
- JSON data storage
- Input validation
- Exception handling
- Clipboard integration
- Working with external Python packages
- Structuring a small desktop application


## Project Evolution

This project started from a simple **Password Generator** and was expanded into a desktop Password Manager.

### Password Generator → MyPass

```text
Password Generator
       ↓
Random password generation
       ↓
Tkinter GUI
       ↓
Clipboard integration
       ↓
Credential storage
       ↓
JSON-based data management
       ↓
Search functionality
       ↓
Input validation
       ↓
Show / Hide password
       ↓
MyPass Password Manager
```

## Future Improvements

Possible future versions may include:

- [ ] Master password authentication
- [ ] Encrypted credential storage
- [ ] Password strength indicator
- [ ] Password history
- [ ] Edit and delete saved accounts
- [ ] Dedicated password list/dashboard
- [ ] Dark mode
- [ ] Auto-lock after inactivity
- [ ] Import/export functionality
- [ ] Better password generation controls

## Author

**Manas Yenegure**


