#!python3
# -*- endoding: utf-8 -*-

import subprocess

def runCommand(command):
    if type(command) != str:
        raise TypeError("runCommand: invalid type, str !={}".format(type(command)))

    res = subprocess.check_output(command, shell=True)
    print("runCommand(): stdout = %s"%res)
    return res.decode()

def testPython():
    test = runCommand("python")
    print(test)

print("starting")
if testPython():
    print("python exists")