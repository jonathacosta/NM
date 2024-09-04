#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Prof.Jonatha Costa
Cálculo básico de derivadas com a biblioteca Sympy
Ver práticas em:
    https://docs.sympy.org/latest/explanation/best-practices.html

"""

import sympy as sp
x = sp.symbols('x')

#%% Q1
"""
Questão 01: Calcular a derivada de uma função simples, f(x)=x^2
"""
# Definir a variável simbólica
f = x**2
# Definir a função
derivada = sp.diff(f, x)
derivada

#%% Q2
'''
Questão 02: Calcular a derivada de f(x)=sin⁡(x)f(x)=sin(x).
'''
# Definir a função
f_trig = sp.sin(x)
# Calcular o limite quando x tende ao infinito
derivada_trig = sp.diff(f_trig, x)
derivada_trig
#%% Q3
'''
Questão 03: Calcular a segunda derivada de f(x)=x3+3x^2
'''
# Definir a função
f2 = x**3 + 3*x**2
# Calcular a segunda derivada
segunda_derivada = sp.diff(f2, x, 2)
# Mostrar a segunda derivada
segunda_derivada

#%% Q4
'''
Questão 04: Calcular a derivada parcial de uma função de duas variáveis, 
f(x,y) = x^2+y^2, em relação a x.
'''
# Definir variáveis simbólicas
x, y = sp.symbols('x y')
# Definir a função
f_xy = x**2 + y**2
# Calcular a derivada parcial em relação a x
derivada_parcial = sp.diff(f_xy, x)
# Mostrar a derivada parcial
derivada_parcial
