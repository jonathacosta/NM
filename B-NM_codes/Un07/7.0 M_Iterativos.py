#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações lineares
Métodos iterativos'
Prof. Jonatha Costa
"""

print('\014')
# =============================================================================
# Funções 
# =============================================================================
print('\n****** Método Iterativo de Jacobi ******\n')
x1,x2,x3,x4 = 0,0,0,0
a,b,c,err = 0,0,0, 0.001
n=20
print(' k \t  x1 \t  x2 \t  x3')

for k in range(1,n):
    a=(7-(2*x2+x3))/10;           # Atualiza a e usa Xi anterior
    b=(-8-(x1+x3))/5;             # Atualiza b e usa Xi anterior
    c=(6-(2*x1+3*x2))/10;         # Atualiza c e usa Xi anterior
    if((abs(x1-a) < err) and (abs(x2-b))<err and (abs(x3-c))<err):
        break
    x1,x2,x3 = a,b,c
    print('%2.d \t%.3f \t%.3f \t%.3f\n'%(k,x1,x2,x3))

print('\n***** Método Iterativo de Gauss-Seidal *****\n\n')
x1,x2,x3,x4 = 0,0,0,0
print(' k \t  x1 \t  x2 \t  x3')

for k in range(1,n):
    a , x1 = x1 , (7-(2*x2+x3))/10          # Guarda x1(k-1) em a;
    b , x2 = x2 , (-8-(x1+x3))/5;           # Guarda x2(k-1) em b;
    c , x3 = x3 , (6-(2*x1+3*x2))/10;       # Guarda x3(k-1) em c;
    if((abs(x1-a) < err) and (abs(x2-b))<err and (abs(x3-c))<err):
        break
    print('%2.d \t%.3f \t%.3f \t%.3f\n'%(k,x1,x2,x3))

















