#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações não lineares
Método da Falsa Posição'
Prof. Jonatha Costa
"""
import numpy as np
import matplotlib.pyplot as plt
import time
print('\014')
# =============================================================================
# Função 
# =============================================================================

print('\014')
f= lambda x: 8-4.5*(x - np.sin(x))    
a,b=2,3
imax=50
tol=0.001
print('Métodos numéricos - Solução de equações não lineares.')
print('Método da Falsa Posição!')
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
        x=( a*f(b) - b*f(a) ) / ( f(b)-f(a) )
        X.append(x)
        toli=(b-a)/2
        print('    %d   %.3f    %.3f   %.4f   %.3f   %.3f    %.3f' 
              %(i+1,a,b,x,f(a),f(x),f(b)))                           
        if f(a)*f(x)>0:   # Raiz localizada entre [a,x] >> [a,b=x]
            a=x             
        else:               # Raiz localizada entre [x,b] >> [a=x,b]
            b=x
        if(toli<tol):
            print(60*'-')
            break
    print()
    print('Solução x=',format(x,'.4f'),'encontrada após',i+1,'iterações!')    
    print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))
                    # Solução gráfica     
    plt.plot(X,np.array(f(X)),'ro--',label='f(x)=8-4.5*x - np.sin(x)')
    plt.plot(X[-1],f(X[-1]),'bo',label='Solução')
    plt.legend()
    plt.title('Convergência para zeros da função.')
    plt.style.use('ggplot')

'''
Atenção nos referenciais ao escolher os intervalos para teste.
Note que dizer que:
> f(a)*f(x) > 0 é o mesmo que f(b)*f(x)< 0 então fixar b e atualizar a=x
 Isto implica que, como b é maior que a, b=b e a=x em ambos testes
> f(a)*f(x) < 0 => f(b)*f(x)> 0 ; então fixar a e atualizar b=x 

'''
