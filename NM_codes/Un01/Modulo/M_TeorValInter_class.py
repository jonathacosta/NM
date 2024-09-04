#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mon Apr 19 11:21:18 2021
@author: Jonatha Rodrigues da Costa
"""
import numpy as np
import matplotlib.pyplot as plt

# Teorema da valor intermediário >> trabalhando com classes
#%%
class JRC:    
    def f(self,x):
        return x**4 + 2.*x+4.

    def al(self,a,b):
        import random as rd
        if (b-a)<=1.:
            return a+rd.random() 
        else:
            return  rd.randrange(int(a),int(b))+rd.random()
           
    def graf(self,x,y,n=1): 
        plt.figure()
        x0= np.linspace(x,y)
        y0= self.f(x0)  
        plt.plot(x0,y0,label='f(x)')
        x1= np.array([ self.al(x,y) for i in range(int(n)) ])
        y1= self.f(x1)
        plt.plot(x1,y1,'g*',label='x aleatório')
        plt.title(f'Teorema do valor intermediário com {n} pontos')
        plt.legend()
        plt.style.use('ggplot')
#
k=JRC().graf(1,10,10)

#%% Class com o método construtor init
class JRC:    
    def __init__(self,a,b,n):
        self.a=a
        self.b=b
        self.n=n
    
    def f(self,x):
        return x**4 + 2.*x+4.

    def al(self):
        import random as rd
        if (self.b-self.a)<=1.:
            return self.a+rd.random() 
        else:
            return  rd.randrange(int(self.a),int(self.b))+rd.random()
           
    def graf(self): 
        plt.figure()
        x0= np.linspace(self.a,self.b)
        y0= self.f(x0)  
        plt.plot(x0,y0,label='f(x)')
        x1= np.array([ self.al() for i in range(int(self.n)) ])
        y1= self.f(x1)
        plt.plot(x1,y1,'g*',label='x aleatório')
        plt.title(f'Teorema do valor intermediário com {self.n} pontos')
        plt.legend()
        plt.style.use('ggplot')
 
# Neste método, as entradas principais são na classe.
# Entradas adicionais, nas funções; se necessário.   
# Alerta para não carregar com atribuitos extras. 
# Se a função é definida como al(self), a chamada dela deve ser vazia al(self)
#         
# =============================================================================
l=JRC(1,10,5).graf()
l,k





