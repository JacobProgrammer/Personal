import string
import random
import tkinter as tk

# function to generate a random password
def generate_password():
    # define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate a random password of length 12
    password = ''.join(random.choice(characters) for i in range(12))

    # update the password label with the new password
    password_label.config(text=password)

# function to generate a random username
def generate_username():
    # define the possible characters for the username
    characters = string.ascii_lowercase + string.digits

    # generate a random username of length 8
    username = ''.join(random.choice(characters) for i in range(8))

    # update the username label with the new username
    username_label.config(text=username)

# create the tkinter window
window = tk.Tk()
window.title("Password and Username Generator")

# create the username label
username_title = tk.Label(window, text="Username:")
username_title.grid(row=0, column=0)

username_label = tk.Label(window, text="")
username_label.grid(row=0, column=1)

# create the password label
password_title = tk.Label(window, text="Password:")
password_title.grid(row=1, column=0)

password_label = tk.Label(window, text="")
password_label.grid(row=1, column=1)

# create the generate username and password buttons
generate_username_button = tk.Button(window, text="Generate Username", command=generate_username)
generate_username_button.grid(row=2, column=0)

generate_password_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_password_button.grid(row=2, column=1)

# run the window
window.mainloop()
