#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações não lineares
Método de Newton Raphson'
Prof. Jonatha Costa
"""
import time
import sympy as sym
print('\014')
# =============================================================================
def cal_NewtonRapson(fun,imax=30,Err=1e-3,tol=1e-4,graph=1):   
    f=sym.Lambda(x,fun)
    df=sym.Lambda(x,sym.diff(f(x),x))    
    Xest=(2+3)/2
    print('Métodos numéricos - Solução de equações não lineares.')
    print('Método da Newton Raphson!')
    print(60*'-')
    t0 = time.process_time()                    #   Ligar cronômetro
    # =============================================================================
    X=[]
    for i in range(imax):
        Xsn=Xest- float(f(Xest))/float(df(Xest))        # Xsn=x(i+1);Xest=x(i)  
        X.append(Xest)
        if(abs( (Xsn-Xest) / Xest)<Err):
            print(f'Solução {Xsn} alcançada com {i} iterações')
            break
        if abs(f(Xsn))<Err:
            print(f'Solução {Xsn} alcançada com {i} iterações e tolerância {f(Xsn)}',f(Xsn))
            break
        if i==imax:
            print(f'A solução não foi encontrada após {i} iterações')
            break
        Xest=Xsn   
    print(f'Solução x={round(Xest,4)},encontrada após {i+1} iterações!')    
    print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))
    if graph==1:         # Solução gráfica              
        p=sym.plot(f(x),(x,-2,2),line_color='blue',show=False)
        r=sym.plot(df(x),(x,-2,2),line_color='red',show=False)
        p.extend(r)
        p.legend=True
        p.show()
#%%

x=sym.Symbol('x')
fun  = 8-4.5*(x - sym.sin(x))

cal_NewtonRapson(fun,graph=1)

