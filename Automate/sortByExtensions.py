#!python3.8
# -*- coding: utf-8 -*-

import os 
import shutil

dirName = "D:\\Udemy\\[FreeTutorials.Eu] Udemy - nodejs-the-complete-guide"
os.chdir(dirName)

for folder in os.listdir("."):
    print(folder)
    os.chdir(folder)

    for file in os.listdir("."):
        if "." in file:
            extension = file.split(".")[-1]
        else:
            continue

        if not os.path.exists(extension+"Files"):
            os.mkdir(extension+"Files")

        if "." in file:
            shutil.move(file, extension+"Files")
        print("\t{}".format(file))
    os.chdir("..")