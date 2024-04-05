import tkinter as tk
from tkinter import messagebox
import re

class FormApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Form")

        self.label_name = tk.Label(self.master, text="Name:")
        self.label_name.grid(row=0, column=0, sticky=tk.W)

        self.entry_name = tk.Entry(self.master)
        self.entry_name.grid(row=0, column=1)

        self.label_email = tk.Label(self.master, text="Email:")
        self.label_email.grid(row=1, column=0, sticky=tk.W)

        self.entry_email = tk.Entry(self.master)
        self.entry_email.grid(row=1, column=1)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=2, columnspan=2)

    def submit_form(self):
        name = self.entry_name.get()
        email = self.entry_email.get()

        if not name:
            messagebox.showerror("Error", "Please enter your name.")
        elif not self.validate_email(email):
            messagebox.showerror("Error", "Please enter a valid email address.")
        else:
            messagebox.showinfo("Success", "Form submitted successfully!")

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

def main():
    root = tk.Tk()
    app = FormApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
