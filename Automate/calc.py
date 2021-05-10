from tkinter import *


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.create_buttons()
        self.create_entry()

    def click(self, num):
        current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, current + str(num))

    def create_entry(self):
        self.e = Entry(self.root, width=35, borderwidth=4)
        self.e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def create_buttons(self):
        b1 = Button(self.root, padx=40, pady=20, text="1",
                    command=lambda: self.click(1))
        b2 = Button(self.root, padx=40, pady=20, text="2",
                    command=lambda: self.click(2))
        b3 = Button(self.root, padx=40, pady=20, text="3",
                    command=lambda: self.click(3))
        b4 = Button(self.root, padx=40, pady=20, text="4",
                    command=lambda: self.click(4))
        b5 = Button(self.root, padx=40, pady=20, text="5",
                    command=lambda: self.click(5))
        b6 = Button(self.root, padx=40, pady=20, text="6",
                    command=lambda: self.click(6))
        b7 = Button(self.root, padx=40, pady=20, text="7",
                    command=lambda: self.click(7))
        b8 = Button(self.root, padx=40, pady=20, text="8",
                    command=lambda: self.click(8))
        b9 = Button(self.root, padx=40, pady=20, text="9",
                    command=lambda: self.click(9))
        b0 = Button(self.root, padx=40, pady=20, text="0",
                    command=lambda: self.click(0))
        badd = Button(self.root, padx=39, pady=20, text="+", command=self.add)
        bC = Button(self.root, padx=88, pady=20, text="C",
                    command=lambda: self.e.delete(0, END))
        bequals = Button(self.root, padx=88, pady=20,
                         text="=", command=self.equals)
        bsubtract = Button(self.root, padx=40, pady=20,
                           text="-", command=self.subtract)
        bmultiply = Button(self.root, padx=40, pady=20,
                           text="*", command=self.multiply)
        bdivide = Button(self.root, padx=42, pady=20,
                         text="/", command=self.divide)

        b1.grid(row=1, column=0)
        b2.grid(row=1, column=1)
        b3.grid(row=1, column=2)
        b4.grid(row=2, column=0)
        b5.grid(row=2, column=1)
        b6.grid(row=2, column=2)
        b7.grid(row=3, column=0)
        b8.grid(row=3, column=1)
        b9.grid(row=3, column=2)
        b0.grid(row=4, column=0)
        bC.grid(row=4, column=1, columnspan=2)
        badd.grid(row=5, column=0)
        bequals.grid(row=5, column=1, columnspan=2)
        bsubtract.grid(row=6, column=0)
        bmultiply.grid(row=6, column=1)
        bdivide.grid(row=6, column=2)

    def equals(self):
        try:
            self.s_num = float(self.e.get())
        except ValueError:
            self.s_num = 0
        self.e.delete(0, END)
        try:
            if self.op == "add":
                self.e.insert(0, self.f_num + self.s_num)
            elif self.op == "subtract":
                self.e.insert(0, self.f_num - self.s_num)
            elif self.op == "multiply":
                self.e.insert(0, self.f_num * self.s_num)
            elif self.op == "divide":
                self.e.insert(0, self.f_num / self.s_num)

        except ValueError:
            pass
        except ZeroDivisionError:
            self.e.insert(0, "can't divide by zero")

    def subtract(self):
        self.op = "subtract"
        try:
            self.f_num = float(self.e.get())
        except ValueError:
            self.f_num = 0
        self.e.delete(0, END)

    def multiply(self):
        self.op = "multiply"
        try:
            self.f_num = float(self.e.get())
        except ValueError:
            self.f_num = 0
        self.e.delete(0, END)

    def divide(self):
        self.op = "divide"
        try:
            self.f_num = float(self.e.get())
        except ValueError:
            self.f_num = 0
        self.e.delete(0, END)

    def add(self):
        self.op = "add"
        try:
            self.f_num = float(self.e.get())
        except ValueError:
            self.f_num = 0
        self.e.delete(0, END)


root = Tk()
e = Interface(root=root)
root.mainloop()
