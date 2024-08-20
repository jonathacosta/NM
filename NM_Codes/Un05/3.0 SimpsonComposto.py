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

#%%                   1/3 de Simpson Composto 
"""
# =============================================================================
                  1/3 de Simpson Composto 
# =============================================================================
Considerações iniciais:
       
     No método de Simpson 1/3 composto divide-se o intervalo [a, b] em 
     N subintervalos de largura h, em que  h = (b − a)/N   
     
     O método de Simpson 1/3 é aplicado em dois subintervalos adjacentes de 
     cada vez, por serem necessários 3 pontos para definir um polinômio 
     quadrático. Portanto, o intervalo total deve ser dividido em um número 
     par de subintervalos.
     A integral ao longo de 2 intervalos adjacentes [xi−1,xi] e [xi,xi+1] fica
     definida de modo que:
         - os subintervalos devem ser igualmente espaçados
         -O número de subintervalos no domínio [a, b] deve ser um número par
     A equação final é uma soma ponderada da função nos pontos que definem 
     os subintervalos tal que o peso é 4 nos pontos xi pares e 2 xi nos 
     ímpares (exceto o primeiro e o último ponto).    
     Estes são os pontos centrais de cada par de subintervalos adjacentes.
     Cada ponto é usado uma vez como o ponto final à direita de um par de 
     subintervalos, e uma vez como o ponto final à esquerda do par de 
     subintervalos seguinte.
     
    I(f)= h/3 [f(a)+4\sum_{i=2,4,6}^{N}f(x_i)+2\sum_{j=3,5,7}^{N-1}f(x_j)+f(b)
           
"""
s=0
N=100
if (N%2)!=0:                            # Validar número par de intervalos
    N=N+1
h=(b-a)/N
x=np.arange(a,(b+h),h)                  # Atualizar x em funçaõ de h intervalos
for i in range(1,N):
    if i%2==0:
        s+=4*f(x[i])
    else:
        s+=2*f(x[i])
s=(f(a)+s+f(b))*h/3 

# Comparativo com solução analítica       
g,e=integrate.quad(f,a,b)
print(f'\nSolução analítica : {round(g,4)}.')  
print(f"Solução numérica por 3/8 de Simpson Composto com {N} subintervalos: {s}")
print(f'Erro entre soluções {round(g,4)-s}')
print()

#%%                  3/8 simpson Composto
"""
# =============================================================================
                  3/8 de Simpson Composto 
# =============================================================================
Considerações iniciais:
       Um polinômio cúbico (de terceira ordem) é usado para aproximar o 
       integrando 
       - Os coeficientes do polinômio quadrático são determinados a partir dos 
       pontos: x1 = a,x4 = b e dois pontos x2 e x3 que dividem o intervalo em 
       três seções iguais, tal que: 
           p(x) = c3x3 + c2x2 + c1x + c0, onde c3, c2, c1 e c0 são constantes
           avaliadas a partir da condição que diz que passa pelos pontos
           p(x1) = f(x1),p(x2) = f(x2), p(x3) = f(x3) e p(x4) = f(x4).
     
        Os subintervalos devem ser igualmente espaçados.
        O número de subintervalos no domínio [a, b] deve ser um número 
        divisível por 3.
        
        Uma combinação dos métodos de Simpson pode ser usada para realizar a 
        integração quando houver um número ímpar qualquer de subintervalos.
        Isso é feito usando o método de Simpson 3/8 nos três primeiros 
        ([a, x2 ], [x2 , x3 ]e[x3 , x4 ]) ou nos três últimos subintervalos
        ([xN −2 , xN −1 ], [xN −1 , xN ]  e [xN , xb ]), aplicando-se o método 
        de Simpson 1/3 no número restante (par) de subintervalos

        Resultando em 
        I(f) = 3/8[f(a) + 3\sum_{i=2,5,8}^{N-1}[f(x_i) 
              +f(x_{i+1}])+ 2\sum_{j=4,7,10}^{N-2}f(x_j)+f(b)],
        em que $h = (b - a)/N$
                                                
            """


while (N%3)!=0:                         # Validar número par de intervalos
    N=N+1
h=(b-a)/N
x=np.arange(a,(b+h),h)                  # Atualizar x em funçaõ de h intervalos
p1,p2=0,0
for i in (np.arange(1,N,3)):
    p1+=3*( f(x[i])+f(x[i+1]) )
for i in (np.arange(4,N,3)):
    p2+=2*f(x[i])
s1=(f(a) + p1 + p2 + f(b))*h*3/8   
   
# Comparativo com solução analítica       
g,e=integrate.quad(f,a,b)
print(f'\nSolução analítica : {round(g,4)}.')  
print(f"Solução numérica por 3/8 de Simpson Composto com {N} subintervalos: {s1}")
print(f'Erro entre soluções {round(g,4)-s1}')
print()

#%% Comparativo entre resultados
print('-'*50)
print("Comparativo entre resultados")
print('-'*50)
print(f'\nSolução analítica : {round(g,4)}.')  
print(f"Solução numérica por 1/3 de Simpson Composto: {round(s,4)}. Erro:{round(g,4)-s1}")
print(f"Solução numérica por 3/8 de Simpson Composto: {round(s1,4)}. Erro: {round(g,4)-s1}")



