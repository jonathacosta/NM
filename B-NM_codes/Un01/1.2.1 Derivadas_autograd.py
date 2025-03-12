#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Prof.Jonatha Costa
Cálculo básico de derivadas com a biblioteca AutoGrad

- O autograd é mais focado em diferenciação automática, o que é útil para 
otimização e aprendizagem de máquina, especialmente com redes neurais.
- Essa biblioteca é orientada para cálculos numéricos, diferente do SymPy,
 que é simbólico e pode manipular expressões algébricas.

Veja detalhes em: https://pypi.org/project/autograd/

Nota:
    O autograd requer que as variáveis de entrada sejam do tipo 
    float ou numpy array. Portanto, use f(3.0) em lugar de f(3).
"""

import autograd.numpy as np
from autograd import grad

#%% Q1
"""
Questão 01: Calcular a derivada de uma função simples, f(x)=x^2
"""
# Definir a função
def f(x):
    return x**2
# Calcular a derivada da função
df_dx = grad(f)
# Avaliar a derivada no ponto x = 3.0 (float)
resultado = df_dx(3.0)
resultado


#%% Q2
'''
Questão 02: Calcular a derivada de f(x)=sin⁡(x)f(x)=sin(x).
'''
# Definir a função
def f_trig(x):
    return np.sin(x)
# Calcular a derivada da função
df_dx = grad(f_trig)
# Avaliar a derivada no ponto x = 0.0 (float)
resultado_trig = df_dx(0.0)
resultado_trig

#%% Q3
'''
Questão 03: Calcular a segunda derivada de f(x)=x3+3x^2
'''
# Definir a função
def f2(x):
    return x**3 + 3*x**2
# Calcular a primeira derivada
df_dx = grad(f2)
# Calcular a segunda derivada
df_dx2 = grad(df_dx)
# Avaliar a segunda derivada no ponto x = 1.0 (float)
res_df_dx2 = df_dx2(1.0)
res_df_dx2

#%% Q4
'''
Questão 04: Calcular a derivada parcial de uma função de duas variáveis, 
f(x,y) = x^2+y^2, em relação a x.
'''
from autograd import elementwise_grad as egrad

# Definir a função de duas variáveis
def f_xy(x, y):
    return x**2 + y**2
# Calcular a derivada parcial em relação a x
grad_f_xy_x = egrad(f_xy, 0)
# Avaliar a derivada parcial no ponto (x=1.0, y=2.0)
resultado_parcial = grad_f_xy_x(1.0, 2.0)
resultado_parcial
#%% Nota
'''
Nota sobre Gradiente vs. Derivada:

   - Derivada: Para uma função de uma única variável f(x)f(x), a derivada 
   f′(x)f′(x) mede a taxa de variação de ff em relação a xx. É um número que 
   representa a inclinação da função em um ponto específico.
   
   - Gradiente: Quando temos uma função de várias variáveis, por exemplo,
   f(x,y)f(x,y), o gradiente é um vetor que contém todas as derivadas parciais 
   da função em relação a cada uma de suas variáveis. Portanto, o gradiente de 
   uma função f(x,y)f(x,y) é:
                     ∇f(x,y)=(∂x/∂f​,∂y/∂f​)

    O gradiente nos dá a direção da maior taxa de crescimento da função e 
    também indica o quão rápido a função está mudando nessa direção.

'''
