# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 08:57:50 2021

@author: Erlend Tøssebro
"""

    
storrelse = int(input("Hvor stor skal diamanten være? "))

for y in range(storrelse):
    for x in range(storrelse):
        if y == storrelse-x-1:
            print("*", end="")
        else:
            print(" ", end="")
    for x in range(storrelse-1):
        if y == x+1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for y in range(storrelse-2, -1, -1):
    for x in range(storrelse):
        if y == storrelse-x-1:
            print("*", end="")
        else:
            print(" ", end="")
    for x in range(storrelse-1):
        if y == x+1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
