#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos
Integração via Métodos de retângulo,trapézio e ponto central
simples e composto
Prof. Jonatha Costa
"""

import numpy as np
import scipy.integrate as integrate

f=lambda x: 97000*x/(5*x**2 + 570000)
a,b = 40,93
Ns=[10,100,1000]
for j in Ns:    
    N=j  #Total de intervalos
    h=(b-a)/N                       # Largura de cada intervalo
    x=np.arange(a,(b+h),h)          # Intervalo particionado a:h:b
    s=0
    for i in range(N):              # Trapézio composto
        s+=0.5*( f(x[i]) + f(x[i+1]))*h
    print(f'\nSolução para {N} partes é {round(s,4)}')     

g,e=integrate.quad(f,a,b)
print(f'\nSolução analítica {round(g,4)}, via comando quad - scipy')     












