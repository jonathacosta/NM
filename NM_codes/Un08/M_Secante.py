#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações não lineares
Método da Secante'
Prof. Jonatha Costa
"""
import numpy as np
import matplotlib.pyplot as plt
import time
print('\014')
# =============================================================================
# Função 
# =============================================================================

f= lambda x: 8-4.5*(x - np.sin(x))    
Err=0.001
tol=Err
x1,x2=2,3
imax=50

print('Métodos numéricos - Solução de equações não lineares.')
print('Método da Secante!')
print('Intervalo de análise [%d,%d].\n'%(x1,x2) )
print(60*'-')
t0 = time.process_time()         #   Ligar cronômetro
# =============================================================================
X=[]
for i in range(imax):
    Xsn=x2-f(x2)*(x1-x2)/( f(x1)-f(x2) )     # Xsn=x(i+1);Xest=x(i)  
    X.append(Xsn)
    if(abs( (Xsn-x2) / x2)<Err):
        break
    if abs(f(Xsn))<Err:
        break
    if i==imax:
        print(f'A solução não foi encontrada após {i} iterações')
        break
    x1,x2=x2,Xsn   
print('Solução x=',format(Xsn,'.4f'),'encontrada após',i+1,'iterações!')    
print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))
 # Solução gráfica     
plt.plot(X,np.array(f(X)),'r*--',label='f(x)=8-4.5*x - np.sin(x)')
plt.plot(X[-1],f(X[-1]),'bo',label='Solução')
plt.legend()
plt.title('Convergência para zeros da função.')
plt.style.use('ggplot')
       














