#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações não lineares
Método da Falsa Posição
Prof. Jonatha Costa
"""

import matplotlib.pyplot as plt
import numpy as np
import time

def Calc_FalsaPosicao(f,a,b,imax,tol,graph=1):  
    print('iteração \t\ta  \t\t\t\tb \t\t\t\tx \t\t\tf(a) \t\tf(x) \t\tf(b) \t\t\tErro')
    print(100*'-')
    t0 = time.process_time()         #   Ligar cronômetro
    if f(a)*f(b)>0:
        print('A raiz não está contida no intervalo dado [%d,%d]!'%(a,b))
        print('Por favor teste um novo intervalo [a,b].')
    else:
        dados=[]        
        for i in range(1,imax):                        
            fa,fb = f(a),f(b)
            x=(a*fb - b*fa) / ( fb-fa )
            fx=f(x)
            toli=(b-a)/2            
            print('\t%d\t\t%.3f \t\t%.3f  \t\t%.3f \t\t%.3f \t\t%.3f \t\t%.3f \t\t%.6f' 
                  %(i,a,b,x,fa,fb,fx,toli))
            dados.append((i,a,b,x,fa,fb,fx,toli))
            if (fa*fx>0): a=x        # Raiz localizada entre a e x >> novo b
            else: b=x                    # Raiz localizada entre b e x >> novo a            
            if(toli<tol):           
                print(60*'-'); break                            
        print('\nSolução x=',format(x,'.3f'),'encontrada após',i,'iterações!')    
        print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))
        if graph==1:
            x=[dados[i][0] for i in range(len(dados))] # Iterações
            y=[dados[i][3] for i in range(len(dados))] # Atualizações de x
            plt.plot(x,y,'o-',label='Valores de x por iteração')
            plt.xlabel('Iterações');plt.ylabel('Valores de x');
            plt.title('Falsa Posição (Regula Falsi)')
            plt.legend()
            plt.grid(True)
            plt.show()     
            
#%% =============================================================================                       
f= lambda x: 8-4.5*(x - np.sin(x))    # ou def fun(x): ...
a, b = 2, 3

Calc_FalsaPosicao(f,a,b,imax=500,tol=1e-6,graph=1)  
