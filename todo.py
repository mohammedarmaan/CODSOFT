import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Entry for new task
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Buttons
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5)

        update_button = tk.Button(root, text="Update Task", command=self.update_task)
        update_button.grid(row=1, column=0, padx=5, pady=5)

        display_button = tk.Button(root, text="Display Tasks", command=self.display_tasks)
        display_button.grid(row=1, column=1, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            messagebox.showinfo("Task Added", f"Task '{task}' added.")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def update_task(self):
        old_task = self.task_entry.get()
        if old_task in self.tasks:
            new_task = simpledialog.askstring("Update Task", "Enter the new task:")
            if new_task:
                index = self.tasks.index(old_task)
                self.tasks[index] = new_task
                messagebox.showinfo("Task Updated", f"Task '{old_task}' updated to '{new_task}'.")
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Empty Task", "Please enter a new task.")
        else:
            messagebox.showwarning("Task Not Found", f"Task '{old_task}' not found.")

    def display_tasks(self):
        if self.tasks:
            task_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(self.tasks)])
            messagebox.showinfo("Your To-Do List", task_list)
        else:
            messagebox.showinfo("Empty To-Do List", "Your To-Do List is empty.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
