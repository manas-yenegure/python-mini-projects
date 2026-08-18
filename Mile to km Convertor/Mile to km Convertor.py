from tkinter import *

#FUNCTION
def convert():
    miles = float(miles_input.get())
    kilometers = miles * 1.60934
    result_label.config(text=f"{kilometers:.2f} km")
#WINDOW
window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=30, pady=30)
#TITLE
title_label = Label(
    text="Mile to Kilometer Converter",
    font=("Arial", 16, "bold")
)
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
#INPUT 

miles_label = Label(text="Enter Miles:")
miles_label.grid(row=1, column=0, sticky="w")

miles_input = Entry(width=15)
miles_input.grid(row=1, column=1)
miles_input.insert(0, "0")

#BUTTON 
calculate_button = Button(
    text="Calculate",
    command=convert,
    width=15
)
calculate_button.grid(row=2, column=0, columnspan=2, pady=(10, 20))
#RESULT

result_text = Label(
    text="Kilometers:",
    font=("Arial", 11, "bold")
)
result_text.grid(row=3, column=0, sticky="w")

result_label = Label(
    text="0.00 km",
    font=("Arial", 11)
)
result_label.grid(row=3, column=1, sticky="w")

#MAIN LOOP 

window.mainloop()