# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 09:13:47 2021

@author: Erlend Tøssebro
"""

STORRELSE = 60

import turtle


def tegn_firkant(storrelse):
    for i in range(4):
        turtle.forward(storrelse)
        turtle.right(90)    

        
if __name__ == "__main__":
    turtle.setup(500,800,1200,250)
    tegn_firkant(STORRELSE)
    turtle.done()
