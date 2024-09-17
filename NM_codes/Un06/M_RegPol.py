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
from A_fun import pol
import A_error_analyzer as ea
import matplotlib.pyplot as plt


#%%=============================================================================

def RegPol(x,y,grau):
    '''
    Regressão Polinomial - Soluções via comandos polyval e polyfit
    '''        
    px=np.polyfit(x,y,grau)               # Coef. de p(x) proposto   
    return px

def results(r2,y2,xint,x,y,px,graph=1):   
    
    # Exibição de resultados
    yint=np.polyval(px,xint)
    print(f'O valor {xint} linearmente interpolado resulta em: {round(yint,2)}')          
    print(f"Coeficiente de determinação(r²):{round(r2,4)}",)
    
    if graph==1:
        p=pol(px,digitos_coef=6)               
        plt.title("Regressão Polinomial")        
        plt.plot(x,y,'*r',label='Medições')
        plt.plot(x,y2,'--b',label=p)
        plt.plot(xint,yint,'oy',label="yint",markersize=12)
        plt.text(0.75, 0.05, f'$R^2 = {round(r2,4)}$', fontsize=12, 
                 transform=plt.gca().transAxes)
        plt.legend(fontsize=18)
        plt.legend()
        plt.style.use('ggplot')
        plt.show()
        
# =============================================================================
# Teste    
# =============================================================================
if __name__=="__main__":
    #Dados
    x=np.array(list(range(0,110,10)))
    y=np.array([ 0.94, 0.96, 1.0, 1.05, 1.07, 1.09, 1.14, 1.17, 1.21, 1.24, 1.28])
    m=3    
    xint=30
    
    # Chamadas de métodos
    px = RegPol(x,y,m)
    y_pred = np.polyval(px, x)
    r2 = ea.r2(y, y_pred)        
        
    # Chamada de resultados e gráficos
    results(r2,y_pred,xint,x,y,px,graph=1)


#%% Uso de dados externos
''' 
   Para utilizar o código com dados externos pode-se :
       * Organizar uma planilha eletrônica com os dados em colunas;
       * Salvar o arquivo em formato '.csv' no mesmo endereço do arquivo '.py';
       * Executar o script abaixo para converter as colunas em vetores de dados
       de interesse para análise. Utilize a coluna '0' para x e 
       a coluna '1' em y, por exemplo:
           
        import pandas as pd
        df = pd.read_csv('Ensaio.csv')
        x=df[df.columns[0]].values
        y=df[df.columns[1]].values
        
'''
