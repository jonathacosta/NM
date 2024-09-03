#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Interpolação via spline quadrátiva'
Prof. Jonatha Costa
"""
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
def spline_quad(x,y,xint):
    n = len(x)
    for i in range(len(x)):
        if (xint < x[0] and xint >x[-1]):
            print('Erro!\nInterpolação fora do intervalo.')
        elif xint<x[i+1]:
            i+=1
            break
    # =============================================================================    
    intervalo=i+2*(i-1)     # Posiciona os 3 coeficientes no intervalo
    #**************************************%***************************************
    eq0 = 2*(n-1)          # Quant. spline por intervalo 
    eq1 =  n-2             # Quant. de nós
    eq = eq0+eq1           # Total de equações         
    #**************************************%***************************************
    A=np.arange(eq*(eq+1)).reshape(eq,eq+1)   # Coluna adicional
    d,k,A[:]=0,0,0
    for b in range(int(eq0/2)):           # bloco   
        for i in range(2):                # linha
            for j in range(3):            # coluna
                A[i+k,j+d]=x[i+b]**abs(j-2)
        d+=3
        k+=2      
    m, d = 1, 0
    for k in range(eq0,eq):              # linha/bloco
        for j in range(2):               # coluna
            A[k,j+d]=(2*x[m])**abs(j-1)
            A[k,j+d+3]=-A[k,j+d]
        m+=1
        d+=3
    A=A[: , 1:]                          # Excluindo a coluna extra
    #%**************************************%***************************************
    #Matriz B
    B=[]
    for i in range(n):
        for j in range(2):
            B.append(y[i])
    del(B[0]); del(B[-1])
    
    for j in range(eq1):
        B.append(0)
    B = np.array(B)
    ##**************************************%***************************************

    coef=list(np.linalg.inv(A)@B.T) #coef=list(np.linalg.solve(A,B))
    coef.insert(0,0)
    ##**************************************%***************************************
    j=intervalo-1
    yint=coef[j]*xint**2 + coef[j+1]*xint + coef[j+2]
    yint
    print("\nMetodo Interpolaçao Quadratica resulta em\nf(%.2f) = %.2f \n\n"%(xint,yint))
    
    plt.plot(x,y,'b',label='Pontos de medição')
    plt.plot(xint,yint,'r*',label='y interpolado')
    plt.legend()
    plt.title('Interpolação via spline Quadrática')
    plt.style.use('ggplot')
# =============================================================================
x=[8,11,15,18,22]; y=[5,9,10,8,7]
xint=12.7

spline_quad(x,y,xint)
 

