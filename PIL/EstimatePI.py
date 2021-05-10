#!python3
# -*- coding: utf-8 -*-

import random
from math import sqrt 
import numpy as np
import matplotlib.pyplot as plt

##################################  
### Created 3/10/2020 ############  
################################## 

##################################
### Georgia: 15 ##################
### Coronavirus cases: 116,740 ###
### Deaths: 4,095 ################
### Recovered: 64,752 ############
##################################

def estimatePI(n, plotPoints):
    n1 = 0
    n2 = 0

    x = np.random.rand(n)
    y = np.random.rand(n)

    if plotPoints:
        plot(x,y)

    for x0,y0 in np.array(list(zip(x,y))):
        l = sqrt(x0**2 + y0**2)
        n2+=1
        if l < 1:
            n1+=1
    return 4*n1/n2    

def plot(x,y):
    circle1 = plt.Circle((0, 0), 1, color="black", alpha=.2)
    fig, ax = plt.subplots() 
    ax.axis('scaled')
    ax.add_artist(circle1)

    plt.scatter(x, y, s=.05, color="black")
    plt.show()


if __name__=="__main__":
    pointCount = 100000 # more points, more accuracy 
    showPlot = True

    pi = estimatePI(pointCount, showPlot)
    print(pi)