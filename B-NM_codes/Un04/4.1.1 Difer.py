#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos
Dferenciação numérica
Prof. Jonatha Costa

- A diferenciação numérica é uma técnica usada para aproximar a derivada de uma 
função com base em valores discretos da função, ao invés de uma expressão 
analítica exata. Em muitas aplicações práticas, como engenharia e ciência de 
dados, as funções podem não ser conhecidas de forma exata ou podem ser muito 
complexas para diferenciar simbolicamente. Nesse contexto, usamos métodos 
numéricos para calcular as derivadas.

# ----------------------------------------------------------------------
- Derivada e Diferenciação Numérica:

    A derivada de uma função f(x)f(x) em um ponto xx é uma medida da taxa 
    de variação da função em relação a xx, definida matematicamente 
    como o limite:
                f′(x) = lim(⁡Δx→0)  ( f(x+Δx)−f(x) )/ Δx
    
    Como o valor de Δx nunca é exatamente zero em uma computação numérica,
    utilizam-se aproximações para calcular esse limite.
    
# ----------------------------------------------------------------------
- Diferença Finita Progressiva: 
    Aproxima a derivada com uma pequena variação positiva em x:
    f′(x)≈ (f(x+h)−f(x)) / h, em que h é um pequeno incremento.

- Diferença Finita Regressiva: 
    Usa uma variação negativa em x:
    f′(x)≈ (f(x)−f(x-h)) / h, em que h é um pequeno incremento.

- Diferença Finita Central: 
    Fornece uma melhor aproximação usando a média de uma variação 
    positiva e negativa de x.
    
    f′(x)≈ (f(x+h)−f(x-h)) / 2h, em que h é um pequeno incremento.
    
    Este método geralmente é mais preciso, pois reduz o erro de 
    truncamento de ordem maior.

# ----------------------------------------------------------------------
A diferenciação numérica é amplamente utilizada em várias áreas, como:

    Simulações de engenharia: 
        Para calcular gradientes em problemas de otimização.
    Análise de dados: 
        Para estimar taxas de variação em conjuntos de dados 
        experimentais.
    Métodos numéricos: 
        Em equações diferenciais parciais (EDPs), onde as derivadas 
        são aproximadas numericamente.   
"""

from autograd import grad
def der_num(x,y,p):
    
    if p<min(x) or p> max(x):
        print(f"\nPonto 'x={p}' de análise fora do domínio do intervalo!\n")        
        return None,None,None

    elif p not in x:
            print(f"\nValor 'x={p}' está fora da lista.\nUma interpolação pode ser necessária!\n")            
            return None,None,None
  
    else:            
        try:
            # Encontrar o índice de p na lista x
            i = x.index(p)
            dp,dr,dc = None,None,None
            if i==0:            
                dp=( y[i+1] - y[i])/(x[i+1]-x[i])                                
                                
            elif i==len(x)-1:
                dr=( y[i] - y[i-1])/(x[i]-x[i-1])
                                                                                
            else:
                dp=( y[i+1] - y[i])/(x[i+1]-x[i])
                dr=( y[i] - y[i-1])/(x[i]-x[i-1])
                dc=( y[i+1] - y[i-1])/(x[i+1]-x[i-1])  
                                    
        finally:
            return dp,dr,dc
                           
def Resultados(dp,dr,dc,p,f):            
        df_dx = grad(f); der = df_dx(float(p))   
        print('-'*50, f"\nRESULTADOS para o ponto x='{p}':\n", '-'*50, sep='')
        print("Analítica \tProgr\t \t\tCentral\t \tRegress")
        print(f" {der}\t \t  {dp}         \t  {dc}     \t   {dr}")                       
        E=[]
        for derivada_num in [dp,dc,dr]:
            if derivada_num==None: E.append(None)
            else: E.append(round(abs(der-derivada_num)/der,2)) 
        print(f" Erro(%): \t {E[0]}  \t\t\t  {E[1]}     \t   {E[2]}")
        
    
    
#%%=============================================================================
if __name__=="__main__":
    f=lambda y:y**3     
    x=[2,3,4,5,6]; 
    y=[f(i) for i in x]
    # Pontos de análise
    print(x);
    for p in [1,5, 2, 3, 6, 6.5]:        
        dp,dr,dc= der_num(x,y,p)
        Resultados(dp,dr,dc,p,f)