#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 13:27:15 2022

@author: infolab
"""

cadena = 'Geringoso'
capadepenapa = ''
vocales = ['a','e','i','o','u']
i = 0

for c in cadena:
    capadepenapa += c
    if c in vocales: 
       capadepenapa = capadepenapa + 'p' + c

print(capadepenapa)
      