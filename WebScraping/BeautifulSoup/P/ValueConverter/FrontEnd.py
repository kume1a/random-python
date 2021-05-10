#!python3
# -*- coding utf-8 -*-
from tkinter import *
from BackEnd import Crawler

spider = Crawler("https://valuta.exchange/")
currency = spider.parse_js()

class Interface(object):
	def __init__(self, root):
		self.root = root

		self.frame = Frame(self.root, width=273, height=140, bg="#404040")
		self.frame.pack()

		self.root.resizable(width=False, height=False)
		self.root.iconbitmap('icon.ico')
		self.root.title("Valute Converter")

		self.in1 = []
		self.in2 = []

		self.selection()
		self.take_input()

	def print_converted(self):
		valute1 = self.menuVar1.get()
		valute2 = self.menuVar2.get()
		
		try:
			val1 = float(str(self.entryVar1.get()))
		except ValueError:
			val1 = 0
		val2 = self.entryVar2.get()

		n = float(currency.get(valute2))/float(currency.get(valute1))
		self.entry2.insert(0, round(n*val1, 2))

	def selection(self):
		options = [x for x in currency.keys()]

		self.menuVar1 = StringVar()
		self.menuVar2 = StringVar()

		self.menuVar1.set(options[0])
		self.menuVar2.set(options[0])

		menu1 = OptionMenu(self.frame, self.menuVar1, *["USD", "GEL", "EUR"], command=lambda: self.in1.append(self.menuVar1)).place(x=5, y=5)
		menu2 = OptionMenu(self.frame, self.menuVar2, *["USD", "GEL", "EUR"], command=lambda: self.in2.append(self.menuVar2)).place(x=203, y=5)
		b1 = Button(self.frame, text="Convert", command=self.print_converted, bg="#14b330").place(x=109, y=85)

	def take_input(self):
		self.entryVar1 = StringVar()
		self.entryVar2 = StringVar()
		self.entry1 = Entry(self.frame, border=3, textvariable=self.entryVar1, font=('Verdana',12), width=10)
		self.entry2 = Entry(self.frame, border=3, textvariable=self.entryVar2, font=('Verdana',12), width=10)

		self.entry1.place(x=5, y=40)
		self.entry2.place(x=160, y=40)


root = Tk()
Interface(root)
root.mainloop()