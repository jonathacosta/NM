#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Integração via Métodos de 1/3 de Simpson simples e composto
Prof. Jonatha Costa
"""
import numpy as np
#import matplotlib.pyplot as plt
print('\14')
# =============================================================================

f=lambda x: 97000*x/(5*x**2 + 570000)
a,b=40,93
h=(b-a)/2    
# =============================================================================
x=np.arange(a,(b+h),h)           # Intervalo particionado a:h:b
I=[]
N=100
# =============================================================================
# #  1/3 de Simpson simples 
# =============================================================================
h=(b-a)/2                                 # Largura de cada intervalo
s=h/3*(f(a)+4*f((a+b)/2)+f(b))            
I.append(s); s=0

# =============================================================================
# #  3/8 de Simpson simples 
# =============================================================================
h=(b-a)/3
s=(3*h/8)*(f(a)+3*f(a+h)+3*f(a+2*h)+f(b))            
I.append(s); s=0

# =============================================================================
# #  1/3 de Simpson composto 
# =============================================================================
if (N%2)!=0:                            # Validar número par de intervalos
    N=N+1
h=(b-a)/N
x=np.arange(a,(b+h),h)                  # Atualizar x em funçaõ de h intervalos
for i in range(1,N):
    if i%2==0:
        s+=4*f(x[i])
    else:
        s+=2*f(x[i])
I.append( (f(a)+s+f(b))*h/3  )

# =============================================================================
# #  3/8 de Simpson composto              # N div 3
# =============================================================================
while (N%3)!=0:                         # Validar número par de intervalos
    N=N+1
h=(b-a)/N
x=np.arange(a,(b+h),h)                  # Atualizar x em funçaõ de h intervalos
p1,p2=0,0
for i in (np.arange(1,N,3)):
    p1+=3*( f(x[i])+f(x[i+1]) )
for i in (np.arange(4,N,3)):
    p2+=2*f(x[i])
I.append( (f(a) + p1 + p2 + f(b))*h*3/8 )     

M=["1/3 de Simpson simples ","3/8 de Simpson simples ",
   "1/3 de Simpson composto ","3/8 de Simpson composto "]
for i in range(len(I)):
     print(round(I[i],4),' >> Método:',M[i])
#
import scipy.integrate as integrate
g,e=integrate.quad(f,a,b)
print(f'\nSolução analítica {round(g,4)}, via comando quad - scipy')  
#
#
#
#
#
#
#
#
#














































