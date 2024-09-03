#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações não lineares
Prof. Jonatha Costa

Método da bisseção
    - Se f(x) for real e contínua no intervalo [𝑥1,𝑥2]
    𝑓(𝑥1) e 𝑓(𝑥2) tiverem sinais opostos, portanto 𝑓(𝑥1).𝑓(𝑥2) < 0,
    então existe pelo menos uma raiz real entre x1 e x2.
    - A nova solução x é obtida pela média entre x1 e x2. A determinação 
    do novo intervalo é feita pela checagem de 𝑓(𝑥1).𝑓(𝑥2) < 0 para x, x1 e x2.
    - O critério de parada pode ser definido como a diferença de f(x) entre 
    duas iterações subsequentes ou pela sua proximidade com o zero.        


Um retificador de meia onda a diodo alimenta uma carga indutiva-resistiva 
(f = 1 kHz, L = 100 mH e R = 1 kΩ). Encontre o ângulo β para o qual a corrente 
no diodo se anula. Considere o seguinte modelo matemático:
𝐼𝑑 = sin(𝛽 − 𝛷) + sin(𝛷)𝑒^(-𝛽/tan(𝛷)))
tan(ϕ) = 2πf.L/R

"""
import matplotlib.pyplot as plt
import numpy as np
import time

#******************************************
# Dados fornecidos e cálculo basilar
f = 1000  # frequência em Hz
L = 0.1   # indutância em Henry
R = 1000  # resistência em Ohms
tan_phi = (2 * np.pi * f * L) / R           # Cálculo de tan(Φ)
phi = np.arctan(tan_phi)                    # Cálculo do ângulo Φ

def f(beta):
    # 0 = sin(𝛽 − 𝛷) + sin(𝛷)𝑒^(-𝛽/tan(𝛷)))
    return np.sin(beta - phi) + np.sin(phi) * np.exp(-beta / tan_phi)

def calc_bissec(f,a,b,imax=1000,tol=1e-6,graph=0):   
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
            print('\t%d\t\t%.3f \t\t%.3f  \t\t%.3f \t\t%.3f \t\t%.3f \t\t%.3f \t\t%.6f' 
                  %(i,np.degrees(a),np.degrees(b),np.degrees(x),f(a),f(b),f(x),toli))
            dados.append((i,np.degrees(a),np.degrees(b),np.degrees(x),f(a),f(b),f(x),toli))
            if (f(a)*f(x)<0): b=x        # Raiz localizada entre a e x >> novo b
            else: a=x                    # Raiz localizada entre b e x >> novo a            
            if(toli<tol): print(60*'-'); break        
        print('\nSolução beta=',format(np.degrees(x),'.3f'),'encontrada após',i+1,'iterações!')    
        print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))
        print(f"tan(Φ) ≈ {tan_phi:.3f}")
        print(f"Φ ≈ {np.degrees(phi):.2f}°")
        print(f"β ≈ {np.degrees(x):.2f}°") 
        
        if graph==1:
           x=[dados[i][0] for i in range(len(dados))] # Iterações
           y=[dados[i][3] for i in range(len(dados))] # Atualizações de x
           plt.plot(x,y,'o-',label='Valores de beta por iteração')
           plt.xlabel('Iterações');plt.ylabel('Valores de beta');
           plt.legend()
           plt.grid(True)
           plt.show()     
            
# =============================================================================
#%%

calc_bissec(f,phi,2*np.pi,imax=1000,tol=1e-6,graph=1)

