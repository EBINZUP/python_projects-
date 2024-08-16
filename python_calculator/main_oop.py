from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        # Entry widget for display
        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).grid(row=0, column=0, columnspan=4, pady=10)

        # Button definitions
        buttons = [
            ('(', 1, 0), (')', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('C', 5, 3)
        ]

        # Create and place buttons
        for (text, row, col) in buttons:
            if text == '=':
                Button(master, text=text, width=5, height=2, command=self.solve).grid(row=row, column=col, padx=5, pady=5)
            elif text == 'C':
                Button(master, text=text, width=5, height=2, command=self.clear).grid(row=row, column=col, padx=5, pady=5)
            else:
                Button(master, text=text, width=5, height=2, command=lambda t=text: self.show(t)).grid(row=row, column=col, padx=5, pady=5)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            # Replace 'x' with '*' for proper evaluation
            expression = self.entry_value.replace('x', '*')
            result = eval(expression)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")
            print(f"Error: {e}")

EBINZ = Tk()
calculator = Calculator(EBINZ)
EBINZ.mainloop()
