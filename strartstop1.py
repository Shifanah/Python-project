import tkinter as tk
from tkinter import messagebox

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer App")

        self.is_running = False
        self.time_elapsed = 0

        self.label = tk.Label(self.master, text="Timer: 0 seconds")
        self.label.pack()

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.time_elapsed = 0
        self.update_label()

    def update_timer(self):
        if self.is_running:
            self.time_elapsed += 1
            self.update_label()
            self.master.after(1000, self.update_timer)

    def update_label(self):
        self.label.config(text=f"Timer: {self.time_elapsed} seconds")

def main():
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
