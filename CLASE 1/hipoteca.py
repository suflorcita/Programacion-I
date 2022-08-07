#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:57:51 2022

@author: infolab
"""
# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
i = 0 
mes = 1

while saldo > 0:   
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    if i < 12: 
        saldo -= 1000   
        total_pagado += 1000
    
    if saldo < 0:         
        total_pagado += abs(saldo)
        saldo = 0 
    i += 1
    mes +=1 
    print(mes, round(total_pagado, 2), round(saldo, 2))
    
print('Total pagado:', round(total_pagado,2))
print('Meses:', mes)
