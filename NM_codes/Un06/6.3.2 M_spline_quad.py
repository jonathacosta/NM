#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Interpolação via spline quadrátiva'
Prof. Jonatha Costa


1)Conceito:
    A spline quadrática é uma técnica de interpolação semelhante à spline linear,
    mas em vez de usar segmentos de reta para conectar os pontos, ela usa funções 
    quadráticas. Isso significa que entre cada par de pontos (xi,yi) e 
    (xi+1,yi+1), o valor interpolado será descrito por uma parábola, o que 
    proporciona uma interpolação mais suave do que a spline linear.

2)Definição:
    Dado um conjunto de pontos (x0,y0),(x1,y1),…,(xn,yn), a spline quadrática 
    utiliza uma função quadrática Si(x) para cada intervalo [xi,xi+1] definida
    como:
                    Si(x)=ai(x−xi)2+bi(x−xi)+ci
    
    Aqui, ai​, bi e ci​ são coeficientes que precisam ser determinados para 
    garantir que as condições de continuidade sejam satisfeitas.

3)Condições para spline quadrática:

Para garantir que a interpolação seja suave, as splines quadráticas precisam 
satisfazer as seguintes condições:

    -Interpolação nos nós: A spline deve passar exatamente pelos pontos dados,
    ou seja:Si(xi)=yi e Si(xi+1)=yi+1
    
    -Continuidade: As funções quadráticas devem ser contínuas, de modo que 
    Si(xi+1)=Si+1(xi+1) para todos os i.
    
    -Continuidade da primeira derivada: A derivada da spline também deve ser 
    contínua, ou seja  Si′​(xi+1​)=Si+1′​(xi+1​)

Essas condições geram um sistema de equações que permite resolver os coeficientes
ai​, bi​ e ci​ para cada intervalo.

"""
import numpy as np

# =============================================================================
def spline_quad(x,y,xint):
    '''
    Encontrar o intervalo que contém o valor de xint.
    '''
    n = len(x)
    for i in range(1,len(x)):
        if xint<x[i+1]:
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
    return yint

# =============================================================================
if __name__ == "__main__":    
    x=[8,11,15,18]; y=[5,9,10,8]
    xint=12.7    
    yint=spline_quad(x,y,xint)
    print('\nA aproximação encontrada para f(%.1f) = %.2f'%(xint,yint))
    from A_fun import graph_sp
    graph_sp(x,y,xint,yint,'quadrática')
        
#%%
