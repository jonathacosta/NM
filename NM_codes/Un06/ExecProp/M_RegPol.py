#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Regressão Polinomial
Prof. Jonatha Costa

 =============================================================================
# p(x)=a_m*x**m + a_(m-1)x**(m-1)+...+a1x + a0
# =============================================================================
# f = lambda x: x**2+2*x -3           # Função de referência comparativa
# x = np.linspace(0,5,10)             # Pontos do domínio avaliado
# y=f(x) 

"""
import numpy as np
import matplotlib.pyplot as plt
from fun import pol

#%%=============================================================================

def RegPol(x,y,grau):
    '''
    Regressão Polinomial - Soluções via comandos polyval e polyfit
    '''        
    px=np.polyfit(x,y,grau)               # Coef. de p(x) proposto   
    return px

def error_evaluation(x,y,px):
       
    # Cálculo do r2
    y2=np.polyval(px,x)
    y_mean = np.mean(y)
    ss_tot = sum((y - y_mean) ** 2)
    ss_res = sum((y - y2) ** 2)
    r2 = 1 - (ss_res / ss_tot)          
    r = round(np.sqrt(r2),4)*100   
    return r2,r,y2

def results(r2,r,y2,xint,x,y,px,graph=1):   
    
    # Exibição de resultados
    yint=np.polyval(px,xint)
    print(f'O valor {xint} linearmente interpolado resulta em: {round(yint,2)}')          
    print(f"Coeficiente de determinação(r²):{round(r2,4)}",)
    print(f"Coeficiente de correlação (r):{r}%")
    
    if graph==1:
        p=pol(px,digitos_coef=4)               
        plt.title("Regressão Linear")        
        plt.plot(x,y,'*r',label='Medições')
        plt.plot(x,y2,'--b',label=p)
        plt.plot(xint,yint,'oy',label="yint",markersize=12)
        plt.text(0.75, 0.05, f'$R^2 = {round(r2,2)}$', fontsize=12, transform=plt.gca().transAxes)
        plt.legend(fontsize=18)
        plt.legend()
        plt.style.use('ggplot')
        plt.show()

def RegPol_Matr(x,y,grau,graph=1):
    '''
    Regressão Polinomial - Soluções via matrizes Ax=B
    '''        
    A=np.eye(grau+1)                      # Matriz A
    for i in range(grau+1):
        for j in range(grau+1):     
            A[i,j] = sum(x**(i+j))
            
    B=np.zeros(grau+1)                   # Vetor da matriz B
    for i in range(grau+1):
        B[i]=sum((x**i)*y)
       
    px=(list(np.linalg.solve(A,B)))   # Vetor de coeficientes de p(x)
    px.reverse()  
    print(f'O polinômio proposto para os pontos dados é:\np(x)= {pol(px)}')
    
    y2=np.polyval(px,x)
    y_mean = np.mean(y)
    ss_tot = sum((y - y_mean) ** 2)
    ss_res = sum((y - y2) ** 2)
    r2 = 1 - (ss_res / ss_tot)      
    r = round(np.sqrt(r2),4)*100

    # print(np.polyval(p,ponto_reg))
    print(f"\nCoeficiente de determinação:{round(r2,4)}",)
    print(f"Coeficiente de correlação:{r}%")
    
    
    if graph==1:
        v=np.polyval(px,x)                 # Imagem do novo domínio
        plt.figure()
        plt.plot(x,y,'r*',label='Pontos de medição - Referência')
        plt.plot(x,v,'bo',label=f'Polinomino proposto com grau {grau}')
        plt.title('Gráfico básico com polyfit e polyval')
        plt.style.use('ggplot');plt.grid(visible='on');
        plt.legend();plt.show()
        
#%%TESTE=============================================================================

if __name__ ==  "__main__":
    x=np.array(list(range(0,110,10)))
    y=np.array([ 0.94, 0.96, 1.0, 1.05, 1.07, 1.09, 1.14, 1.17, 1.21, 1.24, 1.28])
    m=1                              # Grau do polinômio    
    xint=60
    # Evocando atributos e métods
    px = RegPol(x,y,m)
    r2,r,y2 = error_evaluation(x,y,px)
    results(r2,r,y2,xint,x,y,px,graph=1)

#%% 



