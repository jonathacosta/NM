#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Interpolação de Newton
Prof. Jonatha Costa
"""
# =============================================================================
import numpy as np

def PolInterNewton(x,y,p):    
    a,s= [y[0]],y                                # s é vetor das divisoes
    for i in range(len(x)-1):
        y=s                                      # Atualiza o vetor y
        s=(y[1:]-y[:-1])/(x[(1+i):]-x[:-(1+i)])  # Reduz o vetor x
        a.append(s[0])    
    xn,Yint=1,a[0]
    for k in range(1,len(x)):
        xn=xn*(p - x[k-1])
        Yint=Yint+a[k]*xn
    print('\nA aproximação encontrada para f(%.1f) = %.2f'%(p,Yint))
    return Yint

#%%
if __name__=="__main__":
    
    x=np.array([1,2,4,5,7]);  y=np.array([52,5,-5,-40,10])
    p=3
    
    PolInterNewton(x,y,p)