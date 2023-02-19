import random
import string
import sqlite3
import getpass

# Connect to database
conn = sqlite3.connect('passwords.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (website text, username text, password text)''')


# Password Generator
def password():
    while True:
        newSite = input("Please type a website you would like to generate a password for. "
                        "If you no longer want to continue please type 'Done': ")
        if newSite.lower() == 'done':
            break
        newPassword = eval(input("Please type the number of characters you would like in your password: "))

        # Expand character set to include lowercase letters and special characters
        randomPassword = ''.join(
            random.choices(string.ascii_letters + string.digits + string.punctuation, k=newPassword))

        print("Your new password is:", randomPassword)
        print("Would you like to store it?")
        store = input("(Type Y or N): ")
        if store.lower() == "y":
            username = input("Please enter a username for this website: ")
            # Store password securely using getpass library
            password = getpass.getpass(prompt="Please enter the password again to confirm: ")
            c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
                      (newSite, username, password))
            conn.commit()
            print("Now stored.")
        if store.lower() == "n":
            print("Now discarded.")


# Username Generator
def username():
    while True:
        newUsername = input("Please type a website you would like to generate a username for. "
                            "If you no longer want to continue please type 'Done': ")
        if newUsername.lower() == "done":
            break

        newUser = eval(input("Please type the number of characters you would like in your username: "))

        # Expand character set to include lowercase letters and other options
        randomUser = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=newUser))
        print("Your new username is:", randomUser)
        print("Would you like to store it?")
        store = input("(Type Y or N): ")
        if store.lower() == "y":
            c.execute("INSERT INTO passwords (website, username) VALUES (?, ?)", (newUsername, randomUser))
            conn.commit()
            print("Now stored.")
        if store.lower() == "n":
            print("Now discarded.")


# View stored passwords and usernames
def view():
    c.execute("SELECT * FROM passwords")
    print("Website\t\tUsername\t\tPassword")
    print("-----------------------------------------------")
    for row in c.fetchall():
        print(row[0] + "\t\t" + row[1] + "\t\t" + row[2])


# Delete username, password, or both
def delete_data():
    while True:
        website = input("Enter the website whose data you want to delete (Type 'Done' to exit): ")
        if website.lower() == 'done':
            break
        username = input("Enter the username for the website: ")
        password = getpass.getpass(prompt="Enter the password for the website: ")
        while True:
            delete_type = input("What would you like to delete? Type 'U' for username, 'P' for password, or 'B' for "
                                "both: ")
            if delete_type.lower() == 'u':
                confirm = input("Are you sure you want to delete the username for {}? (Y/N): ".format(website))
                if confirm.lower() == 'y':
                    c.execute("UPDATE passwords SET username = NULL WHERE website = ? AND username = ?",
                              (website, username))
                    conn.commit()
                    print("Username for {} deleted.".format(website))
                else:
                    print("Data not deleted.")
                break
            elif delete_type.lower() == 'p':
                confirm = input("Are you sure you want to delete the password for {}? (Y/N): ".format(website))
                if confirm.lower() == 'y':
                    c.execute("UPDATE passwords SET password = NULL WHERE website = ? AND username = ?",
                              (website, username))
                    conn.commit()
                    print("Password for {} deleted.".format(website))
                else:
                    print("Data not deleted.")
                break
            elif delete_type.lower() == 'b':
                confirm = input(
                    "Are you sure you want to delete the username and password for {}? (Y/N): ".format(website))
                if confirm.lower() == 'y':
                    c.execute("DELETE FROM passwords WHERE website = ? AND username = ?", (website, username))
                    conn.commit()
                    print("Username and password for {} deleted.".format(website))
                else:
                    print("Data not deleted.")
                break
            else:
                print("Invalid option. Please try again.")


# Main loop
while True:
    print("\nWhat would you like to do today?")
    print("1. Generate a new password")
    print("2. Generate a new username")
    print("3. View stored passwords and usernames")
    print("4. Delete username, password, or both")
    print("5. Exit program")

    choice = input("\nEnter the number of your choice: ")
    if choice == "1":
        password()
    elif choice == "2":
        username()
    elif choice == "3":
        view()
    elif choice == "4":
        delete_data()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
