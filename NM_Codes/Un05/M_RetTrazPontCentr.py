#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos
Integração via Métodos de retângulo,trapézio e ponto central
simples e composto
Prof. Jonatha Costa
"""
import numpy as np
#import matplotlib.pyplot as plt
print('\14')
# =============================================================================

f=lambda x: 97000*x/(5*x**2 + 570000)
a,b=40,93
# =============================================================================
N=100                           # Total de intervalos
h=(b-a)/N                       # Largura de cada intervalo
x=np.arange(a,(b+h),h)          # Intervalo particionado a:h:b
I=[]

s=f(a)*(b-a)                    #  Retângulo simples extremo a
I.append(s); s=0
s=f(b)*(b-a)                    #  Retângulo simples extremo b            
I.append(s); s=0
s=f((a+b)/2)*(b-a)              # Ponto central
I.append(s); s=0
s=((f(a)+f(b))/2)*(b-a)         # Trapézio Simples
I.append(s); s=0
for i in range(N):              # Retângulo composto
   s+=f(x[i])*h
I.append(s); s=0
for i in range(N):              # Ponto central composto
   s+=f((x[i+1] + x[i])/2)*h
I.append(s); s=0
for i in range(N):              # Trapézio composto
   s+=0.5*( f(x[i]) + f(x[i+1]))*h
I.append(s); s=0
M=["Retângulo simples altura 'a'","Retângulo simples altura 'b'",
   'Ponto central','Trapézio Simples','Retângulo composto',
   'Ponto central composto','Trapézio composto']
for i in range(len(I)):
     print(round(I[i],4),' >> Método:',M[i])

import scipy.integrate as integrate
g,e=integrate.quad(f,a,b)
print(f'\nSolução analítica {round(g,4)}, via comando quad - scipy')     

