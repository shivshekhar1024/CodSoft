import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, comp):
    if comp == "easy":
        characters = string.ascii_letters
    elif comp == "medium":
        characters = string.ascii_letters + string.digits
    else: 
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    length = length_var.get()
    complexity = complexity_var.get()

    try:
        length = int(length)
        if length <= 0:
            messagebox.showerror("Error", "Length must be a positive integer.")
            return
        password = generate_password(length, complexity)
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a valid integer for the length.")

root = tk.Tk()
root.title("Password Generator")

root.geometry("500x350")
root.configure(bg="#f0f0f0") 

length_label = tk.Label(root, text="Enter the desired length:", bg="#f0f0f0", fg="black")
length_label.pack()

length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var, bg="white", fg="black")
length_entry.pack()

complexity_label = tk.Label(root, text="Select complexity level:", bg="#f0f0f0", fg="black")
complexity_label.pack()

complexity_var = tk.StringVar()
complexity_var.set("medium") 
complexity_option = tk.OptionMenu(root, complexity_var, "easy", "medium", "hard")
complexity_option.config(bg="salmon", fg="black")
complexity_option.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui, bg="gray", fg="white")
generate_button.pack()

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, wraplength=300, bg="#f0f0f0", fg="black")
password_label.pack()

root.mainloop()
