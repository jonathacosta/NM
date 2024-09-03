#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos
Integração via Métodos de retângulo,trapézio e ponto central
composto com variação da largura dos intervalos
Prof. Jonatha Costa
"""

import numpy as np
import scipy.integrate as integrate

def metod_retan(a,b,f,Ns:list=[10,100,1000]):
    '''
    Métodos de trapézio composto com variação da largura dos intervalos
    '''
    print("\nMétodo de retângulo composto:")    
    for j in Ns:    
        N=j                             #Total de intervalos
        h=(b-a)/N                       # Largura de cada intervalo
        x=np.arange(a,(b+h),h)          # Intervalo particionado a:h:b
        s=0
        for i in range(N):              # Retângulo composto
            s+=f(x[i])*h
        
        print(f'Solução para {N} partes é {round(s,4)}')     

def metod_p_central(a,b,f,Ns:list=[10,100,1000]):
    '''
    Métodos do ponto central composto com variação da largura dos intervalos
    '''
    print("\nMétodo do Ponto Central Composto")
    for j in Ns:    
        N=j                             #Total de intervalos
        h=(b-a)/N                       # Largura de cada intervalo
        x=np.arange(a,(b+h),h)          # Intervalo particionado a:h:b
        s=0
        for i in range(N):              # Ponto central composto
            s+=f((x[i+1] + x[i])/2)*h
        print(f'Solução para {N} partes é {round(s,4)}')     
        
def metod_trapz(a,b,f,Ns:list=[10,100,1000]):
    '''
    Métodos de trapézio composto com variação da largura dos intervalos
    '''
    print("\nMétodo de trapezio composto:")    
    for j in Ns:    
        N=j                             #Total de intervalos
        h=(b-a)/N                       # Largura de cada intervalo
        x=np.arange(a,(b+h),h)          # Intervalo particionado a:h:b
        s=0
        for i in range(N):              # Trapézio composto
            s+=0.5*( f(x[i]) + f(x[i+1]))*h
        print(f'Solução para {N} partes é {round(s,4)}')             
        
#%%
f=lambda x: 97000*x/(5*x**2 + 570000)
a,b = 40,93
Ns=[10,100,1000,10000,100000]

metod_retan(a,b,f,Ns)
metod_p_central(a,b,f,Ns)
metod_trapz(a,b,f,Ns)

#%% 
g,e=integrate.quad(f,a,b)
print(f'\nSolução analítica {round(g,4)}, via comando quad - scipy')     












