"""
This program randomly selects and outputs an object in a list
Author: Jacob Olshanskiy
Date: 4-26-22
"""
import random
import tkinter as tk
root = tk.Tk()
root.geometry("600x300")
name_var = tk.StringVar()
passw_var = tk.StringVar()
def submit():
    hats = ['Alo', 'JSC', 'SpaceX', 'UTHR', 'FIRST CMP', 'Plain Gray']
    hatchoice = random.choice(hats)
    print(hatchoice)
    name_var.set("")
    passw_var.set("")
name_label = tk.Label(root, text='Hello, I will make picking your hat much easier', font=('calibre', 10, 'bold'))
name_entry = tk.Label(root, text="When you are ready type choose and press submit", font=('calibre', 10, 'bold'))
name_start = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(root, text='Submit', command=submit)
name_label.grid(row=0, column=0)
name_entry.grid(row=1, column=0)
sub_btn.grid(row=2, column=1)
root.mainloop()