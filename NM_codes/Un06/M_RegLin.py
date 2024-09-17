#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Regressão linear'
Prof. Jonatha Costa
#"""
import numpy as np
from A_fun import pol
import A_error_analyzer as ea
import matplotlib.pyplot as plt

# =============================================================================
def reglin(x,y,xint):
    '''
    Solução utilizando estrutura :  Sx ,Sy, Sxy, Sxx
    
    Equivalentes ao comando polyfit : px=np.polyfit(x,y,1)  
    '''
    # Teste de dimensão entre vetores
    if (len(x)!=len(y)): return print('Falha! X e Y tem dimensões diferentes!') 
    
    # Estrutura básica de regressão linear
    n=len(x)
    Sx ,Sy  = sum(x)   , sum(y)
    Sxy,Sxx = sum(x*y) , sum(x**2)
    a1=(n*Sxy-Sx*Sy)/(n*Sxx-Sx**2)
    a0=(Sxx*Sy-Sxy*Sx)/(n*Sxx-Sx**2)
    px=[a1,a0] 
        
    return px
    
def results(r2,y2,xint,x,y,px,graph=1):    
    # Exibição de resultados
    yint=np.polyval(px,xint)
    print(f'O valor {xint} linearmente interpolado resulta em: {round(yint,2)}')          
    print(f"Coeficiente de determinação(r²):{round(r2,4)}",)
    
    if graph==1:
        p=pol(px,digitos_coef=4)
        plt.title("Regressão Linear")        
        plt.plot(x,y,'*r',label='Medições')
        plt.plot(x,y2,'--b',label=p)
        plt.plot(xint,yint,'oy',label="yint",markersize=12)
        plt.text(0.75, 0.05, f'$R^2 = {round(r2,4)}$', fontsize=12, 
                 transform=plt.gca().transAxes)
        plt.legend(fontsize=18)
        plt.legend()
        plt.style.use('ggplot')
        plt.show()

#%% Simulação
# =============================================================================
if __name__=="__main__":
    # Carregando as dados de um arquivo externo chamada dados.csv    
    
    import pandas as pd
    df=pd.read_csv("dados.csv")
    x=df[df.columns[0]]
    y=df[df.columns[1]]
    xint=30
    
    # Chamadas de métodos
    px = reglin(x,y,xint)
    y_pred = np.polyval(px, x)
    r2 = ea.r2(y, y_pred)
    
    # Chamada de resultados e gráficos
    results(r2,y_pred,xint,x,y,px,graph=1)

''' 
   Para utilizar o código com dados externos pode-se :
       * Organizar uma planilha eletrônica com os dados em colunas;
       * Salvar o arquivo em formato '.csv' no mesmo endereço do arquivo '.py';
       * Executar o script abaixo para converter as colunas em vetores de dados
       de interesse para análise. Utilize a coluna '0' para x e 
       a coluna '1' em y, por exemplo:
           
        import pandas as pd
        df = pd.read_csv('dados.csv')
        x=df[df.columns[0]].values
        y=df[df.columns[1]].values
        
'''
