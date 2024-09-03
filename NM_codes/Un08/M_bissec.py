#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações não lineares
Prof. Jonatha Costa

Método da bisseção
    - Se f(x) for real e contínua no intervalo [𝑥1,𝑥2]
    𝑓(𝑥1 ) e 𝑓(𝑥2 ) tiverem sinais opostos, portanto 𝑓(𝑥1 ).𝑓(𝑥2 ) < 0,
    então existe pelo menos uma raiz real entre x1 e x2.
    - A nova solução x é obtida pela média entre x1 e x2. A determinação 
    do novo intervalo é feita pela checagem de 𝑓(𝑥1 ).𝑓(𝑥2 ) < 0 para x, x1 e x2.
    - O critério de parada pode ser definido como a diferença de f(x) entre 
    duas iterações subsequentes ou pela sua proximidade com o zero.
        
"""
import numpy as np
import matplotlib.pyplot as plt
import time
print('\014')
# =============================================================================
# Função 
# =============================================================================

print('\014')
f= lambda x: 8-4.5*(x - np.sin(x))    # ou def fun(x): ...
a,b=2,3
imax=50
tol=0.001
print('Métodos numéricos - Solução de equações não lineares.')
print('Método da bisseção!')
print('Intervalo de análise [%d,%d].\n'%(a,b) )
print('iteração  a       b        x     f(a)    f(x)       f(b)')
print(60*'-')
t0 = time.process_time()         #   Ligar cronômetro
# =============================================================================
if f(a)*f(b)>0:
    print('A raiz não está contida no intervalo dado [%d,%d]!'%(a,b))
    print('Por favor teste um novo intervalo [a,b].')
else:
    X=[]
    for i in range(imax):
        x=(a+b)/2
        X.append(x)
        toli=(b-a)/2
        print('    %d   %.3f    %.3f   %.3f   %.3f   %.3f    %.3f' 
              %(i+1,a,b,x,f(a),f(x),f(b)))
        if (f(a)*f(x)<0):   # Raiz localizada entre a e x >> novo b
            b=x             
        else:               # Raiz localizada entre b e x >> novo a
            a=x 
        if(toli<tol):
            print(60*'-')
            break
    print()
    print('Solução x=',format(x,'.3f'),'encontrada após',i+1,'iterações!')    
    print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))
                    # Solução gráfica     
    plt.plot(X,np.array(f(X)),'ro-',label='f(x)=8-4.5*x - np.sin(x)')
    plt.plot(X[-1],f(X[-1]),'bo',label='Solução')
    plt.legend()
    plt.title('Convergência para zeros da função.')
    plt.style.use('ggplot')

#%%
f= lambda x: 8-4.5*(x - np.sin(x))    # ou def fun(x): ...
a, b, imax, tol = 2, 3, 50, 0.001
print('iteração  a       b        x     f(a)    f(x)       f(b)')
print(60*'-')
t0 = time.process_time()         #   Ligar cronômetro
# =============================================================================
if f(a)*f(b)>0:
    print('A raiz não está contida no intervalo dado [%d,%d]!'%(a,b))
    print('Por favor teste um novo intervalo [a,b].')
else:
    X=[]
    for i in range(imax):
        x=(a+b)/2
        X.append(x)
        toli=(b-a)/2
        print('    %d   %.3f    %.3f   %.3f   %.3f   %.3f    %.3f' 
              %(i+1,a,b,x,f(a),f(x),f(b)))
        if (f(a)*f(x)<0):   # Raiz localizada entre a e x >> novo b
            b=x             
        else:               # Raiz localizada entre b e x >> novo a
            a=x 
        if(toli<tol):
            print(60*'-')
            break
    print()
    print('Solução x=',format(x,'.3f'),'encontrada após',i+1,'iterações!')    
    print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))
    #                 # Solução gráfica     
    plt.plot(X,np.array(f(X)),'ro-',label='f(x)=8-4.5*x - np.sin(x)')
    plt.plot(X[-1],f(X[-1]),'bo',label='Solução')
    plt.legend()
    plt.title('Convergência para zeros da função.')
    plt.style.use('ggplot')



