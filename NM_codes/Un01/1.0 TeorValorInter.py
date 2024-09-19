#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mon Apr 19 11:21:18 2021
@author: Jonatha Rodrigues da Costa
"""
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
def Inter_Val(f,a,b,x,graph=1):
    if  ( f(x)>f(a) and f(x)<f(b) ):
        print("Polinômio tem raíz no intervalo [",a,",",b,"]")
    else:
        print("Polinômio tem não raíz no intervalo!") 

    if graph==1: 
        x0 = np.linspace(a,b);y0=f(x0) 
        plt.plot(x0,y0,'--',label='f(x)')
        plt.plot(x,f(x),'o',label='x aleatório',markersize=12)
        plt.title("Teorema do valor intermediário")
        plt.legend()
        plt.style.use('ggplot')

# =============================================================================
def f(x):
    return x**4 + 2.*x+4.

if __name__ == "__main__":
    a,b =1, 2;                           # Intervalo de base
    for i in range(5):                   # 5 pontos diversos
        x1 = a+np.random.random()        # x | a < x < b
        Inter_Val(f,a,b,x1)              # 











