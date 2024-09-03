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


Calcule o comprimento do cabo (C) entre duas torres de transmissão. 
A distância entre as torres é de d= 500m. A flecha máxima permitida é 
fmax = 50m. Flecha é a distância vertical entre uma reta que liga os dois 
pontos de fixação,conforme indicado na ilustração. A flecha depende do 
comprimento do vão (d), da temperatura do cabo e da tração aplicada ao cabo
quando este é instalado. O seu modelo matemático pode ser:

"""
import matplotlib.pyplot as plt
import numpy as np
import time

d,fmax=500,50
def f(C):
    return C * (np.cosh(d / (2 * C)) - 1) - fmax

def calc_bissec(f,a,b,imax,tol,graph=1):  
    print('iteração \t\ta  \t\t\t\tb \t\t\t\tx \t\t\tf(a) \t\tf(x) \t\tf(b) \t\t\tErro')
    print(100*'-')
    t0 = time.process_time()         #   Ligar cronômetro
    if f(a)*f(b)>0:
        print('A raiz não está contida no intervalo dado [%d,%d]!'%(a,b))
        print('Por favor teste um novo intervalo [a,b].')
    else:
        dados=[]        
        for i in range(1,imax):
            x=(a+b)/2
            toli=(b-a)/2            
            fa,fb,fx = f(a),f(b),f(x)
            print('\t%d\t\t%.3f \t\t%.3f  \t\t%.3f \t\t%.3f \t\t%.3f \t\t%.3f \t\t%.6f' 
                  %(i,a,b,x,fa,fb,fx,toli))
            dados.append((i,a,b,x,fa,fb,fx,toli))
            if (f(a)*f(x)<0): b=x        # Raiz localizada entre a e x >> novo b
            else: a=x                    # Raiz localizada entre b e x >> novo a            
            if(toli<tol):           
                print(60*'-'); break        
        print('\nSolução x=',format(x,'.3f'),'encontrada após',i+1,'iterações!')    
        print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))
        if graph==1:
            x=[dados[i][0] for i in range(len(dados))] # Iterações
            y=[dados[i][3] for i in range(len(dados))] # Atualizações de x
            plt.plot(x,y,'o-',label='Valores de x por iteração')
            plt.xlabel('Iterações');plt.ylabel('Valores de x');
            plt.legend()
            plt.grid(True)
            plt.show()     
            
# =============================================================================                       
calc_bissec(f,500,1000,imax=1000,tol=1e-6,graph=1)  
