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
def der_num(x,y,p,f):
    
    if (p<min(x) or p> max(x)):
        print(f"\nPonto 'x={p}' de análise fora do domínio do intervalo!\n")
    
    else:            
        try:
            # Encontrar o índice de p na lista x
            i = x.index(p)
            E=[]
            df_dx = grad(f); der = df_dx(float(p))       
            
            if i==0:            
                dp=( y[i+1] - y[i])/(x[i+1]-x[i])
                dr,dc=None,None
                
                print('-'*50, f"\nRESULTADOS para o ponto x='{p}':\n", '-'*50, sep='')
                print("Analítica \tProgr\t\tCentral\t \tRegress")
                print(f" {der}\t \t  {dp} \t\t  {dc}     \t   {dr}")               
                E.append(round(abs(der-dp)/der,2))
                E.append(dc)
                E.append(dr)
                print(f" Erros:\t\t {round(E[0]*100,2)}% \t\t  {E[1]}     \t   {E[2]}")
                
            elif i==len(x)-1:
                dr=( y[i] - y[i-1])/(x[i]-x[i-1])
                dp,dc=None,None                
                print('-'*50, f"\nRESULTADOS para o ponto x='{p}':\n", '-'*50, sep='')
                print("Analítica \tProgr\t\tCentral\t \tRegress")
                print(f" {der}\t \t  {dp} \t\t  {dc}     \t   {dr}")               
                
                E.append(dp)
                E.append(dc)
                E.append(round(abs(der-dr)/der,2))                
                print(f" Erros:\t\t  {E[0]}  \t\t  {E[1]}  \t\t {round(E[2]*100,2)}%")
                                                                
            else:
                dp=( y[i+1] - y[i])/(x[i+1]-x[i])
                dr=( y[i] - y[i-1])/(x[i]-x[i-1])
                dc=( y[i+1] - y[i-1])/(x[i+1]-x[i-1])  
                
                print('-'*50, f"\nRESULTADOS para o ponto x='{p}':\n", '-'*50, sep='')
                print("Analítica \tProgr\t \t\tCentral\t \tRegress")
                print(f" {der}\t \t  {dp}         \t  {dc}     \t   {dr}")               
                E.append(round(abs(der-dp)/der,2))
                E.append(round(abs(der-dc)/der,2))
                E.append(round(abs(der-dr)/der,2))
                print(f" Erros:\t\t {E[0]*100}%        \t  {E[1]*100}%     \t   {E[2]*100}%")
            
        except ValueError:
            print(f"\nValor 'x={p}' está fora da lista.\nUma interpolação pode ser necessária!\n")            
                                       
    
#%%=============================================================================
if __name__=="__main__":
    f=lambda y:y**3     
    # x=[2,3,4,5,6];   
    # y=[f(i) for i in x]  
    # # Pontos de análise
    # print(x);
    # for p in [1.5, 2,3,6]:        
    #     der_num(x,y,p,f)
        
    y=[80,75,70,65,60]
    x=[2,3,4,5,6]      
    for p in [3,4]:        
            der_num(x,y,p,f)
            
        
        
