#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Prof.Jonatha Costa
Cálculo básico de integral com a biblioteca Scipy
Ver práticas em:
    https://scipy.org/
"""
from scipy.integrate import quad

#%% Q1
"""
Questão 01: Calcular a integral definida de uma função f(x)=x^2 
no intervalo de 0 a 2"""
# Definir a função
def f(x):
    return x**2
# Calcular a integral definida
resultado, erro = quad(f, 0, 2)
resultado
#%% Q2
'''
Questão 02 : Calcular a integral indefinida da função g(x)=sin⁡(x):
'''
import numpy as np
import scipy.integrate as integrate
# Definir a função
def g(x):
    return np.sin(x)
# Calcular a integral indefinida aproximada em um intervalo pequeno
a, b = 0, 1  # Intervalo pequeno para aproximação
resultado, erro = integrate.quad(g, a, b)
resultado

#%% Q3
'''
Questão 03: Calcular uma integral definida onde o limite superior é 
um parâmetro​.
'''
# Definir a função com parâmetro
def h(x, a):
    return np.exp(-x) * a
# Calcular a integral definida com parâmetro a
a = 2
resultado, erro = integrate.quad(h, 0, a, args=(a,))
resultado

#%% Q4
'''
Questão 04: Cálculo de uma integral dupla de f(x,y)=x2+y2 sobre o 
retângulo [0,1]×[0,2]:
'''
# Definir a função para a integral dupla
def f_xy(x, y):
    return x**2 + y**2
# Calcular a integral dupla
resultado, erro = integrate.dblquad(f_xy, 0, 1, lambda x: 0, lambda x: 2)
resultado

#%% Nota
'''
Note que:      ∫_0^2​(∫_0^1​(x^2+y^2)dx)dy
    
1) ∫_0^1​(x2+y2)dx=[x3/3​+y^2x]_0^1​= (1/3​+y^2)
    
2) ∫_0^2​(1/3​+y2)dy=[y/3​+y3/3​]_0^2= 2/3​+(2^3)/3​ = 2/​3+8/3​ = 10/3 = 3,333
   
'''