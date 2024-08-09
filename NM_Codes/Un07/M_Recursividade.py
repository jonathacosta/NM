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
l1=[-2,3,-1]
l2=[1,1.2,-1]
l3=[-2,-1,1]
lb=[1,4,-3]
A=np.array([l1+l2+l3]).reshape(3,3)
b=np.array(lb).reshape(3,1) # ou b=np.array([ [1],[4],[3]  ])

m1="Utilizando o comando solve - 'solve(A,b)'."
s1= np.linalg.solve(A,b)   
print(m1,'\n',s1)
print()

m2=" Utilizando o comando 'inv(A)' e '@' - 'inv(A) @ b'"
s2=np.linalg.inv(A) @ b
print(m2,'\n',s2)
print()

m3=" Utilizando o comando 'inv(A)' e 'np.dot' - dot( inv(A) , b  )"
s3=np.dot( np.linalg.inv(A) , b  )
print(m3,'\n',s3)
print()

# =============================================================================
# Scipy
# =============================================================================
from scipy.linalg import lu
P, L, U = lu(A)
m4=" Utilizando o comando 'lu(A)' do scipy - P, L, U = lu(A)"
print(m4,'\n\n',P,'\n\n',L,'\n\n',U)
print()

# =============================================================================
#  Sympy
# =============================================================================
#%%
from sympy import Matrix
m5="Utilizando o comando 'Matrix(A).rref()' do sympy para a forma escalonada."
A1=np.array([-2,3,-1, 1,  1,1.2,-1, 4,  -2,-1,1,-3]).reshape(3,4)
s5=Matrix(A1).rref()
print(m5,'\n',s5)

# Sugestão de otimização: Automatizar a passagem para matriz A homogênea!!!

















