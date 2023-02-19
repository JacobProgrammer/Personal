import random
import string
import tkinter as tk
from tkinter import messagebox

# Password Generator
def generate_password():
    new_password = ''
    password_length = length_entry.get()
    if password_length.isnumeric():
        password_length = int(password_length)
        # Expand character set to include lowercase letters and special characters
        password_characters = string.ascii_letters + string.digits + string.punctuation
        new_password = ''.join(random.choices(password_characters, k=password_length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, new_password)
    else:
        messagebox.showerror('Invalid Length', 'Please enter a valid integer for password length.')

# Create Tkinter window
root = tk.Tk()
root.title('Password Generator')
root.geometry('300x200')

# Add labels and entry fields for password length and generated password
length_label = tk.Label(root, text='Password Length:')
length_label.pack()
length_entry = tk.Entry(root, width=10)
length_entry.pack()

password_label = tk.Label(root, text='Generated Password:')
password_label.pack()
password_entry = tk.Entry(root, width=30)
password_entry.pack()

# Add button to generate new password
generate_button = tk.Button(root, text='Generate Password', command=generate_password)
generate_button.pack()

root.mainloop()
