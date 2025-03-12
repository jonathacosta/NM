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

Perceba que a solução é realiza utilizando-se os métodos desenvolvidos
no exercício anterior, presentes no módulo M_RegLin.

"""

import numpy as np
from M_RegLin import reglin,results
import A_error_analyzer as ea

# Definição de valores de entrada
x = np.array([0,10,20,30,40,50,70,80,90])# V
y = np.array([0,10,19,31,39,52,65,69,70]) # I
xint=60
# Evocando atributos e métods
px = reglin(x,y,xint)
# Chamadas de métodos
y_pred = np.polyval(px, x)
r2 = ea.r2(y, y_pred)
# Chamada de resultados e gráficos
results(r2,y_pred,xint,x,y,px,graph=1)







