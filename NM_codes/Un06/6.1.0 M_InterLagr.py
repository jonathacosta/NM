#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Interpolação de Lagrange
Prof. Jonatha Costa

Conceito basilares:
    A interpolação de Lagrange é um método clássico de interpolação polinomial, 
    utilizado para encontrar um polinômio que passa por um conjunto de pontos 
    dados. É muito útil quando queremos aproximar uma função desconhecida, mas
    temos alguns pontos amostrais dela.

    A ideia principal da interpolação de Lagrange é encontrar um polinômio 
    P(x) de grau n−1 que passe por nn pontos distintos (x0,y0),(x1,y1),…,
    (xn−1,yn−1).
    
    O polinômio interpolador é construído como uma combinação linear de funções
    base de Lagrange.

Fórmula do Polinômio Interpolador:

    O polinômio de Lagrange é dado por:
                P(x)=\sum _{i=0 ^n−1} ( yi ⋅ Li(x) )

    em que Li​(x) são os polinômios de Lagrange definidos como:
        Li(x)= \prod_{0 ≤ j ≤ n−1, com j≠i} (x−xj) / (xi−xj)
    
    Aqui, Li(x) é um polinômio de grau n−1 que vale 1 no ponto xi e 0 em todos 
    os outros pontos xj (j≠i).

Vantagens e Desvantagens:
    - Vantagens: Simples de implementar e fornece um polinômio único que passa 
    por todos os pontos dados.
    - Desvantagens: Pode ser computacionalmente caro para um grande número de 
    pontos,e a precisão pode se deteriorar se os pontos estiverem muito próximos 
    ou distantes uns dos outros (problema de Runge).

Conceito de grau:
    O grau do polinômio interpolador de Lagrange é n−1, onde n é o número 
    de pontos distintos (x0,y0),(x1,y1),…,(xn−1,yn−1) utilizados para a 
    interpolação.
    
    Dessa forma, perceba que:
    a) Se você tiver 2 pontos (x0,y0) e (x1,y1), o polinômio 
    interpolador de Lagrange será de grau 1 (ou seja, uma reta).
    b) Se tiver 3 pontos (x0​,y0​),(x1​,y1​) e (x2​,y2​), o polinômio será de grau 
    2(uma parábola).
       
"""
import numpy as np
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

def GerPolIntLagr(x,y):
    '''
    Exibe o polinômio Interpolador de Lagrage a partir na dimensão do vetor
    de entrada x espaçado num espaço linear de 100 unidades.
    Note que o grau do polinômio interpolador de Lagrange é n−1, onde n é o 
    número  de pontos distintos (x0,y0),(x1,y1),…,(xn−1,yn−1) utilizados para 
    a  interpolação.
    '''
    import sympy as sp
    p = sp.symbols('x')
    n = len(x)        
    P = 0   # Inicializa o polinômio P(x) como 0
    # Construir o polinômio interpolador de Lagrange
    for i in range(n):
        # Calcula o termo L_i(x)
        L_i = 1
        for j in range(n):
            if j != i:
                L_i *= (p - x[j]) / (x[i] - x[j])        
        # Adiciona o termo ao polinômio P(x)
        P += y[i] * L_i    
    # Simplifica o polinômio
    P = sp.simplify(P)
    print(f"Polinômio interpolador: {P}")

def GraphPolIntLagr(x,y):
    '''
    Percepção gráfica para um espaço linear a partir do vetor de entrada x.
    Note que o grau do polinomio muda em função dos pontos do espaço linear
    
    O resultado gráfico é gerado a partir de um novo vetor x linearmente espa-
    çado em 100 partes. O grau o polinômio passa a ser função da quantidade de pontos do 
    vetor de entrada x.
    '''
    import matplotlib.pyplot as plt
    # Plotando os pontos e o polinômio interpolador
    x_values = np.linspace(min(x), max(x), 100)
    y_values = [PolIntLagr(x, y, i) for i in x_values]    
    plt.plot(x_values, y_values, label='Polinômio Interpolador')
    plt.scatter(x, y, color='red', label='Pontos Dados')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.legend()
    plt.title('Interpolação de Lagrange')
    plt.grid(True)
    plt.show()
        
#%% =============================================================================
# Valores de entrada
if __name__=="__main__":    
    # Ponto de interpolação e vetores de entrada x,y
    p=3; 
    x=np.array([1,2,4,5,7,8]); y=np.array([52,5,-5,-40,10,5])    
    # Resultado da interpolação do ponto 'p'
    Yint= PolIntLagr(x,y,p)
    print('\nA aproximação encontrada para f(%.2f) = %.2f'%(p,Yint))   
    # Percepção gráfica 
    GerPolIntLagr(x,y)
    # Percepção do grau do polinômio
    GraphPolIntLagr(x, y)   