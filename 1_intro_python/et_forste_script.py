# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:16:50 2021

@author: 2900888
"""

lengde_meter_streng = input("Skriv inn lenden til rommet i meter: ")
bredde_meter_streng = input("Skriv inn bredden til rommet i meter: ")
lengde_meter = float(lengde_meter_streng)
bredde_meter = float(bredde_meter_streng)
areal = lengde_meter*bredde_meter
print("Arealet til rommet er: ")
print(round(areal, 2))
