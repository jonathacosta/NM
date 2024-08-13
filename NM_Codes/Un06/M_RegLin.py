#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Regressão linear'
Prof. Jonatha Costa
#"""
import numpy as np
import matplotlib.pyplot as plt
print('\014')
# =============================================================================
#  Valores de entrada
# =============================================================================
x=np.array(list(range(0,110,10)))
y=np.array([ 0.94, 0.96, 1.0, 1.05, 1.07, 1.09, 1.14, 1.17, 1.21, 1.24, 1.28])

if (len(x)!=len(y)): 
  print('Falha! X e Y tem dimensões diferentes!') 
else:
  n=len(x)
  Sx ,Sy  = sum(x)   , sum(y)
  Sxy,Sxx = sum(x*y) , sum(x**2)
  a1=(n*Sxy-Sx*Sy)/(n*Sxx-Sx**2)
  a0=(Sxx*Sy-Sxy*Sx)/(n*Sxx-Sx**2)
p=[a1,a0]
y2=np.polyval(p,x)
print(np.polyval(p,70))
#%%
import sympy as sym
m=sym.Symbol('m')
p= round(p[0],4)*m+round(p[1],4)
print(p)
# print(np.polyval(p,70))
plt.title("Regressão Linear")
plt.plot(x,y,'*r',label='Medições')
plt.plot(x,y2,'--b',label=p)
plt.legend()
plt.show()
plt.style.use('ggplot')

#%%=============================================================================
# Utilizando o polyval e polyfit
# =============================================================================

c=np.polyfit(x,y,1)               # Coef. de p(x) proposto   
p=np.linspace(0,100,10)           # Novo domínio para teste
v=np.polyval(c,p)                 # Imagem do novo domínio
    
import sympy as sym
k=sym.Symbol('k')
f= round(c[0],4)*k+round(c[1],4)
print(f)

plt.plot(p,v,'r-',label=f); 
plt.plot(x,y,'o',label='x aleatório'); 
plt.legend();
plt.title('Gráfico básico com polyfit e polyval')
plt.show()

