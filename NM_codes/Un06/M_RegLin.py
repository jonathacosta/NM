#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Regressão linear'
Prof. Jonatha Costa
#"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# =============================================================================
def reglin(x,y,xint):
    '''
    Solução utilizando estrutura :  Sx ,Sy, Sxy, Sxx
    
    Equivalentes ao comando polyfit : px=np.polyfit(x,y,1)  
    '''
    # Teste de dimensão entre vetores
    if (len(x)!=len(y)): return print('Falha! X e Y tem dimensões diferentes!') 
    
    # Estrutura básica de regressão linear
    n=len(x)
    Sx ,Sy  = sum(x)   , sum(y)
    Sxy,Sxx = sum(x*y) , sum(x**2)
    a1=(n*Sxy-Sx*Sy)/(n*Sxx-Sx**2)
    a0=(Sxx*Sy-Sxy*Sx)/(n*Sxx-Sx**2)
    px=[a1,a0] 
        
    return px

def error_evaluation(x,y,px):
       
    # Cálculo do r2
    y_mean = np.mean(y)
    y2=np.polyval(px,x)
    ss_tot = sum((y - y_mean) ** 2)
    ss_res = sum((y - y2) ** 2)
    r2 = 1 - (ss_res / ss_tot)          
    r = round(np.sqrt(r2),4)*100
    return r2,r,y2
    
def results(r2,r,y2,xint,px,graph=1):    
    # Exibição de resultados
    yint=np.polyval(px,xint)
    print(f'O valor {xint} linearmente interpolado resulta em: {round(yint,2)}')          
    print(f"Coeficiente de determinação(r²):{round(r2,4)}",)
    print(f"Coeficiente de correlação (r):{r}%")
    
    if graph==1:
        m=sym.Symbol('m')
        p= round(px[0],4)*m+round(px[1],4)
        plt.title("Regressão Linear")        
        plt.plot(x,y,'*r',label='Medições')
        plt.plot(x,y2,'--b',label=p)
        plt.plot(xint,yint,'oy',label="yint",markersize=12)
        plt.legend()
        plt.style.use('ggplot')   

#%% Dados de entrada
x=np.array(list(range(0,110,10)))
y=np.array([ 0.94, 0.96, 1.0, 1.05, 1.07, 1.09, 1.14, 1.17, 1.21, 1.24, 1.28])
xint=30

# Solução 01
px = reglin(x,y,xint)
r2,r,y2 = error_evaluation(x,y,px)
results(r2,r,y2,xint,px,graph=1)

