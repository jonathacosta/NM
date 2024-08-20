#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Interpolação de Lagrange'
Prof. Jonatha Costa
"""
import numpy as np
# =============================================================================
x=np.array([1,2,4,5,7])
y=np.array([52,5,-5,-40,10])
#%% OPÇÃO 01===================================================================
p=3
k=np.ones(len(x))                          # vetor de uns para 1ª elemento
for i in range(len(x)):
    for j in range(len(x)):
        if (i!=j):          
            k[i]=k[i]*(p-x[j])/(x[i]-x[j])    
Yint=sum(y*k)
print(Yint)

#%% OPÇÃO 02 ==================================================================
print('\014')
p=3
l=[]                          
for i in range(len(x)):
    k=1                          # Valor inicial para primeiro produto
    for j in range(len(x)):
        if (i!=j):          
            k=k*(p-x[j])/(x[i]-x[j])
    l.append(k)                 # Armazenamento dos vetores
Yint=sum(y*np.array(l))
print(Yint)






