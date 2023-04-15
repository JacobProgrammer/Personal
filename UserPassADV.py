import re 
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox



def display_users():
    # Connect to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Retrieve the list of usernames from the users table
    cursor.execute('SELECT username FROM users')
    results = cursor.fetchall()

    # Create a new window to show the usernames
    display_window = Toplevel()
    display_window.title("User List")

    # Create a listbox to display the usernames
    user_list = Listbox(display_window)
    user_list.pack()

    # Add each username to the listbox
    for row in results:
        user_list.insert(END, row[0])

    # Close the database connection
    conn.close()


def validate_email(email):
    # Check if the email address is valid using a regular expression
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email)

def validate_password(password):
    # Check that the password meets the strength requirements
    if len(password) < 8:
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+]", password):
        return False
    return True

def register_user(username, password, email):
    # Check that the password meets the strength requirements
    if not validate_password(password):
        raise ValueError("Password does not meet strength requirements")

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Store the user information in a database
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    # Create the users table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (username text, password text, email text)''')

    c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, hashed_password, email))
    conn.commit()
    conn.close()


def login_user(username, password):
    # Get the user's hashed password from the database
    # Connect to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Retrieve the user's hashed password from the database
    cursor.execute('SELECT password FROM users WHERE username=?', (username,))
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    # If the username doesn't exist in the database, return False
    if not result:
        return False

    # Hash the provided password and compare it to the hashed password in the database
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), result[0])
    if hashed_password == result[0]:
        return True
    else:
        return False

def delete_all_users():
    # Create a confirmation message box to confirm the action
    confirmed = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete all users?")
    if confirmed:
        # Connect to the database
        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        # Delete all rows from the users table
        c.execute("DELETE FROM users")

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Show a message box confirming the action
        messagebox.showinfo("Success", "All users deleted successfully")


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("User Registration Form")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create labels and entry fields for each input
        self.username_label = Label(self, text="Username:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = Entry(self)
        self.username_entry.grid(row=0, column=1)

        self.password_label = Label(self, text="Password:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=1, column=1)
        self.show_password_button = Button(self, text="Show Password", command=self.toggle_password_visibility)
        self.show_password_button.grid(row=1, column=2)

        self.email_label = Label(self, text="Email:")
        self.email_label.grid(row=2, column=0)
        self.email_entry = Entry(self)
        self.email_entry.grid(row=2, column=1)

        # Create a register button
        self.register_button = Button(self, text="Register", command=self.register_user, bg="lightblue", font=("Helvetica", 12))
        self.register_button.grid(row=4, column=0, padx=10, pady=10)

        # Create a login button
        self.login_button = Button(self, text="Login", command=self.login_user, bg="lightgreen", font=("Helvetica", 12))
        self.login_button.grid(row=4, column=2, padx=15, pady=10)

        # Create a display users button
        self.display_users_button = Button(self, text="Display Users", command=self.display_users, bg="orange", font=("Helvetica", 12))
        self.display_users_button.grid(row=4, column=1, padx=10, pady=10)

        # Create a delete all users button
        self.delete_all_users_button = Button(self, text="Delete All Users", command=self.delete_all_users, bg="red", font=("Helvetica", 12))
        self.delete_all_users_button.grid(row=4, column=3, padx=10, pady=10)



    def register_user(self):
        # Get values from the entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        # Validate the email address
        if not validate_email(email):
          messagebox.showerror("Error", "Invalid email address")
          return

        try:
          register_user(username, password, email)
          messagebox.showinfo("Success", "User registered successfully")
        except ValueError as e:
          messagebox.showerror("Error", str(e))

    def display_users(self):
        # Call the display_users function from the display_users module
        display_users()
    

    def login_user(self):
    # Get values from the entry fields
      username = self.username_entry.get()
      password = self.password_entry.get()
      # Check if the username and password are correct
      if login_user(username, password):
        messagebox.showinfo("Success", "Logged in successfully")
      else:
        messagebox.showerror("Error", "Incorrect username or password")

    def delete_all_users(self):
        delete_all_users()

    def toggle_password_visibility(self):
        # Toggle the show attribute of the password entry field between * and ''
        if self.password_entry.cget('show') == '':
            self.password_entry.configure(show='*')
            self.show_password_button.configure(text='Show Password')
        else:
            self.password_entry.configure(show='')
            self.show_password_button.configure(text='Hide Password')

root = Tk()
app = Application(master=root)
app.mainloop()
