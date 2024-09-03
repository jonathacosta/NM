#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações não lineares
Método da Secante'
Prof. Jonatha Costa
"""

import matplotlib.pyplot as plt
import numpy as np
import time

def Calc_FalsaPosicao(f,a,b,imax,Err,graph=1):  
    print('iteração \t\ta  \t\t\t\tb \t\t\t\tx \t\t\tf(a) \t\tf(x) \t\tf(b) \t\t\tErro')
    print(100*'-')
    t0 = time.process_time()         #   Ligar cronômetro
    if f(a)*f(b)>0:
        print('A raiz não está contida no intervalo dado [%d,%d]!'%(a,b))
        print('Por favor teste um novo intervalo [a,b].')
    else:
        dados=[]          
        for i in range(1,imax):  
            Xsn=b-f(b)*(a-b)/( f(a)-f(b) )     # Xsn=x(i+1);Xest=x(i)  
            # X.append(Xsn)
            if(abs( (Xsn-b) / b)<Err):
                break
            if abs(f(Xsn))<Err:
                break
            if i==imax:
                print(f'A solução não foi encontrada após {i} iterações')
                break
            a,b=b,Xsn 
            dados.append((i,a,b,Xsn))                       
        print('\nSolução x=',format(Xsn,'.3f'),'encontrada após',i,'iterações!')    
        print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))
        if graph==1:
            x=[dados[i][0] for i in range(len(dados))] # Iterações
            y=[dados[i][3] for i in range(len(dados))] # Atualizações de x
            plt.plot(x,y,'ob-',label='Valores de x por iteração')
            plt.xlabel('Iterações');plt.ylabel('Valores de x');
            plt.title('Secante')
            plt.legend()
            plt.grid(True)
            plt.show()     
            
#%% =============================================================================                       
f= lambda x: 8-4.5*(x - np.sin(x))    # ou def fun(x): ...
a, b = 2, 3

Calc_FalsaPosicao(f,a,b,imax=500,Err=1e-6,graph=1)  

