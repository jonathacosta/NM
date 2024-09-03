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
def reglin(x,y,xint,graph=1):    
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
    yint=np.polyval(p,xint)
    print(np.polyval(p,xint))
    
    if graph==1:
        m=sym.Symbol('m')
        p= round(p[0],4)*m+round(p[1],4)
        plt.title("Regressão Linear")        
        plt.plot(x,y,'*r',label='Medições')
        plt.plot(x,y2,'--b',label=p)
        plt.plot(xint,yint,'oy',label="yint",markersize=12)
        plt.legend()
        plt.style.use('ggplot')   

def reglin_pol(x,y,xint,graph=1):
    
    px=np.polyfit(x,y,1)               # Coef. de p(x) proposto   
    y2=np.polyval(px,x)                # Imagem do novo domínio 
    k=sym.Symbol('k')
    yint=np.polyval(px,xint)
    f= round(px[0],4)*k+round(px[1],4)
    print(yint)    
    print(f)    
    
    if graph==1:        
        plt.figure()
        plt.title("Regressão Linear")        
        plt.plot(x,y,'*r',label='Medições')
        plt.plot(x,y2,'--b',label=f)
        plt.plot(xint,yint,'oy',label="yint",markersize=12)
        plt.legend()
        plt.style.use('ggplot')  


#%% Dados de entrada
x=np.array(list(range(0,110,10)))
y=np.array([ 0.94, 0.96, 1.0, 1.05, 1.07, 1.09, 1.14, 1.17, 1.21, 1.24, 1.28])
xint=70

# Solução 01
reglin(x,y,xint)
# Solução 02
reglin_pol(x,y,xint)
