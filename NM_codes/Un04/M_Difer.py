#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos
Dferenciação
Prof. Jonatha Costa
"""
from scipy.misc import derivative
print('\14')
# =============================================================================
# Dados de entrada
# =============================================================================
x=[2,3,4]
p=3
i=filter(lambda n:n == p,x)
i=x.index(p)

# =============================================================================
f=lambda y:y**3
dp=( f(x[i+1]) - f(x[i]) )/(x[i+1]-x[i])
dr=( f(x[i]) - f(x[i-1]) )/(x[i]-x[i-1])
dc=( f(x[i+1]) - f(x[i-1]) )/(x[i+1]-x[i-1])
der=round(derivative(f,p,dx=1e-1),2)                    # Analítico e erro
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

print()
#%=============================================================================
# ABORDAGENS OPTATIVAS PARA DIFERENCIAÇÃO 
# =============================================================================
# OPÇÃO 01
import sympy as sym
x=sym.Symbol('x')
g=x**3
dg=sym.Derivative(g).doit()
k=dg.subs(x,p)
print(k,'- Trabalhado com Sympy, Derivative(g).doit() e subs(x,valor).')
# =============================================================================
# OPÇÃO 02
import sympy as sym
x=sym.Symbol('x')
g=sym.Lambda(x,x**3)
dg=sym.Lambda(x, sym.diff(g(x),x) )
k=dg(p)
print(k,'- Trabalhado com Sympy, Lambda(x, sym.diff(g(x),x) e f(valor).')






