#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Integração via Métodos de 1/3 de Simpson simples e composto
Prof. Jonatha Costa
"""

import numpy as np
import scipy.integrate as integrate

f=lambda x: 97000*x/(5*x**2 + 570000)     # Função 
a,b = 40,93                               # Intervalo

#%%                   1/3 de Simpson simples 
"""
=============================================================================
                    1/3 de Simpson simples 
=============================================================================
Considerações iniciais:
    
    Um polinômio quadrático (de segunda ordem) é usado para aproximar o integrando
    - Os coeficientes do polinômio quadrático são determinados a partir de 
    três pontos: x1 = a, x2 = (a + b)/2 e x3 = b;
    - Portanto, p(x) = α + β(x−x1)+ γ(x−x1)(x−x2), em que α,β e γ são 
    constantes desconhecidas tais que o polinômio deve passar por todos 
    os pontos, p(x1) = f (x1), p(x2) = f (x2) e p(x3) = f (x3).
    -
    Isso resulta em:
        α = f(x1),
        β = [f(x2) − f(x1)]/(x2−x1) e 
        γ = [f(x3) − 2f (x2) + f (x1)]/(2(h)^2), em que h = (b − a)/2
    Portanto:
        I = [f(a) + 4f((a+b)/2) + f(b)]
"""



h=(b-a)/2                                 # Largura de cada intervalo
x=np.arange(a,(b+h),h)                    # Intervalo x1,x2,x3
s=h/3*(f(a)+4*f((a+b)/2)+f(b))   

# Comparativo com solução analítica       
g,e=integrate.quad(f,a,b)
print(f'\nSolução analítica : {round(g,4)}.')  
print(f"Solução numérica por 1/3 de Simpson simples: {s}")
print(f'Erro entre soluções {round(g,4)-s}')

#%%                  3/8 simpson simples
"""
# =============================================================================
                  3/8 de Simpson simples 
# =============================================================================
Considerações iniciais:
    
    Um polinômio cúbico (de terceira ordem) é usado para aproximar o integrando
    - Os coeficientes do polinômio quadrático são determinados a partir dos 
    pontos:
      x1 = a,x4 = b e dois pontos x2 e x3 que dividem o intervalo em três 
      seções iguais
    - Desse modo, p(x) = c3x3 + c2x2 + c1x + c0 , em que c3,c2,c1 e c0 
    são constantes avaliadas a partir da condição que diz que passa pelos 
    pontos p(x1) = f(x1),p(x2) = f(x2), p(x3) = f(x3) e p(x4) = f(x4).
    - Isso resulta em:
        I = 3/8 h[f(a)+ 3f(x2) + 3f(x3)+f (b)]
"""

h=(b-a)/3                                 # Largura de cada intervalo
x=np.arange(a,(b+h),h)                    # Intervalo x1,x2,x3,x4
s1=(3*h/8)*(f(a)+3*f(a+h)+3*f(a+2*h)+f(b))            

# Comparativo com solução analítica       
g,e=integrate.quad(f,a,b)
print(f'\nSolução analítica : {round(g,4)}.')  
print(f"Solução numérica por 3/8 de Simpson simples: {s1}")
print(f'Erro entre soluções {round(g,4)-s1}')
print()

#%% Comparativo entre resultados
print('-'*50)
print("Comparativo entre resultados")
print('-'*50)
print(f'\nSolução analítica : {round(g,4)}.')  
print(f"Solução numérica por 1/3 de Simpson simples: {round(s,4)}. Erro:{round(g,4)-s1}")
print(f"Solução numérica por 3/8 de Simpson simples: {round(s1,4)}. Erro: {round(g,4)-s1}")




