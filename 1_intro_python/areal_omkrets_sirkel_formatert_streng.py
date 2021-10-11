# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:31:04 2021

@author: 2900888
"""

import math

radius_streng = input("Skriv inn radius til sirkelen: ")
radius = float(radius_streng)
areal = math.pi*radius*radius
omkrets = 2.0*math.pi*radius
print(f"Areal: {areal:6.2f}    Omkrets: {omkrets:6.2f}")
