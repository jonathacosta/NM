#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Interpolação de Lagrange
Prof. Jonatha Costa
"""
import numpy as np
# =============================================================================

def PolIntLagr(x,y,p):
    
    k=np.ones(len(x))                          # vetor de uns para 1ª elemento
    for i in range(len(x)):
        for j in range(len(x)):
            if (i!=j):          
                k[i]=k[i]*(p-x[j])/(x[i]-x[j])    
    Yint=sum(y*k)
    print('\nA aproximação encontrada para f(%.1f) = %.2f'%(p,Yint))
    return Yint

#%% =============================================================================
# Valores de entrada
if __name__=="__main__":
    
    x=np.array([1,2,4,5,7]); y=np.array([52,5,-5,-40,10])
    p=3

    PolIntLagr(x,y,p)
