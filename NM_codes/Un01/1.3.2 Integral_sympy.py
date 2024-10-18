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

class ExecAula_1810():
    def q1():
        '''
        Esta é a integral da função da letra a
        da questão
        '''
        f = 2*((x**2 - 1))* 2*x
        res = sp.integrate(f) 
        print(res)
        return res

    def q2():
        f = 4*((x**2 -1)**3) * 2*x
        print(sp.integrate(f))
    
    def q3():
        f = 2**((x**3 - 2))*3*x**2
        return sp.integrate(f)  
    
    def q4():
        f = 3*((x**3 - 2)**2)*(3*x**2)
        return sp.integrate(f)  



ExecAula_1810.q1



#%% Q4
    
f = 2*((x**2 - 1))* 2*x
sp.integrate(f)
g =  4*((x**2 -1)**3) * 2*x
sp.integrate(g)
h = 2**((x**3 - 2))*3*x**2
sp.integrate(h)
i = 3*((x**3 - 2)**2)*(3*x**2)
sp.integrate(i)





