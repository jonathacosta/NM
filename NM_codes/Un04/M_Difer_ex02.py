#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos
Diferenciação via exercícios 01
Prof. Jonatha Costa
"""


#%%
'''
Versão 03 - versão 02 utilizando métodos def
'''
import sympy as sp
# *****************************************************************************
# Lista de valores

def dados_entrada():
    entrada = input("Insira os pontos do domínio separados por vírgula: ").split(',')
    X = list(map(int, entrada))
    ponto_p= int(input("Informe o ponto de referência da lista para cálculo da derivada numérica"))

    # Função filtro para localizar o ponto_p na lista
    i=filter(lambda n:n == ponto_p,X)
    # Índice de locação do ponto na lista X
    i=X.index(ponto_p)

    return X,ponto_p,i

# Função para derivada analítica com auxílio da biblioteca sympy
def derivada(k): 
    x = sp.Symbol('x')
    fun = k(x)    
    dh=sp.diff(fun,x,1)              # Derivada primeira
    
    return sp.lambdify(x,dh,'numpy') 


def calculo_derivadas(f,X,ponto_p):
# # *****************************************************************************
# Derivada Analítica incluída automaticamente a partir da função 'derivada' criada
    df1=derivada(f)

    deriv = df1(ponto_p)
    # Derivada numérica
    dprog  =( f(X[i+1]) - f(X[i]) ) / (X[i+1]-X[i])
    dcentr =( f(X[i+1]) - f(X[i-1]))/ (X[i+1]-X[i-1])
    dregr  =( f(X[i]) - f(X[i-1]) ) / (X[i]-X[i-1])

    return dprog,dcentr,dregr,deriv    
# # *****************************************************************************
# Resultados

# # *****************************************************************************
# Resultados do erros
def calculo_erros(dprog,dcentr,dregr,deriv):
    E=[]
    for i in [dprog,dcentr,dregr]:
        E.append(round(abs(i-deriv)/deriv,2))    
    return E

def resultados(E,dprog,dcentr,dregr,deriv):
    print('-'*50)
    print("RESULTADOS:")
    print('-'*50)
    print("Dif.Analítica \tDif.Prog\tDif.Central\tDif.Regr")
    print(f" \t{deriv}\t  {dprog}         \t  {dcentr}     \t   {dregr}")
    print(f"\n Erros:\t\t {E[0]*100}%    \t  {E[1]*100}%     \t   {E[2]*100}%")


if __name__ == "__main__":    
    # Função de análise
    f=lambda x:x**3
    # *****************************************************************************
    X,ponto_p,i = dados_entrada()       
    dprog,dcentr,dregr,deriv = calculo_derivadas(f,X,ponto_p)
    E=calculo_erros(dprog,dcentr,dregr,deriv)
    resultados(E,dprog,dcentr,dregr,deriv)
    
    
#%%
'''
Versão 02 - Solução em classe com  o método construtor init e variáveis globais (self)
'''
class DifNumeric():
    def __init__(self,f):
        
        self.f=f
        self.X=None
        self.dados_entrada()       
        self.calculo_derivadas()
        self.calculo_erros()
        self.resultados()    
    
# Lista de valores
    def dados_entrada(self):
        entrada = input("Insira os pontos do domínio separados por vírgula: ").split(',')
        X = list(map(int, entrada))
        ponto_p= int(input("Informe o ponto de referência da lista para cálculo da derivada numérica"))

        # Função filtro para localizar o ponto_p na lista
        i=filter(lambda n:n == ponto_p,X)
        # Índice de locação do ponto na lista X
        i=X.index(ponto_p)

        self.X=X
        self.ponto_p=ponto_p
        self.i=i

    
    def derivada(self,k): 
        # Função para derivada analítica com auxílio da biblioteca sympy
        x = sp.Symbol('x')
        fun = k(x)    
        dh=sp.diff(fun,x,1)              # Derivada primeira

        return sp.lambdify(x,dh,'numpy') 


    def calculo_derivadas(self):
        # # *****************************************************************************
        # Derivada Analítica incluída automaticamente a partir da função 'derivada' criada
        df1=self.derivada(self.f)
        self.deriv = df1(self.ponto_p)
        
        # Derivada numérica
        X,i=self.X,self.i
        self.dprog  =( f(X[i+1]) - f(X[i]) ) / (X[i+1]-X[i])
        self.dcentr =( f(X[i+1]) - f(X[i-1]))/ (X[i+1]-X[i-1])
        self.dregr  =( f(X[i]) - f(X[i-1]) ) / (X[i]-X[i-1])

    def calculo_erros(self):
        # Resultados do erros

        E=[]
        for i in [self.dprog,self.dcentr,self.dregr]:
            E.append(round(abs(i-self.deriv)/self.deriv,2))    
        self.E = E

    def resultados(self):
        print('-'*50)
        print("RESULTADOS:")
        print('-'*50)
        print("Dif.Analítica \tDif.Prog\tDif.Central\tDif.Regr")
        print(f" \t{self.deriv}\t  {self.dprog}         \t  {self.dcentr}     \t   {self.dregr}")
        print(f"\n Erros:\t\t {self.E[0]*100}%    \t  {self.E[1]*100}%     \t   {self.E[2]*100}%")

        
f=lambda x:x**3
a=DifNumeric(f)        
    