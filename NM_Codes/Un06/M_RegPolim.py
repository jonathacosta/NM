#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Regressão Polinomial'
Prof. Jonatha Costa
"""
import numpy as np
import matplotlib.pyplot as plt
from fun import pol
# =============================================================================
# p(x)=a_m*x**m + a_(m-1)x**(m-1)+...+a1x + a0
# =============================================================================
# f = lambda x: x**2+2*x -3           # Função de referência comparativa
# x = np.linspace(0,5,10)             # Pontos do domínio avaliado
# y=f(x) 

x=np.array(list(range(0,110,10)))
y=np.array([ 0.94, 0.96, 1.0, 1.05, 1.07, 1.09, 1.14, 1.17, 1.21, 1.24, 1.28])


                             # Pontos da imagem avaliada 
print('\014')
# =============================================================================
# Regressão Polinomial - Soluções via matrizes Ax=B
# =============================================================================
m=6                               # Grau do polinôminio
n=len(x)                           # Quantidade de pontos

A=np.eye(m+1)                      # Matriz A
for i in range(m+1):
    for j in range(m+1):     
        A[i,j] = sum(x**(i+j))
        
B=np.zeros(m+1)                   # Vetor da matriz B
for i in range(m+1):
    B[i]=sum((x**i)*y)
   
px=(list(np.linalg.solve(A,B)))   # Vetor de coeficientes de p(x)
px.reverse()  
px=[round(px[i],100) for i in range(len(px))]                        
px=np.array(px)                   # Vetor de coeficientes de p(x) ordenado
sol=pol(px)
print(f'O polinômio proposto para os pontos dados é:\np(x)= {sol}')
# =============================================================================
y2=np.polyval(px,x)               # Imagem de x no polinômio proposto
plt.title('Comparativo com regressão Polinomial')
plt.plot(x,y,'r*',label='Pontos de medição - Referência')
plt.plot(x,y2,'b',label='f')
plt.legend()
plt.style.use('ggplot')
plt.show()


# %%=============================================================================
# # Regressão Polinomial - Soluções via comandos polyval e polyfit
# =============================================================================
c=np.polyfit(x,y,m)               # Coef. de p(x) proposto   
v=np.polyval(c,x)                 # Imagem do novo domínio

plt.plot(x,v,'b-',label='f'); 
plt.plot(x,y,'o',label='x aleatório'); 
plt.legend();
plt.title('Gráfico básico com polyfit e polyval')
plt.show()
