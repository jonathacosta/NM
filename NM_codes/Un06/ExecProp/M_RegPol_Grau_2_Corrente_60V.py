#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Regressão Polinomial - grau 2
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
def calc_regpol_g2(x,y,ponto_reg=60,graph=1):    
        
    if (len(V)!=len(I)) : 
        print('Falha! V e I tem dimensões diferentes!');         
    elif ((ponto_reg < min(x)) or (ponto_reg > max(x))) :
        print(f"Ponto de entrada fora da faixa de análise: min: {min(x)} |--| max: {max(x)}") 
    else:
      n=len(x)
      # Somatórios necessários à matriz 
      Sx , Sy  = sum(x) , sum(y)
      Sx2 = np.sum(x * x)
      Sx3 = np.sum(x * x * x)
      Sx4 = np.sum(x * x * x * x)
      Sxy = np.sum(x * y)
      Sx2y = np.sum(x * x * y)    
      
      # Matriz A e vetor b
      A = np.array([[n, Sx, Sx2],
                    [Sx, Sx2, Sx3],
                    [Sx2, Sx3, Sx4]])

      b = np.array([Sy, Sxy, Sx2y])

      # Resolução do sistema linear para encontrar os coeficientes c
      a0, a1, a2 = np.linalg.solve(A, b)           
      p=[a2, a1,a0]
      
      y2=np.polyval(p,x)
      # Cálculo do coeficiente de determinação R^2
      y_mean = np.mean(y)
      ss_tot = sum((y - y_mean) ** 2)
      ss_res = sum((y - y2) ** 2)
      r2 = 1 - (ss_res / ss_tot)      
      r = round(np.sqrt(r2),4)*100
      
      print(np.polyval(p,ponto_reg))
      print(f"Coeficiente de determinação:{round(r2,4)}",)
      print(f"Coeficiente de correlação:{r}%")
      
      #%Grafico
    if graph==1:
        m=sym.Symbol('m')
        y_reg=np.polyval(p,ponto_reg)
        p= round(p[0],4)*m**2+round(p[1],4)*m+round(p[2],4)
        print(p)
        # print(np.polyval(p,70))
        plt.style.use('ggplot')     

        plt.title("Regressão Linear")
        plt.plot(x,y,'*r',label='Medições')
        plt.plot(x,y2,'--b',label=p)
        plt.plot(ponto_reg,y_reg,'oy',label="ponto_reg",markersize=12)
        plt.text(0,70, f'$R^2 = {round(r2,2)}$', fontsize=12)
        plt.legend(fontsize=18)
        plt.legend()
        plt.show()
        
#%%
V = np.array([0,10,20,30,40,50,70,80,90])
I = np.array([0,10,19,31,39,52,65,69,70])

calc_regpol_g2(V,I,60,graph=1)


