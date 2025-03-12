#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Prof.Jonatha Costa
Cálculo básico de limites com a biblioteca Sympy
Ver práticas em:
    https://docs.sympy.org/latest/explanation/best-practices.html

"""

from sympy import Symbol, sin, limit,oo
x = Symbol('x')

#%%
"""
Questão 01
Calcular o limite de uma função simples: lim⁡ (x→0) sin⁡(x)/x
"""
# Definir a variável simbólica
x = Symbol('x')
# Definir a função
func = sin(x)/x
# Calcular o limite quando x tende a 0
resultado = limit(func, x, 0)
print(resultado)

#%%
'''
Questão 02
Calcular o limite de lim ⁡x→∞ 1 / x^2
'''
# Definir a função
func = 1/x**2
# Calcular o limite quando x tende ao infinito
resultado = limit(func, x, oo)
print(resultado)
#%%
'''
Questão 03
Calcular o limite lateral lim(x→0) ​1/x​.
'''
# Calcular o limite lateral pela direita quando x tende a 0
resultado = limit(1/x, x, 0, dir='+')
print(resultado)
#%%
'''
Questão 04
Calcular lim⁡(x→∞) (1+1/x)^x, que é uma forma de calcular o 
número de Euler e.
'''
# Definir a função
func = (1 + 1/x)**x
# Calcular o limite quando x tende ao infinito
resultado = limit(func, x, oo)
print(resultado)
#%%
'''Calcular lim (⁡x→1) x^2 − 1/x−1​,
que resulta em uma forma indeterminada do tipo 0/0.

'''
# Definir a função
func = (x**2 - 1)/(x - 1)
# Calcular o limite quando x tende a 1
resultado = limit(func, x, 1)
print(resultado)




