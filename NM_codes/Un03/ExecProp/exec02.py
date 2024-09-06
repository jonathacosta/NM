#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos Numéricos
Prof. Jonatha Costa

Exercício proposto
Questão 2. Escreva os números a seguir nos seguintes formatos:
    - Formato binário; 
    - Representação em ponto flutuante na base 2.
    - Cadeia de 64 bits em precisão dupla conforme a norma IEEE–754.
    
    a. 256,1875
    b. –30952
    c. 0,33203125
    d. 0,001220703125
"""

# Q2
#%%
from PontoFlutuante import Num2ieee
itens=[256.1875, -30952, 0.33203125, 0.001220703125]
for item in itens:
    print(f'\nNúmero {item} em:')
    a,b,c = Num2ieee.int_frac(item)
    print(f'Fomato binário:{a}')
    print(f'Fomato binário ponto flutuante base 2: {a[0]}.{a[1:]}{b} * 2^{len(a)-1}')
    print('Precisão de 32 bits:',Num2ieee.NumRes64bits(a,b,c))


    
    
