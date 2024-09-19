#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Prof.Jonatha Costa
Cálculo básico de integral com a biblioteca Sympy
Ver práticas em:
    https://docs.sympy.org/latest/explanation/best-practices.html

"""

import sympy as sp
x = sp.Symbol('x')

#%% Q1
"""
Questão 01: Calcular a integral definida de uma função f(x)=x^2 
no intervalo de 0 a 2"""
  # Definir a função
f = x**2
# Calcular a integral definida de 0 a 2
integral_definida = sp.integrate(f, (x, 0, 2))
integral_definida
#%% Q2
'''
Questão 02 : Calcular a integral indefinida da função g(x)=sin⁡(x):
'''
# Definir a função
g = sp.sin(x)
# Calcular a integral indefinida
integral_indefinida = sp.integrate(g, x)
integral_indefinida
#%% Q3
'''
Questão 03: Calcular uma integral definida onde o limite superior é 
um parâmetro​.
'''
# Definir a variável simbólica e o parâmetro
a = sp.Symbol('a')
# Definir a função
h = sp.exp(-x)
# Calcular a integral definida de 0 a 'a'
integral_parametrica = sp.integrate(h, (x, 0, a))
integral_parametrica

#%% Q4
'''
Questão 04: Cálculo de uma integral dupla de f(x,y)=x2+y2 sobre o 
retângulo [0,1]×[0,2]:
'''
# Definir as variáveis simbólicas
y = sp.Symbol('y')
# Definir a função
f_xy = x**2 + y**2
# Calcular a integral dupla
integral_dupla = sp.integrate(f_xy, (x, 0, 1), (y, 0, 2))
integral_dupla

#%% Nota
'''
Note que:      ∫_0^2​(∫_0^1​(x^2+y^2)dx)dy
    
1) ∫_0^1​(x2+y2)dx=[x3/3​+y^2x]_0^1​= (1/3​+y^2)
    
2) ∫_0^2​(1/3​+y2)dy=[y/3​+y3/3​]_0^2= 2/3​+(2^3)/3​ =2/​3+8/3​=10/3
   
'''