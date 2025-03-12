#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Interpolação via spline linear'
Prof. Jonatha Costa


Conceito basilar:
    Um spline linear é uma forma simples de interpolação que utiliza uma sequência
    de segmentos de reta para conectar um conjunto de pontos dados, conhecidos 
    como nós (ou "knots"). A ideia é interpolar valores entre esses nós utilizando 
    uma função linear em cada intervalo. Isso é muito útil em muitas aplicações,
    porque é uma forma rápida e eficiente de obter aproximações contínuas, mesmo
    que não sejam suavizadas como em outros tipos de splines (por exemplo, 
    splines cúbicos).

Definição:
    Dado um conjunto de n+1n+1 pontos (x0,y0),(x1,y1),…,(xn,yn), o spline linear 
    é composto de nn funções lineares, uma para cada intervalo [xi,xi+1], 
    que são definidas da seguinte forma:
                
        Si(x) = yi + ( (y(i+1)−yi)/(x(i+ 1)−xi)) (x−xi), para xi ≤ x ≤ xi+1

Aqui, Si(x) é a equação da reta que passa pelos pontos (xi,yi) e (xi+1,yi+1).
Em cada intervalo, temos uma função linear que conecta os pontos adjacentes.


"""
# =============================================================================
def sp_lin(x,y,xint):
    '''
    Encontrar o intervalo que contém o valor de xint.
    '''
    for i in range(1,len(x)):        
        if (xint < x[0] and xint >x[-1]):
            print('Erro!\nInterpolação fora do intervalo.')
        elif xint<x[i+1]:
            i+=1            # Intervalo
        break
    yint=(xint-x[i])* y[i-1]/ (x[i-1]-x[i]) + (xint-x[i-1])*y[i]/(x[i]-x[i-1]) 

    return yint

# =============================================================================
if __name__ == "__main__":    
    from A_fun import graph_sp
    
    x=[8,11,15,18]; y=[5,9,10,8]
    xint=12.7    
    yint=sp_lin(x,y,xint)
    print('\nA aproximação encontrada para f(%.1f) = %.2f'%(xint,yint))
    graph_sp(x,y,xint,yint,'linear')
    