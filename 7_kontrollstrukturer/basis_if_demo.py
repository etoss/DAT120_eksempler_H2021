# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 14:26:25 2021

@author: 2900888
"""

# Dette er en kommentar

tall_streng = input("Skriv inn et heltall:")
tallet = int(tall_streng)
if tallet < 0:
    print("Tallet er negativt")
    print("  blokk 1")
    print("   test")
else:
    print("Tallet et ikke negativt")
    print("   blokk 2")
print("Etter if-setningen")

