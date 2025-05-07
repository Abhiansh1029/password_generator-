import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    character_pool = ''
    if upper_var.get():
        character_pool += string.ascii_uppercase
    if lower_var.get():
        character_pool += string.ascii_lowercase
    if digits_var.get():
        character_pool += string.digits
    if special_var.get():
        character_pool += string.punctuation

    if not character_pool:
        messagebox.showwarning("Warning", "Select at least one character type.")
        return

    password = ''.join(random.choice(character_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")
root.resizable(False, False)

# Password Length
tk.Label(root, text="Password Length:").pack(pady=(10, 0))
length_entry = tk.Entry(root, width=10)
length_entry.pack()

# Options
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include UPPERCASE", variable=upper_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include lowercase", variable=lower_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include digits", variable=digits_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include special characters", variable=special_var).pack(anchor='w', padx=20)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Output Field
password_entry = tk.Entry(root, width=40, font=('Arial', 12))
password_entry.pack(pady=10)

# Info Label
tk.Label(root, text="(Password copied to clipboard automatically!)", font=("Arial", 8)).pack()

root.mainloop()
