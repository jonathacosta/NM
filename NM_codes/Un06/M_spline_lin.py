#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Interpolação via spline linear'
Prof. Jonatha Costa
"""
import matplotlib.pyplot as plt
# =============================================================================
def spline(x,y,xint):
    for i in range(len(x)):
        if (xint < x[0] and xint >x[-1]):
            print('Erro!\nInterpolação fora do intervalo.')
        elif xint<x[i+1]:
            i+=1
            break
    yint=(xint-x[i])* y[i-1]/ (x[i-1]-x[i]) + (xint-x[i-1])*y[i]/(x[i]-x[i-1]) 
    print('\nA aproximação encontrada para f(%.1f) = %.2f'%(xint,yint))
    
    plt.plot(x,y,'b',label='Pontos de medição')
    plt.plot(xint,yint,'r*',label='y interpolado')
    plt.legend()
    plt.title('Interpolação via spline linear')
    plt.style.use('ggplot')
        
# =============================================================================
x=[8,11,15,18]; y=[5,9,10,8]
xint=12.7    
spline(x,y,xint)