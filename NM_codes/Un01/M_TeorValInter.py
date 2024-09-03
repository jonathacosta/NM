#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mon Apr 19 11:21:18 2021
@author: Jonatha Rodrigues da Costa
"""
import numpy as np
import matplotlib.pyplot as plt
print('\14')
# Teorema da valor intermediário
def f(x):
    return x**4 + 2.*x+4.

def grap(x,y): 
#    plt.figure()
    plt.plot(x0,y0,label='f(x)')
    plt.plot(x1,y1,'g*',label='x aleatório')
    plt.title("Teorema do valor intermediário")
    plt.legend()
    plt.style.use('ggplot')

a=1.;b=2.; 
x1 = a+np.random.random()
y1 = f(x1)

# Teste do teorema
if  ( f(x1)>f(a) and f(x1)<f(b) ):
    print("Polinômio tem raíz no intervalo [",a,",",b,"]")
else:
    print("Polinômio tem não raíz no intervalo!") 


#%% Saída Gráfica 01
x0= np.linspace(a,b)
y0=f(x0) 
grap(x0,y0)

#%% Saída Gráfica 02 - com 5 pontos aleatórios

#x0,y0 = np.linspace(a,b),f(x0) 
#x1=[]     # Usando tuplas 
#for i in range(5):
#    s=(a+np.random.random())
#    x1.append(s)              # Comando exclusivo de lista
#x1=np.array(x1)

x0,y0 = np.linspace(a,b),f(x0) 
x1=np.array([ a+np.random.random() for i in range(5)  ])
y1=f(x1)   
grap(x0,y0)

#%% Saída 03 - com 3 pontos aleatórios











