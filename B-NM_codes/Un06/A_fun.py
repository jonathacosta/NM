#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Thu May 20 15:09:14 2021
@author: Jonatha Rodrigues da Costa

Rotinas (métodos) auxiliares para a execução de códigos com maior clareza
do processo.
"""
import numpy as np
#=============================================================================
def pol(p,digitos_coef):
    
    '''
    Converte os coeficientes de um polinômio no formato 
    p(x)=ax^n + bx^(n-1) + cx^(n-2) +... + m
    '''
    s=''
    import sympy as sym
    x=sym.Symbol('x')
    for i in range(len(p)):          
        if p[i]==p[-1]:
            px=str(round(p[i],digitos_coef))
        else:
            if p[i]==1.:
                px=str(x**(len(p)-1-i))              
            else:    
                px=str(round(p[i],digitos_coef)*x**(len(p)-1-i))                                 
        if i==0:
            s=s + px    
        elif p[i]>0:
            s=s+' + '+px
        else:
            s=s +' '+ px    
    return sym.Symbol(s)
    
# =============================================================================
def PolIntLagr(x,y,p):
    '''
    Exibe o resultado objetivo da interpolação de lagrange um valor 'p' num 
    pares de vetores X,Y.
    '''    
    k=np.ones(len(x))                          
    for i in range(len(x)):
        for j in range(len(x)):
            if (i!=j):          
                k[i]=k[i]*(p-x[j])/(x[i]-x[j])    
    Yint=sum(y*k)
    return Yint

# =============================================================================
def PolInterNewton(x,y,p):
    '''
    Exibe o resultado objetivo da interpolação de Newton para um valor 'p' 
    num pares de vetores X,Y.
    '''
    import numpy as np
    x=np.array(x)
    y=np.array(y)
    a,s= [y[0]],y                                # s é vetor das divisoes
    for i in range(len(x)-1):
        y=s                                      # Atualiza o vetor y
        s=(y[1:]-y[:-1])/(x[(1+i):]-x[:-(1+i)])  # Reduz o vetor x
        a.append(s[0])    
    xn,Yint=1,a[0]
    for k in range(1,len(x)):
        xn=xn*(p - x[k-1])
        Yint=Yint+a[k]*xn
    
    return Yint
# =============================================================================

def graph_sp(x,y,xint,yint,tipo:str): 
    '''
    Gera os gráficos para as splines: linear, quadrátic ou cúbica
    '''
    import numpy as np
    import matplotlib.pyplot as plt
    x_values = np.linspace(min(x), max(x), 100)
    y_values = [PolInterNewton(x, y, p) for p in x_values]    
    plt.plot(x_values, y_values,'--', label='Polinômio Interpolador')    
    plt.plot(x,y,'or',label='Pontos de medição')
    plt.plot(xint,yint,'-Db',label='y interpolado',markersize=12)
    plt.legend()
    plt.title(f'Interpolação via spline {tipo}')
    plt.style.use('ggplot')
    
