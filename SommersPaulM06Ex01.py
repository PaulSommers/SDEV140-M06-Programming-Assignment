"""
Author: Paul Sommers
Date written: 11/27/2024
Assignment: Module 06 Programming Assignment 1
Short Desc: This program creates a GUI-based window in tkinter, and the user provides a temperature.
            The program displays 2 buttons, a Celsius and a Fahrenheit button.  When the user clicks the Celsius button,
            the program converts the temperature to celsius and displays it.  When the user clicks 
            the Fahrenheit button, the program converts the temperature to fahrenheit and displays it.
"""
# Import the tkinter library
import tkinter as tk
from tkinter import messagebox


# Create the function to convert the temperature to fahrenheit
def convert_to_fahrenheit():
    try:
        # Get the temperature from the entry field
        celsius = float(temp_entry.get())
        # Convert to Fahrenheit using the formula
        fahrenheit = (9/5 * celsius) + 32
        # Display the result
        result_label.config(text=f"{celsius}°C = {fahrenheit:.1f}°F")
    except ValueError:
        messagebox.showerror("Error!", "Please enter a valid number")


# Create the function to convert the temperature to celsius
def convert_to_celsius():
    try:
        # Get the temperature from the entry field
        fahrenheit = float(temp_entry.get())
        # Convert to Celsius using the rearranged formula
        celsius = (fahrenheit - 32) * 5/9
        # Display the result
        result_label.config(text=f"{fahrenheit}°F = {celsius:.1f}°C")
    except ValueError:
        messagebox.showerror("Error!", "Please enter a valid number")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("300x200")

# Create and pack the input label
input_label = tk.Label(window, text="Enter Temperature:")
input_label.pack(pady=10)

# Create and pack the entry field
temp_entry = tk.Entry(window)
temp_entry.pack()

# Create and pack the buttons frame
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Create the conversion buttons
celsius_button = tk.Button(button_frame, text="Convert to Fahrenheit", command=convert_to_fahrenheit)
celsius_button.pack(side=tk.LEFT, padx=5)

fahrenheit_button = tk.Button(button_frame, text="Convert to Celsius", command=convert_to_celsius)
fahrenheit_button.pack(side=tk.LEFT, padx=5)

# Create and pack the result label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the main event loop
window.mainloop()