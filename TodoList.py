import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        
        # Initialize tasks list
        self.tasks = []

        # Create GUI elements
        self.task_entry = tk.Entry(master, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="green", fg="white")
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, height=10, width=40)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.edit_button = tk.Button(master, text="Edit Task", command=self.edit_task, bg="blue", fg="white")
        self.edit_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg="red", fg="white")
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.task_listbox.insert(tk.END, new_task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            current_task = self.task_listbox.get(selected_index)
            edited_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=current_task)
            if edited_task:
                self.tasks[selected_index] = edited_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, edited_task)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            response = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
            if response == tk.YES:
                del self.tasks[selected_index]
                self.task_listbox.delete(selected_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


