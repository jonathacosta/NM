#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos Numéricos
Prof. Jonatha Costa

Exercício proposto

1. Escreva os números a seguir nos seguintes formatos: 
    - Formato binário; 
    - Representação em ponto flutuante na base 2. 
    - Cadeia de 32 bits em precisão simples conforme a norma IEEE–754.

    a. 81
    b. 66,25
    c. -0,625
    d. 0,533203125
"""

from PontoFlutuante import Num2ieee
# Q1
#%%
itens=[81.5, 66.25,-0.625, 0.533203125]
for item in itens:
    print(f'\nNúmero {item} em:')
    a,b,c = Num2ieee.int_frac(item)
    print(f'Fomato binário:{a}')
    print(f'Fomato binário ponto flutuante base 2: {a[0]}.{a[1:]}{b} * 2^{len(a)-1}')
    print('Precisão de 32 bits:',Num2ieee.NumRes32bits(a,b,c))
    
