#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Prof.Jonatha Costa
Cálculo básico de limites com a biblioteca MpMath

O mpmath é particularmente útil para cálculos de alta 
precisão numérica. No entanto, diferentemente do SymPy, 
ele não é tão focado em manipulação simbólica, 
sendo mais indicado para cálculos numéricos complexos 
com precisão arbitrária.

Ver detalhes em:
    https://mpmath.org/

"""

from mpmath import limit, sin

#%% Q1
"""
Questão 01
Calcular o limite de uma função simples: lim⁡ (x→0) sin⁡(x)/x
"""
# Definir a função
def func(x):
    return sin(x) / x

resultado = limit(func,0)
print(resultado)

#%% Q2
'''
Questão 02
Calcular o limite de lim⁡x→∞ 1 / x^2
'''
# Definir a função
def func(x):
    return 1 / x**2
# Calcular o limite quando x tende ao infinito
resultado = limit(func, float('inf'))
print(resultado)
#%% Q3
'''
Questão 03
Calcular o limite lateral lim(x→0) ​1/x​.
'''
# Definir a função
def func(x):
    return 1 / x

# Calcular o limite lateral pela direita quando x tende a 0
resultado = limit(func, 0, direction=1)  # direction=1 para limite pela direita
print(resultado)
#%% Q4
'''
Questão 04
Calcular lim⁡(x→∞) (1+1/x)^x, que é uma forma de calcular o 
número de Euler e.
'''
def func(x):
    return (1 + 1/x)**x
# Calcular o limite quando x tende ao infinito
resultado = limit(func, float('inf'))
print(resultado)
#%% Q5
'''
    Calcular lim (⁡x→1) x2−1/ x−1​,
que resulta em uma forma indeterminada do tipo 0/0.

    Note que a função parece inicialmente problemá­tica no ponto x=1, 
pois substituindo diretamente o valor de x=1x=1 resulta em uma forma 
indeterminada 0/0​. 
    Para resolver isso, é necessário simplificar a expressão antes de calcular 
o limite, resultando na função simplificada é f(x)=x+1.
    As questõs anteriores seguem o mesmo raciocínio.       
'''
# Definir a função
def func(x):
    return (x**2 - 1) / (x - 1)
# Calcular o limite quando x tende a 1
resultado = limit(func, 1)
print(resultado)




