#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Regressão Polinomial
Prof. Jonatha Costa

Conceito:
    A regressão polinomial é uma extensão da regressão linear que permite modelar 
    a relação entre a variável dependente y e a variável independente x como um 
    polinômio de grau n. Enquanto a regressão linear simples ajusta uma linha reta
    aos dados, a regressão polinomial ajusta uma curva, permitindo modelar relações
    mais complexas e não lineares.

Modelo da Regressão Polinomial    
    A equação da regressão polinomial de grau nn é dada por:
            y=b0+b1x+b2x2+b3x3+…+bnxn
    Onde:
        y é a variável dependente.
        x é a variável independente.
        b0,b1,b2,…,bnb0​,b1​,b2​,…,bn​ são os coeficientes do polinômio.
        n é o grau do polinômio.        
    
Transformação de Variáveis: 
    A variável independente x é elevada a diferentes potências (graus), criando 
    uma nova matriz de variáveis independentes [x,x2,x3,…,xn].

Ajuste do Modelo: 
    O modelo é ajustado aos dados usando o método dos mínimos quadrados, assim 
    como na regressão linear, mas agora com os termos polinomiais incluídos.

Curva de Ajuste: 
    A curva ajustada pode modelar relações não lineares, oferecendo uma melhor 
    adequação quando a relação entre xx e yy não é simplesmente linear.        
        
Vantagens da Regressão Polinomial

    Modelagem de Relações Não Lineares: Permite capturar padrões nos dados que
    a regressão linear simples não consegue.
    Flexibilidade: Aumentar o grau do polinômio pode aumentar a precisão do 
    modelo, desde que seja feito com cuidado.
    Simples Implementação: Relativamente fácil de implementar usando bibliotecas
    padrão de regressão linear, apenas transformando a variável independente.

Desvantagens da Regressão Polinomial

    Overfitting: Com um grau muito alto, o modelo pode ajustar-se demais aos 
    dados de treinamento, capturando o "ruído" em vez da tendência real, o que
    resulta em um desempenho ruim em novos dados.
    Instabilidade: Polinômios de alta ordem podem oscilar significativamente 
    entre os pontos de dados, especialmente nas extremidades do intervalo 
    (fenômeno de Runge).
    Interpretação Mais Complexa: Coeficientes em polinômios de alta ordem são 
    mais difíceis de interpretar em termos práticos do que em uma regressão 
    linear simples.    
    
Escolha do Grau do Polinômio
A escolha do grau nn é crítica:
    Um polinômio de grau muito baixo pode subestimar a relação (underfitting).
    Um polinômio de grau muito alto pode sobrestimar a relação (overfitting).
    
Métodos como validação cruzada são frequentemente usados para determinar o grau 
    adequado,balanceando a complexidade do modelo e seu desempenho preditivo.    
    
Comparação com Regressão Linear
    Linear vs. Não Linear: Enquanto a regressão linear modela uma relação linear, 
    a regressão polinomial pode modelar relações mais complexas.
    Flexibilidade: A regressão polinomial é mais flexível, mas isso vem ao custo 
    de maior risco de overfitting e instabilidade numérica.

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
        plt.plot(x,y,'-*r',label='Medições')
        plt.plot(x,y2,'-ob',label=p,markersize=4)
        plt.plot(xint,yint,'oy',label="yint",markersize=12)
        plt.text(0.75, 0.05, f'$R^2 = {round(r2,4)}$', fontsize=12, 
                 transform=plt.gca().transAxes)
        plt.legend(fontsize=18)
        plt.legend()
        plt.style.use('ggplot')
        plt.show()
        
#     
# =============================================================================
if __name__=="__main__":
    #Dados
    x=np.array(list(range(0,110,10)))
    y=np.array([ 0.94, 0.96, 1.0, 1.05, 1.07, 1.09, 1.14, 1.17, 1.21, 1.24, 1.28])  
    m=2    # Grau
    xint=3    
    # Chamadas de métodos
    px = RegPol(x,y,m)
    y_pred = np.polyval(px, x)
    r2 = ea.r2(y, y_pred)             
    # Chamada de resultados e gráficos
    results(r2,y_pred,xint,x,y,px,graph=1)
    # Polinônio
    print(f'\n\nPolimônio de grau {m}: p(x)=',pol(px,digitos_coef=6))


    


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
