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
def der_num(x,p,f):
    i=x.index(p)
    dp=( f(x[i+1]) - f(x[i]) )/(x[i+1]-x[i])
    dr=( f(x[i]) - f(x[i-1]) )/(x[i]-x[i-1])
    dc=( f(x[i+1]) - f(x[i-1]) )/(x[i+1]-x[i-1])
    df_dx = grad(f); der = df_dx(float(p))    # Derivada analítica via autograd
    
    print('-'*50)
    print("RESULTADOS:")
    print('-'*50)
    print("Dif.Analítica \tDif.Prog\tDif.Central\tDif.Regr")
    print(f" {der}\t \t  {dp}         \t  {dc}     \t   {dr}")
    
    E=[]
    E.append(round(abs(der-dp)/der,2))
    E.append(round(abs(der-dc)/der,2))
    E.append(round(abs(der-dr)/der,2))
    print(f" Erros:\t\t {E[0]}%        \t  {E[1]}%     \t   {E[2]}%")

#%%=============================================================================
if __name__=="__main__":
    f=lambda y:y**3 
    x=[2,3,4,5,6]; p=4
    der_num(x,p,f)
