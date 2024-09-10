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

Perceba que a solução é realiza utilizando-se os métodos desenvolvidos
no exercício anterior, presentes no módulo M_RegPol.

"""

#%%
import numpy as np
from M_RegPol import RegPol,error_evaluation,results
# Definição de valores de entrada
x = np.array([0,10,20,30,40,50,70,80,90])# V
y = np.array([0,10,19,31,39,52,65,69,70]) # I
xint=60
# Evocando atributos e métods
m=2                              # Grau do polinômio    
# Evocando atributos e métods
px = RegPol(x,y,m)
r2,r,y2 = error_evaluation(x,y,px)
results(r2,r,y2,xint,x,y,px,graph=1)
