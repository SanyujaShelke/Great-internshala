import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        result_label.config(text="Result: " + result)
    except Exception as e:
        result_label.config(text="Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for input
entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Result label
result_label = tk.Label(root, text="Result:", font=("Arial", 20))
result_label.grid(row=row_val, column=col_val, columnspan=4)

# Start the main loop
root.mainloop()
