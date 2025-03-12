#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Thu May 20 15:09:14 2021
@author: Jonatha Rodrigues da Costa

Ao avaliar a qualidade de estimadores ou modelos de regressão, é importante 
utilizar várias métricas para analisar os erros. 
Algumas das principais métricas usadas para avaliar o desempenho de 
estimadores são:

1. Erro Absoluto Médio (MAE - Mean Absolute Error)
2. Erro Quadrático Médio (MSE - Mean Squared Error)
3. Raiz do Erro Quadrático Médio (RMSE - Root Mean Squared Error)
4. Erro Médio Percentual Absoluto (MAPE - Mean Absolute Percentage Error)
5. Coeficiente de Determinação (R²)
6. Erro Médio (Bias)
7. Erro Médio Logarítmico Quadrático (MSLE - Mean Squared Logarithmic Error)
8. Erro Quadrático Médio Ponderado (WMSE - Weighted Mean Squared Error)
"""

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def mae(y_true, y_pred):
    '''
    Fórmula: MAE = 1/n ​∑(i=1 ^n) ​∣yi​−y^​i​∣
    Descrição: Fornece a média das diferenças absolutas entre os valores 
    observados (yi​) e os valores preditos (y^​i​). 
    Fornece uma noção direta da magnitude média dos erros.
    '''
    return mean_absolute_error(y_true, y_pred)
     
def mse(y_true, y_pred):
    '''
    Fórmula:   MSE = 1/n​ ∑(i=1 ^n)​ (yi​−y^​i​)²
    Descrição: Mede a média das diferenças ao quadrado entre os 
    valores observados e preditos. 
    Penaliza erros grandes mais severamente do que erros menores, 
    devido ao termo ao quadrado.    
    '''    
    return mean_squared_error(y_true, y_pred)
    
def rmse(y_true, y_pred):
    '''        
    Fórmula: RMSE = ( ∑(i=1 ^n) (yi−y^i)2 )1/2
    Descrição: É a raiz quadrada do MSE. Fornece uma medida da magnitude do 
    erro na mesma unidade dos dados originais, facilitando a interpretação.
    '''
    erro = mse(y_true, y_pred)
    return np.sqrt(erro)

def mape(y_true, y_pred):
    '''
    MAPE= 100% / n​ ∑(i=1^n)​ abs( (yi​​−y^​i​​)/yi  )
    Descrição: Mede o erro absoluto como uma porcentagem dos valores observados.
    É útil para entender o erro em termos relativos, contudo pode ser problemático 
    se houver valores observados muito próximos de zero.    
    '''
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def r2(y_true, y_pred):
    '''
    Fórmula: R2 = 1 − (SSres/ SStot)
    Descrição: Mede a proporção da variância nos dados que é explicada 
    pelo modelo. Um valor mais próximo de 1 indica um bom ajuste, enquanto 
    um valor próximo de 0 indica um ajuste ruim.
    '''
    return r2_score(y_true, y_pred)

def bias(y_true, y_pred):
    '''
    Fórmula:   Bias = 1/n ​∑(i=1 ^n) ​(yi​−y^​i​)
    Descrição: Fornece a média das diferenças entre os valores observados 
    e preditos. Um valor de viés próximo de zero indica que o estimador 
    é imparcial.
    '''
    return np.mean(y_pred - y_true)

def msle(y_true, y_pred):
    ''' 
    Fórmula: MSLE = 1/n ∑ (i=1 ^n) ( log⁡(1+yi)−log⁡(1+y^i) )²
    Descrição: Semelhante ao MSE, mas aplicado aos logaritmos dos valores.
    É útil quando a diferença relativa entre os valores é mais importante que 
    a diferença absoluta.    
    '''
    return mean_squared_error(np.log1p(y_true), np.log1p(y_pred))

def wmse(y_true, y_pred,weights = np.array([0.1, 0.2, 0.3, 0.4])):
    '''
    Fórmula:  WMSE = 1/n ∑(i=1^n) wi*(yi−y^i)2
    Descrição: Uma versão ponderada do MSE onde cada erro é multiplicado 
    por um peso (wiwi​). Útil quando se quer dar mais importância a certos 
    pontos.
    '''    
    return np.sum(weights * (y_true - y_pred) ** 2) / np.sum(weights)
    
#%%
if __name__== "__main__":
    # Dados de exemplo (valores observados e valores preditos por um p(x).) 
    y_true = np.array([3.0, -0.5, 2.0, 7.0])
    y_pred = np.array([2.5, 0.0, 2.0, 8.0])
    
    # Exibir resultados
    print()
    print(f"Mean Absolute Error (MAE): {mae(y_true, y_pred):.4f}")
    print(f"Mean Squared Error (MSE): {mse(y_true, y_pred):.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse(y_true, y_pred):.4f}")
    print(f"Mean Absolute Percentage Error (MAPE): {mape(y_true, y_pred):.2f}%")
    print(f"Coefficient of Determination (R^2): {r2(y_true, y_pred):.4f}")
    print(f"Bias: {bias(y_true, y_pred):.4f}")
    print(f"Mean Squared Logarithmic Error (MSLE): {msle(y_true, y_pred):.4f}")
    print(f"Weighted Mean Squared Error (WMSE): {wmse(y_true, y_pred):.4f}")

