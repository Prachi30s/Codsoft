import random
import string
import tkinter as tk

def generate_password(length, include_letters, include_numbers, include_symbols):
    character_set = ""
    if include_letters:
        character_set += string.ascii_letters
    if include_numbers:
        character_set += string.digits
    if include_symbols:
        character_set += string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(character_set)

    return password

def generate_and_display_password():
    length = int(length_entry.get())
    include_letters = letters_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    password = generate_password(length, include_letters, include_numbers, include_symbols)
    password_label.config(text=f"The password: {password}", fg="blue")  # Change label text and color

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")  # Set window size
root.configure(background='#f0f0f0')  # Set background color

# Create and place the widgets
length_label = tk.Label(root, text="Password Length:", font=("Arial", 14), bg='#f0f0f0')
length_label.grid(row=0, column=0)

length_entry = tk.Entry(root, font=("Arial", 14))
length_entry.grid(row=0, column=1)

letters_var = tk.BooleanVar()
letters_var.set(True)
letters_checkbutton = tk.Checkbutton(root, text="Include Letters", variable=letters_var, font=("Arial", 12), bg='#f0f0f0')
letters_checkbutton.grid(row=1, column=0)

numbers_var = tk.BooleanVar()
numbers_var.set(True)
numbers_checkbutton = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, font=("Arial", 12), bg='#f0f0f0')
numbers_checkbutton.grid(row=2, column=0)

symbols_var = tk.BooleanVar()
symbols_var.set(True)
symbols_checkbutton = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, font=("Arial", 12), bg='#f0f0f0')
symbols_checkbutton.grid(row=3, column=0)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, font=("Arial", 14), bg='black', fg='white')
generate_button.grid(row=4, column=0)

password_label = tk.Label(root, text="", font=("Arial", 16), bg='#f0f0f0')  # Increase font size
password_label.grid(row=5, column=0, columnspan=2)  # Span two columns

root.mainloop()