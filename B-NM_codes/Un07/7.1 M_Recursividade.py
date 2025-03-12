#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações lineares
Métodos e recursividade'
Prof. Jonatha Costa
"""
import numpy as np
print('\014')
# =============================================================================
# Sistema na forma matricial - Ax=b -> x=inv(A)*b
# -2x + 3y -z =  1
#   x + 2y -z =  4
# -2x -  y +z = -3

## =============================================================================
A=np.array([[-2,3,-1],
            [1,2,-1],
            [-2,-1,1]])
b=np.array([1,4,-3])

#%%
m1="Utilizando o comando solve - 'solve(A,b)'."
s1= np.linalg.solve(A,b)   
print(m1,'\n',s1)
print()
#%%
m2="Utilizando o comando 'inv(A)' e '@' - 'inv(A) @ b'"
s2=np.linalg.inv(A) @ b
print(m2,'\n',s2)
print()
#%%
m3="Utilizando o comando 'inv(A)' e 'np.dot' - dot( inv(A) , b  )"
s3=np.dot( np.linalg.inv(A) , b  )
print(m3,'\n',s3)
print()
#%% sympy
from sympy import Matrix
A1,b1 = Matrix(A), Matrix(b)
# Criar a matriz aumentada [A|b] utilizando Matrix do SymPy
augmented_matrix = A1.row_join(b1)
# Usar a função rref() para obter a forma escalonada reduzida por linhas
rref_matrix, pivot_columns = augmented_matrix.rref()
# Extrair a solução do sistema (última coluna da matriz resultante)
s4 = rref_matrix[:, -1]
m4="Utilizando o comando 'Matrix(A).rref()' do sympy para a forma escalonada."
print(m4,'\n',s4)
#%% Scipy
from scipy.linalg import lu,solve
# Decomposição LU
P, L, U = lu(A)
# Resolvendo o sistema Ld = b (substituição progressiva)
d = solve(L, b, lower=True)
# Resolvendo o sistema UI = d (substituição regressiva)
x = solve(U, d)
# print("Matriz de permutação P:\n", P)
# print("Matriz triangular inferior L:\n", L)
# print("Matriz triangular superior U:\n", U)
print("\nSolução do sistema por fatoração LU:\n", x)

'''
Nota:
    - Métodos diferentes, como a decomposição LU, podem produzir
    soluções diferentes se houver erros numéricos ou se o sistema 
    não tiver uma solução única.
        
    - A decomposição LU é geralmente mais adequada para sistemas 
    que têm uma solução única e bem comportada, enquanto o método 
    RREF pode fornecer mais detalhes sobre a natureza das soluções,
    incluindo possíveis dependências entre variáveis.
    
    - O método rref() pode revelar informações sobre a consistência 
    do sistema e possíveis soluções infinitas ou nenhum resultado 
    (caso o sistema seja inconsistente). Já a decomposição LU 
    normalmente assume que o sistema tem uma solução única e não 
    verifica diretamente a consistência.
    
    - O sistema abaixo, por exemplo, ter respostas convergentes em 
    todos os métodos acima.    
    
    A=np.array([[3.,1.,0.,-1.],
                [1.,3.,1.,1.],
                [0.,1.,3.,-1.],
                [-1.,1.,-1.,4.]])
    b = np.array([10.,15.,10.,0.])
    
'''


