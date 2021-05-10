#!python3
# -*- coding: utf-8 -*-

# date: 5/02/20

import random
import itertools

def generateSamples(count):
    if type(count) != int:
        raise TypeError("Invalid type of arg in generateSamples()")
    sample = ['+', '*', '-', '/']
    randomSamples = list()
    for _ in range(count):
        tmp = sample.copy()
        random.shuffle(tmp)
        randomSamples.append(tmp)
    return randomSamples

def check(operations):
    possibleParentheses = (
        (0,4),
        (0,6),
        (0,8),

        (2,6),
        (2,8),
        (2,10),

        (4,8),
        (4,10),

        (6,10)
    )
    for pi in possibleParentheses:
        answer = []
        for op in operations:
            answer.append("3")
            answer.append(op)
        answer.append("3")

        answer.insert(pi[0], "(")  
        answer.insert(pi[1], ")")  
        answer = "".join(answer)

        try:
            evalAnswer = eval(answer)
        except ZeroDivisionError as err:
            continue
        yield answer, evalAnswer

def checkV2(operations):
    pass
    # 3/3-3*3+3
    # 3 3 3 3 3
    
if __name__ == "__main__":
    # allPossibleArr = [list(p) for p in itertools.permutations(['+', '*', '-', '/'])] 
    # for op in allPossibleArr:
    #     print("Testing for > {}".format(op))
    #     for answerS, answer in check(op):
    #         print("\tCheck: {} = {}".format(answerS, answer))
    #         # if(answer==6 or answer==8 or answer==10):
    #         #     print(answerS)
    #     print("\n")
    with open("tmp.txt", "r") as file:
        with open("eqs.txt", "w") as f:
            for _ in [x.strip(" :") for x in file.readlines()]:
                f.write(_)