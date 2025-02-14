import tkinter as tk
from tkinter import ttk

def handleButtonClick(button):
    current_text = result_var.get()
    temp = 1
    if button == "=":
        try:
            expression = current_text.replace("÷", "/").replace("x", "*")
            result,temp = eval(expression)
            
            if result.is_integer():
                result = int(result)
            
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
            print(temp) # wont print answer
    elif button == "C":
        result_var.set("")
    elif button == "%":
        try:
            current_number = float(current_text)
            result_var.set(current_number / 100)
        except ValueError:
            result_var.set("Error")
    elif button == "±":
        try:
            current_number = float(current_text)
            result_var.set(-current_number)
        except ValueError:
            result_var.set("Error")
    else:
        result_var.set(current_text + button)

# creating main window with size and title
root = tk.Tk()
root.title("Simple Calculator") # change title of app

result_var = tk.StringVar()
# result text field
result_entry = ttk.Entry(root, textvariable = result_var, font = ("Helvetica", 24), justify = "right")
result_entry.grid(row = 0, column = 0, columnspan = 4, sticky = "nsew")

# tuple holding buttons ("button", row, column, columnspan)
buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("x", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("3", 4, 0), ("2", 4, 1), ("1", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
]

style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font = ("Helvetica", 16), width = 10, height = 4)

# placing buttons onto window
for button in buttons:
    button_text, row, col = button[:3]
    colspan = button[3] if len(button) > 3 else 1
    btn = ttk.Button(root, text = button_text, command = lambda text = button_text: handleButtonClick(text), style = "TButton")
    btn.grid(row = row, column = col, columnspan = colspan, sticky = "nsew", ipadx = 10, ipady = 4, padx = 5, pady = 5)

# proptionally sizing window
for i in range(6):
    root.grid_rowconfigure(i, weight = 1)
for i in range(4):
    root.grid_columnconfigure(i, weight = 1)

# keyboard controls
root.bind("<Return>", lambda event: handleButtonClick("="))
root.bind("<BackSpace>", lambda event: handleButtonClick("C"))

root.geometry("500x700")
root.resizable(False, False)

root.mainloop()