import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Entry widget to display and input numbers
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.entry_var, font=('Arial', 14), justify='right', bd=8, insertwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

        # Buttons for digits and operations with colors
        buttons = [
            ('7', '#D3D3D3'), ('8', '#D3D3D3'), ('9', '#D3D3D3'), ('/', '#808080'),
            ('4', '#D3D3D3'), ('5', '#D3D3D3'), ('6', '#D3D3D3'), ('*', '#808080'),
            ('1', '#D3D3D3'), ('2', '#D3D3D3'), ('3', '#D3D3D3'), ('-', '#808080'),
            ('0', '#D3D3D3'), ('.', '#D3D3D3'), ('=', '#808080'), ('+', '#808080')
        ]

        # Create and place buttons in the grid
        row_val = 1
        col_val = 0
        for button_text, button_color in buttons:
            tk.Button(master, text=button_text, width=5, height=2, command=lambda b=button_text: self.button_click(b), bg=button_color).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, value):
        current_text = self.entry_var.get()

        if value == '=':
            try:
                result = str(eval(current_text))
                self.entry_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
        else:
            current_text += value
            self.entry_var.set(current_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
