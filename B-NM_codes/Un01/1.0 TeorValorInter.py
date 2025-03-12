#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mon Apr 19 11:21:18 2021
Prof. Jonatha Costa

Código básico com implementação do teorema do valor intermediário para
uma função f(x).
"""
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
def Inter_Val(f,a,b,x,graph=1):
    '''
    Dado um valor de 'x', pertencente ao domínio [a,b], este método 
    verifica se o valor de f(x) pertence ao contra-domínio [f(a),f(b)]    
    '''    
    
    if  ( f(x)>f(a) and f(x)<f(b) ):
        print("Polinômio tem raíz no intervalo, visto que é satisfeita a condição f(x)>f(a) and f(x)<f(b)\n")
        print(f"f({a}) = {f(a)}")
        print(f"f({round(x,1)}) = {round(f(x),1)}")
        print(f"f({b}) = {f(b)}")
    
    if graph==1: 
        x0 = np.linspace(a,b);y0=f(x0) 
        plt.plot(x0,y0,'--',label='f(x)')
        plt.plot(x,f(x),'o',label='x aleatório',markersize=12)
        plt.title("Teorema do valor intermediário")
        plt.legend()
        plt.style.use('ggplot')            

    else:
        print("Polinômio não tem raíz no intervalo [",a,",",b,"]")
   

# =============================================================================
def f(x):
    return -x**4 + 2.*x + 4.

if __name__ == "__main__":
    a,b =0, 2;                           # Intervalo de base
    for i in range(1):                   # 'n' pontos diversos
        x1 = a+np.random.random()        # x | a < x < b
        Inter_Val(f,a,b,x1)              # 











