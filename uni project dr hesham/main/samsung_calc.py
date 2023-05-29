import tkinter as tk

# Define the colors
bg_color = "#f2f2f2"
fg_color = "#000000"
keypad_bg_color = "#d9d9d9"
keypad_fg_color = "#000000"
display_bg_color = "#e5e5e5"
display_fg_color = "#000000"
operator_color = "#ff9500"
equals_color = "#ff2d55"

# Create the main window
root = tk.Tk()
root.title("iPhone Calculator")
root.configure(bg=bg_color)

# Create the display
display = tk.Entry(root, font=("Helvetica", 36), bd=0, justify="right", bg=display_bg_color, fg=display_fg_color)
display.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="NSEW")

# Create the buttons
buttons = [
    "C", "±", "%", "÷",
    "7", "8", "9", "×",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", ".", "DEL", "="
]

# Create a function to handle button clicks
def button_click(value):
    if value == "C":
        display.delete(0, tk.END)
    elif value == "±":
        if display.get()[0] == "-":
            display.delete(0)
        else:
            display.insert(0, "-")
    elif value == "%":
        display.insert(tk.END, "/100")
    elif value == "DEL":
        display.delete(len(display.get())-1, tk.END)
    elif value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, value)

# Create the buttons in a grid
for i, value in enumerate(buttons):
    button = tk.Button(root, text=value, width=6, height=3, font=("Helvetica", 18), bg=keypad_bg_color, fg=keypad_fg_color, activebackground=fg_color, activeforeground=keypad_bg_color, bd=0, highlightthickness=0, command=lambda v=value: button_click(v))
    button.grid(row=i//4+1, column=i%4, padx=5, pady=5, sticky="NSEW")
    if value in ["÷", "×", "-", "+", "="]:
        button.configure(bg=operator_color, fg=fg_color, activebackground=equals_color, activeforeground=fg_color)

# Configure the grid
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
for i in range(1, 6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

# Start the main loop
root.mainloop()