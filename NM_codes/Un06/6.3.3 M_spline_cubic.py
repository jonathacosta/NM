#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Interpolação via spline cubica'
Prof. Jonatha Costa


1)Conceito:
   
    Uma spline cúbica é uma função polinomial de grau três que é usada para 
    interpolar um conjunto de pontos. Em outras palavras, dado um conjunto de 
    pontos (xi,yi), em que i=0,1,2,…,n, uma spline cúbica cria uma curva suave 
    que passa por todos esses pontos. A ideia é garantir que a curva seja 
    contínua e que tenha uma derivada contínua até a segunda ordem em todos os 
    pontos de interpolação.


    Uma spline cúbica é composta por um conjunto de funções polinomiais cúbicas 
    definidas em cada intervalo [xi,xi+1].
    Para um intervalo específico, a spline cúbica Si(x) é dada por:

            Si(x)=ai+bi(x−xi)+ci(x−xi)2+di(x−xi)3
    em que ai​, bi​, ci​, e di​ são coeficientes a serem determinados. 
    Cada spline cúbica é ajustada para garantir a continuidade da função e das 
    suas primeiras e segundas derivadas nos pontos de interpolação.   
    
2)Condições de Contorno

    Para resolver o sistema de equações que determina os coeficientes ai​, bi​,
    ci​, e di, precisamos especificar algumas condições de contorno. 
    As opções comuns são:

    - Condições de extremos (ou de "borda"): 
        Definem as derivadas nas extremidades do intervalo. Por exemplo, você 
        pode definir a derivada como zero (conhecida como condição de 
       "extremidade natural") ou usar outros valores específicos.

    - Condições de continuidade: 
        Asseguram que a função e suas derivadas de primeira e segunda ordem 
        sejam contínuas nos pontos de interpolação.    
    
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def spline_cubic(x, y, xint):
    x=np.array(x); y=np.array(y);
    n = len(x)
    h = np.diff(x)
    
    # Sistema de equações para os coeficientes
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    # Condições de contorno naturais (segunda derivada igual a zero nas extremidades)
    A[0, 0] = 1
    A[-1, -1] = 1
    
    # Preenchendo o sistema
    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        b[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])
    
    # Resolvendo o sistema para os coeficientes da segunda derivada
    m = np.linalg.solve(A, b)
    
    # Coeficientes dos splines cúbicos
    a = y[:-1]
    b = (y[1:] - y[:-1]) / h - h * (m[1:] + 2 * m[:-1]) / 3
    c = m[:-1]
    d = (m[1:] - m[:-1]) / (3 * h)

    # Aplicando resultado no spline 
    i = np.searchsorted(x, xint) - 1
    i = np.clip(i, 0, len(a) - 1)
    
    dx = xint - x[i]

    yint = a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
    
    return yint

#%%
if __name__ == "__main__":    
    x=[8,11,15,18]; y=[5,9,10,8]
    xint=12.7    
    yint = spline_cubic(x, y,xint)    
    print(f"O valor interpolado em p = {xint} é: {yint}")
    from A_fun import graph_sp
    graph_sp(x,y,xint,yint,'cúbica')

