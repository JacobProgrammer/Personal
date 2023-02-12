import tkinter as tk

# Function to perform calculation
def calculate(operation):
    if operation == "=":
        try:
            result.set(eval(entry.get()))
        except:
            result.set("Error")
    elif operation == "C":
        result.set("")
        entry.delete(0, tk.END)
    else:
        result.set("")
        entry.insert(tk.END, operation)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Result display
result = tk.StringVar()
result.set("")
display = tk.Entry(root, textvariable=result, font=("Helvetica", 16), width=20, bd=4, bg="white", justify="right")
display.grid(row=0, column=0, columnspan=4)

# Entry widget
entry = tk.Entry(root, font=("Helvetica", 16), width=20, bd=4, bg="white", justify="right")
entry.grid(row=1, column=0, columnspan=4)

# Buttons
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", "C", "=", "/"
]

row = 2
column = 0
for button in buttons:
    command = lambda x=button: calculate(x)
    tk.Button(root, text=button, font=("Helvetica", 16), width=5, height=2, command=command).grid(row=row, column=column)
    column += 1
    if column > 3:
        column = 0
        row += 1

# Run the main loop
root.mainloop()
