import json
import re
from pathlib import Path
from random import choice, randint, shuffle
from tkinter import Tk, Canvas, END, StringVar, messagebox
from tkinter import ttk, Toplevel, PhotoImage

import pyperclip


# FILE SETUP 

DATA_FILE = Path("data.json")
LOGO_FILE = Path("logo.png")


# PASSWORD GENERATOR 

def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!#$%&()*+"

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    try:
        pyperclip.copy(password)
    except Exception:
        pass


# JSON DATA HANDLING

def load_data():
    """Load saved passwords from JSON."""
    if not DATA_FILE.exists():
        return {}

    try:
        with DATA_FILE.open("r", encoding="utf-8") as data_file:
            data = json.load(data_file)

        return data if isinstance(data, dict) else {}

    except (json.JSONDecodeError, OSError):
        messagebox.showerror(
            "Data Error",
            "The saved password file could not be read."
        )
        return {}


def save_data(data):
    """Save passwords to JSON."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as data_file:
            json.dump(data, data_file, indent=4)
        return True

    except OSError as error:
        messagebox.showerror(
            "Save Error",
            f"Could not save your password:\n{error}"
        )
        return False


# VALIDATION

def is_valid_email(email):
    """Basic email format validation."""
    if not email:
        return True  # Email/username can be optional.

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None


def validate_inputs():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get()

    if not website:
        messagebox.showwarning(
            "Missing Website",
            "Please enter a website or app name."
        )
        website_entry.focus()
        return None

    if not email:
        messagebox.showwarning(
            "Missing Email",
            "Please enter an email or username."
        )
        email_entry.focus()
        return None

    if not is_valid_email(email):
        messagebox.showwarning(
            "Invalid Email",
            "Please enter a valid email address or username."
        )
        email_entry.focus()
        return None

    if not password:
        messagebox.showwarning(
            "Missing Password",
            "Please enter or generate a password."
        )
        password_entry.focus()
        return None

    if len(password) < 8:
        messagebox.showwarning(
            "Weak Password",
            "Password should contain at least 8 characters."
        )
        password_entry.focus()
        return None

    return website, email, password


# SAVE PASSWORD

def save():
    details = validate_inputs()

    if details is None:
        return

    website, email, password = details
    data = load_data()

    if website in data:
        replace = messagebox.askyesno(
            "Website Already Exists",
            f"A password for '{website}' already exists.\n\n"
            "Do you want to replace it?"
        )

        if not replace:
            return

    data[website] = {
        "email": email,
        "password": password
    }

    if save_data(data):
        messagebox.showinfo(
            "Saved",
            f"Password for {website} has been saved successfully."
        )

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# SHOW / HIDE PASSWORD

def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="•")
        toggle_button.config(text="Show")
    else:
        password_entry.config(show="")
        toggle_button.config(text="Hide")


# SEARCH PASSWORDS

def search_password():
    website = website_entry.get().strip()

    if not website:
        messagebox.showwarning(
            "Search Password",
            "Enter a website or app name to search."
        )
        website_entry.focus()
        return

    data = load_data()

    if website in data:
        details = data[website]

        messagebox.showinfo(
            title=website,
            message=(
                f"Email/Username: {details.get('email', '')}\n"
                f"Password: {details.get('password', '')}"
            )
        )

        try:
            pyperclip.copy(details.get("password", ""))
        except Exception:
            pass

    else:
        # Also allow partial search.
        matches = [
            key for key in data
            if website.lower() in key.lower()
        ]

        if len(matches) == 1:
            details = data[matches[0]]

            messagebox.showinfo(
                title=matches[0],
                message=(
                    f"Email/Username: {details.get('email', '')}\n"
                    f"Password: {details.get('password', '')}"
                )
            )

            try:
                pyperclip.copy(details.get("password", ""))
            except Exception:
                pass

        elif len(matches) > 1:
            show_search_results(matches, data)

        else:
            messagebox.showinfo(
                "Not Found",
                f"No saved password was found for '{website}'."
            )


def show_search_results(matches, data):
    """Display multiple search matches in a small window."""
    search_window = Toplevel(window)

    search_window.title("Search Results")
    search_window.geometry("430x300")
    search_window.resizable(False, False)

    ttk.Label(
        search_window,
        text="Select a saved account:",
        font=("Segoe UI", 11, "bold")
    ).pack(pady=(18, 10))

    list_box = ttk.Treeview(
        search_window,
        columns=("website", "email"),
        show="headings",
        height=8
    )
    list_box.heading("website", text="Website / App")
    list_box.heading("email", text="Email / Username")
    list_box.column("website", width=160)
    list_box.column("email", width=220)
    list_box.pack(padx=15, fill="both", expand=True)

    for item in matches:
        details = data[item]
        list_box.insert(
            "",
            "end",
            iid=item,
            values=(item, details.get("email", ""))
        )

    def open_selected():
        selected = list_box.selection()

        if not selected:
            messagebox.showwarning(
                "Select Account",
                "Please select an account first.",
                parent=search_window
            )
            return

        selected_website = selected[0]
        details = data[selected_website]

        website_entry.delete(0, END)
        website_entry.insert(0, selected_website)

        email_entry.delete(0, END)
        email_entry.insert(0, details.get("email", ""))

        password_entry.delete(0, END)
        password_entry.insert(0, details.get("password", ""))

        try:
            pyperclip.copy(details.get("password", ""))
        except Exception:
            pass

        search_window.destroy()

    ttk.Button(
        search_window,
        text="Load Account & Copy Password",
        command=open_selected
    ).pack(pady=15)


# CLEAR FIELDS

def clear_fields():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


# UI SETUP

window = Tk()
window.title("MyPass - Password Manager")
window.geometry("620x620")
window.resizable(False, False)
window.config(padx=35, pady=30)

# Modern ttk theme
style = ttk.Style()
try:
    style.theme_use("clam")
except Exception:
    pass

style.configure(
    "Title.TLabel",
    font=("Segoe UI", 22, "bold")
)

style.configure(
    "Subtitle.TLabel",
    font=("Segoe UI", 10)
)

style.configure(
    "TLabel",
    font=("Segoe UI", 10)
)

style.configure(
    "TButton",
    font=("Segoe UI", 10),
    padding=(10, 7)
)

style.configure(
    "Primary.TButton",
    font=("Segoe UI", 10, "bold"),
    padding=(15, 8)
)

style.configure(
    "TEntry",
    padding=8
)

# Header
header_frame = ttk.Frame(window)
header_frame.pack(fill="x", pady=(0, 20))

try:
    logo_img = PhotoImage(file=str(LOGO_FILE))
    logo_canvas = Canvas(
        header_frame,
        width=110,
        height=110,
        highlightthickness=0
    )
    logo_canvas.create_image(55, 55, image=logo_img)
    logo_canvas.pack(side="left", padx=(20, 15))
except Exception:
    logo_img = None

title_frame = ttk.Frame(header_frame)
title_frame.pack(side="left", pady=20)

ttk.Label(
    title_frame,
    text="MyPass",
    style="Title.TLabel"
).pack(anchor="w")

ttk.Label(
    title_frame,
    text="Simple & secure password management",
    style="Subtitle.TLabel"
).pack(anchor="w", pady=(4, 0))

# Main card
card = ttk.LabelFrame(
    window,
    text="  Save Password  ",
    padding=20
)
card.pack(fill="x", padx=10)

# Website
ttk.Label(card, text="Website / App").grid(
    row=0, column=0, sticky="w", pady=8
)

website_entry = ttk.Entry(card, width=42)
website_entry.grid(
    row=0, column=1, columnspan=2, sticky="ew", pady=8
)
website_entry.focus()

# Email / Username
ttk.Label(card, text="Email / Username").grid(
    row=1, column=0, sticky="w", pady=8
)

email_entry = ttk.Entry(card, width=42)
email_entry.grid(
    row=1, column=1, columnspan=2, sticky="ew", pady=8
)

# Password
ttk.Label(card, text="Password").grid(
    row=2, column=0, sticky="w", pady=8
)

password_entry = ttk.Entry(
    card,
    width=27,
    show="•"
)
password_entry.grid(
    row=2, column=1, sticky="ew", pady=8
)

toggle_button = ttk.Button(
    card,
    text="Show",
    width=8,
    command=toggle_password
)
toggle_button.grid(
    row=2, column=2, padx=(8, 0), pady=8
)

# Generator
generate_password_button = ttk.Button(
    card,
    text="Generate Password",
    command=generate_password
)
generate_password_button.grid(
    row=3, column=1, sticky="ew", pady=(10, 8)
)

# Search + Save
search_button = ttk.Button(
    card,
    text="Search Saved Password",
    command=search_password
)
search_button.grid(
    row=4, column=1, sticky="ew", pady=6
)

save_button = ttk.Button(
    card,
    text="Save Password",
    style="Primary.TButton",
    command=save
)
save_button.grid(
    row=5, column=1, sticky="ew", pady=(12, 6)
)

clear_button = ttk.Button(
    card,
    text="Clear",
    command=clear_fields
)
clear_button.grid(
    row=6, column=1, sticky="ew", pady=6
)

card.columnconfigure(1, weight=1)

# Footer
ttk.Label(
    window,
    text="Passwords are stored locally in data.json",
    style="Subtitle.TLabel"
).pack(pady=(18, 0))

window.mainloop()
