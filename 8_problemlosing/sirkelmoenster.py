# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 09:20:07 2021

@author: 2900888
"""

import turtle

STORRELSE = 50
VINKEL = 10

turtle.setup(500,800,1200,250)
turtle.speed(0)
vinkel_saa_langt = 0
while vinkel_saa_langt < 360:
    turtle.circle(STORRELSE)
    turtle.right(VINKEL)
    vinkel_saa_langt += VINKEL
turtle.done()
