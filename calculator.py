import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.display_var = tk.StringVar()
        self.display_var.set("")

        self.display = tk.Entry(self.master, textvariable=self.display_var, font=('Arial', 20), bd=10, insertwidth=4, width=15, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, btn_text):
        current_display = self.display_var.get()

        if btn_text == 'C':
            self.display_var.set("")
        elif btn_text == '=':
            try:
                result = eval(current_display)
                self.display_var.set(str(result))
            except Exception as e:
                self.display_var.set("Error")
        else:
            self.display_var.set(current_display + btn_text)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
