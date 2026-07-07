import tkinter as tk

# Function to update the display
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x420")

# Display
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]

for (text, row, col) in buttons:
    if text == "=":
        cmd = calculate
    elif text == "C":
        cmd = clear
    else:
        cmd = lambda t=text: click(t)

    tk.Button(
        root,
        text=text,
        width=8,
        height=3,
        font=("Arial", 14),
        command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()