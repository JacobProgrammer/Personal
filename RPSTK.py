import tkinter as tk
import random

# Function to play the game
def play_game(user_choice):
    # Computer makes a choice
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    # Determine the winner
    result = ""
    if user_choice == "Rock":
        if computer_choice == "Rock":
            result = "Draw"
        elif computer_choice == "Paper":
            result = "Computer wins"
        else:
            result = "You win"
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            result = "You win"
        elif computer_choice == "Paper":
            result = "Draw"
        else:
            result = "Computer wins"
    else:
        if computer_choice == "Rock":
            result = "Computer wins"
        elif computer_choice == "Paper":
            result = "You win"
        else:
            result = "Draw"

    # Show the result
    result_label.config(text=f"Result: {result}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Labels
result_label = tk.Label(root, text="Result: ", font=("Helvetica", 16))
result_label.pack()
computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Helvetica", 16))
computer_choice_label.pack()

# Buttons
buttons = [
    ("Rock", "Rock"),
    ("Paper", "Paper"),
    ("Scissors", "Scissors")
]

for text, choice in buttons:
    tk.Button(root, text=text, font=("Helvetica", 16), command=lambda c=choice: play_game(c)).pack()

# Run the main loop
root.mainloop()
