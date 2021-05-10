#!python3
# -*- encoding: utf-8 -*-

# created on 3/22/2020

'''
In a previous exercise, we’ve written a program that “knows” a number and asks a 
user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will have in your 
head a number between 0 and 100. The program will guess a number, and you, the user,
will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took
to get your number.

As the writer of this program, you will have to choose how your program will 
strategically guess. A naive strategy can be to simply start the guessing at 1,
and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal
guessing strategy. An alternate strategy might be to guess 50 
(right in the middle of the range), and then increase / decrease by 1 as needed.
After you’ve written the program, try to find the optimal strategy! 
(We’ll talk about what is the optimal one next week with the solution.)
'''

from random import randint

def pick_number():
    print("Picking a number between 0-100")
    num = randint(0, 100)
    print("Guess is {}".format(num))
    return num

def guess(target):
    if type(target) != int:
        raise ValueError("int guess(): Invalid type, int != {}".format(type(target)))

    _min = 0
    _max = 101
    _guess = (_min + _max)//2
    guessCount = 0

    while _guess!=target:
        guessCount += 1
        print("\tguess = {}, target = {}".format(_guess, target))
        if _guess < target:
            _min = _guess
            _guess = (_min + _max)//2
        elif _guess > target:
            _max = _guess
            _guess = (_min + _max)//2
        
    print("{} = {}".format(_guess, target))
    print("Got it guessCount = {}\n".format(guessCount))    
      
    return guessCount

if __name__=="__main__":
    totalGuessCount = 0
    a = 10_0000

    for _ in range(a):
        totalGuessCount += guess(pick_number())
    print("\nDone")
    print("Median is {}".format(totalGuessCount/a))