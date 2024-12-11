#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações lineares
Resolva o sistema de equações lineares Ax = b usando eliminação de Gauss.
Prof. Jonatha Costa
---------------------------------------------
Dado um circuito elétrico, calcule a corrente no resistor R5.
As fontes têm valor de V1 = 10 V, V2 = 15 V e V3 = 10 V. Os resistores
são iguais e tem valor de 1 Ω.

O circuito elétrico pode ser equacionado pela lei das
tensões de Kirchhoff.

(𝑅1 + 𝑅2 + 𝑅8 )𝐼1 + 𝑅2 𝐼2 + 0𝐼3 − 𝑅8 𝐼4 = 𝑉1
𝑅2 𝐼1 + (𝑅2 + 𝑅3 + 𝑅5 )𝐼2 + 𝑅3 𝐼3 + 𝑅5 𝐼4 = 𝑉2
0𝐼1 + 𝑅3 𝐼2 + (𝑅3 + 𝑅4 + 𝑅6 )𝐼3 − 𝑅6 𝐼4 = 𝑉3
{ −𝑅8 𝐼1 + 𝑅5 𝐼2 − 𝑅6 𝐼3 + (𝑅5 + 𝑅6 + 𝑅7 + 𝑅8 )𝐼4 = 0        
---------------------------------------------        
"""
import numpy as np

def gauss_elimination(A, b):   
    n = len(b)
    # Aplicando eliminação para obter uma matriz triangular superior
    for i in range(n):
        # Pivotação parcial (caso o pivô seja zero ou próximo a zero)
        if abs(A[i, i]) < 1e-12:
            for k in range(i + 1, n):
                if abs(A[k, i]) > abs(A[i, i]):
                    A[[i, k]] = A[[k, i]]
                    b[i], b[k] = b[k], b[i]
                    break        
        # Eliminação
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]    
    # Resolução por substituição regressiva
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]    
    return x

#%% Utilizando Eliminação de Gauss.
# Matriz A 4x4
A=np.array([[3.,1.,0.,-1.],
            [1.,3.,1.,1.],
            [0.,1.,3.,-1.],
            [-1.,1.,-1.,4.]])

# Matriz de constantes
b = np.array([10.,15.,10.,0.])
# Matriz de coeficientes (i1,i2,i3,i4)
x = gauss_elimination(A, b)
print("Solução utilizango Eliminação de Gauss\n", x)

#%% Utilizando fatoração LU
from scipy.linalg import lu,solve
P, L, U = lu(A)
# Resolvendo o sistema Ld = b (substituição progressiva)
d = solve(L, b, lower=True) 
# Resolvendo o sistema UI = d (substituição regressiva)
I = solve(U, d)
m4="Utilizando o comando 'lu(A)' do scipy - P, L, U = lu(A)"
print('\n',m4,'\n',I)
