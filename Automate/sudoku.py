# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import re

def clear_screen():
    os.system("cls")

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

class Sudoku:
    def __init__(self):
        self.board = [[0 for row in range(9)] for column in range(9)]

    def draw_board(self):
        clear_screen()

        print("  ", "-"*17)
        for index, row in enumerate(self.board):
            print("{}".format(9-index), end=" |")
            print(*row, end="")
            print("|")
        print("  ", "-"*17)
        print("   ", end="")
        for index in range(1, 10):
            print(index, end=" ")
        print("\n")

    def check_input(self, inp):
        pattern = re.compile(r"^\d{2} \d$")
        return bool(pattern.match(inp))

    def take_input(self):
        # 24 9
        self.draw_board()
        move = input("$$ ")

        is_valid = self.check_input(move)
        while not is_valid:
            print("Wrong input format")
            move = input("$$ ")
            is_valid = self.check_input(move)
        


sudoku = Sudoku()
for i in range(4):
    sudoku.take_input()