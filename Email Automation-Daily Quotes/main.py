import smtplib
import datetime as dt
import random

My_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

now = dt.datetime.now()
weekday = now.weekday()
with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

print(quote)
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(My_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=My_EMAIL,
        to_addrs=My_EMAIL,
        msg=f"Subject:Daily Motivation\n\n{quote}"
    )
    print("Email sent successfully!")