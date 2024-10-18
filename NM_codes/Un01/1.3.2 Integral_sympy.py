#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Prof.Jonatha Costa
Cálculo básico de integral com a biblioteca Sympy
Ver práticas em:
    https://docs.sympy.org/latest/explanation/best-practices.html


Encontre a função primária para:
a) dy/dx = 2(x² -1) . 2x
b) dy/dx = 4(x² -1)³ .2x
c) dy/dx = 2(x³ -2)  . 3x²
d) dy/dx = 3(x³ -2)² . 3x²    
   
"""

import sympy as sp
x = sp.Symbol('x')

#%% Q4
    
f = 2*((x**2 - 1))* 2*x
g =  4*((x**2 -1)**3) * 2*x
h = 2**((x**3 - 2))*3*x**2
i = 3*((x**3 - 2)**2)*(3*x**2)
# display(f,g,h,i)
#%%    
for m,fun in enumerate([f,g,h,i]):
     print(f'Item {m}:')
     display(fun)
     display(sp.integrate(fun))
     print()



