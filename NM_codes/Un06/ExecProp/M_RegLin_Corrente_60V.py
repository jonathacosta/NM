#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Regressão linear'
Prof. Jonatha Costa

Um engenheiro foi à bancada do laboratório de medidas elétricas e
obteve dados de tensão e corrente. Ele esqueceu de medir a corrente
para 60V. Como transformar os dados pontuais numa curva, ou seja,
uma tendência de comportamento do circuito elétrico estudado?
V (V) = [0,10,20,30,40,50,70,80,90]
I (A) = [0,10,19,31,39,52,65,69,70]
#"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
# =============================================================================
#  Valores de entrada
def calc_reglin(x,y,ponto_reg=60,graph=1):    
        
    if (len(V)!=len(I)) : 
        print('Falha! V e I tem dimensões diferentes!'); 
        
    elif ((ponto_reg < min(x)) or (ponto_reg > max(x))) :
        print(f"Ponto de entrada fora da faixa de análise: min: {min(x)} |--| max: {max(x)}") 
    else:
      n=len(x)
      Sx ,Sy  = sum(x)   , sum(y)
      Sxy,Sxx = sum(x*y) , sum(x**2)
      Syy = sum(y**2)
      a1=(n*Sxy-Sx*Sy)/(n*Sxx-Sx**2)
      a0=(Sxx*Sy-Sxy*Sx)/(n*Sxx-Sx**2)
      p=[a1,a0]
      y2=np.polyval(p,x)
      r2=((n*Sxy-Sx*Sy)/np.sqrt(n*Sxx-Sx**2)/np.sqrt(n*Syy-Sy**2))**2;
      print(np.polyval(p,ponto_reg))
      print("Coeficiente de determinação:", round(r2,2))
      print("Coeficiente de correlação:",round((r2**0.5),2)*100,'%')
      
      #%Grafico
    if graph==1:
        m=sym.Symbol('m')
        y_reg=np.polyval(p,ponto_reg)
        p= round(p[0],4)*m+round(p[1],4)
        print(p)
        # print(np.polyval(p,70))
        plt.title("Regressão Linear")
        plt.plot(x,y,'*r',label='Medições')
        plt.plot(x,y2,'--b',label=p)
        plt.plot(ponto_reg,y_reg,'oy',label="ponto_reg",markersize=12)
        plt.text(0.75, 0.05, f'$R^2 = {round(r2,2)}$', fontsize=12, transform=plt.gca().transAxes)
        plt.legend(fontsize=18)
        plt.legend()
        plt.show()
        plt.style.use('ggplot')

#%%
V = np.array([0,10,20,30,40,50,70,80,90])
I = np.array([0,10,19,31,39,52,65,69,70])
calc_reglin(V,I,60,graph=1)


