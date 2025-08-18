import tkinter as tk
from tkinter import messagebox
from time import strftime
import threading
import time
import winsound  # works on Windows. For Linux/Mac you can use 'playsound' library

# Main window
root = tk.Tk()
root.title("Digital Clock with Alarm")

# Function to update clock
def update_time():
    current_time = strftime('%H:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Function to check alarm
def check_alarm():
    while True:
        set_alarm_time = alarm_time.get()
