import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")

# Function to update time
def time():
    string = strftime('%H:%M:%S %p')  # Format: Hour:Minute:Second AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update every 1 second

# Styling the clock
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

time()  # Call time function

root.mainloop()
