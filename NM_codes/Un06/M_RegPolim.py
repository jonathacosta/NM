#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Regressão Polinomial
Prof. Jonatha Costa

 =============================================================================
# p(x)=a_m*x**m + a_(m-1)x**(m-1)+...+a1x + a0
# =============================================================================
# f = lambda x: x**2+2*x -3           # Função de referência comparativa
# x = np.linspace(0,5,10)             # Pontos do domínio avaliado
# y=f(x) 

"""
import numpy as np
import matplotlib.pyplot as plt
from fun import pol

#%%=============================================================================

def RegPol(x,y,grau,graph=1):
    '''
    Regressão Polinomial - Soluções via comandos polyval e polyfit
    '''        
    c=np.polyfit(x,y,grau)               # Coef. de p(x) proposto   
    v=np.polyval(c,x)                 # Imagem do novo domínio
    print(f'\nO polinômio proposto para os pontos dados, com grau {grau}, é:\np(x)= {pol(c)}')
    if graph==1:
        plt.plot(x,y,'r*',label='Pontos de medição - Referência')
        plt.plot(x,v,'bo',label=f'Polinomino proposto com grau {grau}')
        plt.title('Gráfico básico com polyfit e polyval')
        plt.style.use('ggplot');plt.grid(visible='on');
        plt.legend();plt.show()

def RegPol_Matr(x,y,grau,graph=1):
    '''
    Regressão Polinomial - Soluções via matrizes Ax=B
    '''        
    A=np.eye(grau+1)                      # Matriz A
    for i in range(grau+1):
        for j in range(grau+1):     
            A[i,j] = sum(x**(i+j))
            
    B=np.zeros(grau+1)                   # Vetor da matriz B
    for i in range(grau+1):
        B[i]=sum((x**i)*y)
       
    px=(list(np.linalg.solve(A,B)))   # Vetor de coeficientes de p(x)
    px.reverse()  
    print(f'O polinômio proposto para os pontos dados é:\np(x)= {pol(px)}')
    
    if graph==1:
        v=np.polyval(px,x)                 # Imagem do novo domínio
        plt.plot(x,y,'r*',label='Pontos de medição - Referência')
        plt.plot(x,v,'bo',label=f'Polinomino proposto com grau {grau}')
        plt.title('Gráfico básico com polyfit e polyval')
        plt.style.use('ggplot');plt.grid(visible='on');
        plt.legend();plt.show()
        
#%%TESTE=============================================================================
x=np.array(list(range(0,110,10)))
y=np.array([ 0.94, 0.96, 1.0, 1.05, 1.07, 1.09, 1.14, 1.17, 1.21, 1.24, 1.28])
m=4                              # Grau do polinômio

RegPol(x,y,m,graph=1)
RegPol_Matr(x,y,m,graph=1)

#%% 



