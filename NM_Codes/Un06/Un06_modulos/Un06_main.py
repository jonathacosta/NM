#!/usr/bin/env python
# coding: utf-8
""" Métodos Numéricos - Unidade 06: Ajuste de curvas 

# ## Objeto:
# 
# * Apresentar conteúdo de Ajuste de Curvas
#     * Interpolação e extrapolação
#     * Regressão Linear por Mínimos Quadrados
#     * Linearização de Equações não lineares
#     * Polinômio de Lagrange e de Newton
#     * Spline Linear, quadrática e cúbica

# # Estrutura de classe
# ## Interpoladores
"""
from metodos import Resultados 
import numpy as np     

x=np.arange(0,110,10)
y=np.array([ 0.94, 0.96, 1.0, 1.05, 1.07, 1.09, 1.14, 1.17, 1.21, 1.24, 1.28])       
m = 3   # Grau do polinomio  
p = 12.7 
#p = float(input(f'\nInforme um ponto a interpolar no intervalo de x ({min(x)} e {max(x)}) ou <enter> para encerrar: '))  


if p <= min(x) or p >= max(x):
    print('Alerta!\nValor de entrada fora do domínio de X.')

curvas = Resultados(x, y, p, m)
lista = curvas.compare()
curvas.graf(lista)
