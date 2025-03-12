#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tue May 18 17:28:19 2021
@author: Jonatha Rodrigues da Costa
"""
import time
import numpy as np

class  MetSol: 
    def __init__(self,a,b,imax,Err,tol,f):
        self.a = a
        self.b = b
        self.imax = imax
        self.Err = Err
        self.tol = tol
        self.f =f
        print("Objeto instanciado!")
    
    
    def dfdx(self,fun,x):
        from scipy.misc import derivative
        return derivative(fun,x,1e-10)
        
    
    def graf(self,X,title):
        import matplotlib.pyplot as plt  
        plt.figure()
        x=[X[i][0] for i in range(len(X))]
        y=[X[i][1] for i in range(len(X))]        
        plt.plot(x,y,'bo--',label='f(x)')
        plt.legend()
        plt.xlabel('Iterações');plt.ylabel('Valores de x');
        plt.title(f'{title}')
        plt.style.use('ggplot')

    def imp_tab(self,s):        
        print()
        print(60*'-')
        print(f'Método da {s}!')
        print('Intervalo de análise [%d,%d].\n' %(self.a,self.b) )
        print('iteração  a       b        x     f(a)    f(x)       f(b)')
        print(60*'-')
# =============================================================================
#        Bisseção
# =============================================================================
    def bissec(self):
        self.imp_tab('bisseção')         
        t0=time.process_time()  # Ligar cronômetro      
        if self.f(self.a)*self.f(self.b)>0:
            print('A raiz não está contida no intervalo \
                  dado [%d,%d]!'%(self.a,self.b))
            print('Por favor teste um novo intervalo [a,b].')
        else:
            X=[]
            a,b=self.a, self.b
            for i in range(self.imax):
                x=(a+b)/2
                X.append((i,x))
                toli=(b-a)/2
                print('    %d   %.3f    %.3f   %.3f   %.3f   %.3f    %.3f'
                      %(i+1,a,b,x,self.f(a),self.f(x),self.f(b)))
                if (self.f(a)*self.f(x)<0):   # Raiz localizada entre a e x >> novo b
                    b=x             
                else:               # Raiz localizada entre b e x >> novo a
                    a=x 
                if(toli<self.tol):
                    break
            print()
            print('Solução x=',format(x,'.3f'),'encontrada após',i+1,'iterações!')    
            print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))
            self.graf(X,'Metodo da bisseção')
# =============================================================================
#  Regula Falsi
# =============================================================================
    def regfalsi(self):
        '''
        Os métodos de regula falsi e falsa posição são, na verdade, o mesmo método, apenas com nomes diferentes. 
        Ambos são métodos numéricos usados para encontrar raízes de funções não lineares.
        Diferenças nominais    
            Regula Falsi: Nome em latim que significa "regra da falsidade".
            Falsa Posição: Tradução para o português ou outras línguas, mantendo o mesmo significado.
        '''
        
        self.imp_tab('regula falsi')
        t0 = time.process_time()         #   Ligar cronômetro
        if self.f(self.a)*self.f(self.b)>0:
            print('A raiz não está contida no intervalo \
                  dado [%d,%d]!'%(self.a,self.b))
            print('Por favor teste um novo intervalo [a,b].')
        else:
            X=[]
            a,b = self.a, self.b
            for i in range(self.imax):
                x=(a*self.f(b) - b*self.f(a) ) / ( self.f(b)-self.f(a) )
                X.append((i,x))
                toli=(b-a)/2
                print('    %d   %.3f    %.3f   %.4f   %.3f   %.3f    %.3f' 
                      %(i+1,a,b,x,self.f(a),self.f(x),self.f(b)))                           
                if self.f(a)*self.f(x)>0:   # Raiz localizada entre [a,x] >> [a,b=x]
                    a=x             
                else:               # Raiz localizada entre [x,b] >> [a=x,b]
                    b=x
                if(toli<self.tol):
                    print(60*'-')
                    break
            print()
            print('Solução x=',format(x,'.4f'),'encontrada após',i+1,'iterações!')    
            print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))
                            # Solução gráfica     
            self.graf(X,'Método Regula Falsi')

# =============================================================================
# Secante
# =============================================================================
    def sec(self):
        self.imp_tab('Secante')
        t0 = time.process_time()         #   Ligar cronômetro
        if self.f(self.a)*self.f(self.b)>0:
            print('A raiz não está contida no intervalo\
                  dado [%d,%d]!'%(self.a,self.b))
            print('Por favor teste um novo intervalo [a,b].')
        else:
            X=[]
            x1,x2=self.a,self.b
            for i in range(self.imax):
                Xsn=x2-self.f(x2)*(x1-x2)/( self.f(x1)-self.f(x2) )     # Xsn=x(i+1);Xest=x(i)  
                X.append((i,Xsn))
                print('    %d   %.3f    %.3f   %.4f   %.3f   %.3f    %.3f' 
                      %(i+1,self.a,self.b,Xsn,self.f(self.a),self.f(Xsn),self.f(self.b))) 
                if(abs( (Xsn-x2) / x2)<self.Err):
                    break
                if abs(self.f(Xsn))<self.Err:
                    break
                if i==self.imax:
                    print(f'A solução não foi encontrada após {i} iterações')
                    break
                x1,x2=x2,Xsn 
            print(60*'-')
            print('Solução x=',format(Xsn,'.4f'),'encontrada após',i+1,'iterações!')    
            print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))                            
            self.graf(X,'Método da Secante')
            
# =============================================================================
# Newton Rapson
# =============================================================================
    def newtonrapson(self):
        self.imp_tab('Newton Rapson')
        
        import random  as rd
        t0 = time.process_time()         #   Ligar cronômetro
        Xest=rd.uniform(self.a,self.b)
        X=[]
        for i in range(self.imax):
            Xsn=Xest- (self.f(Xest))/( self.dfdx(self.f,Xest) )        # Xsn=x(i+1);Xest=x(i)  
            X.append((i,Xest))
            print('    %d   %.3f    %.3f   %.4f   %.3f   %.3f    %.3f' 
                      %(i+1,self.a,self.b,Xsn,self.f(self.a),self.f(Xsn),self.f(self.b)))     
            if(abs( (Xsn-Xest) / Xest)<self.Err):
                break           
            if i==self.imax:
                print(f'A solução não foi encontrada após {i} iterações')
                break
            Xest=Xsn
        print(60*'-')
        print('Solução x=',format(Xsn,'.4f'),'encontrada após',i+1,'iterações!')    
        print('Tempo de processamento computacional:%.4fs' %(time.process_time()-t0))
        self.graf(X,'Método Newton Rapson')            
            
        
                       
# =============================================================================
#         
# =============================================================================

def escopo():
    a, b, imax = 2, 3, 30
    Err, tol= 0.01, 0.001
    f=lambda x: 8-4.5*(x - np.sin(x))
    
    s=MetSol(a,b,imax,Err,tol,f)   
    s.bissec()
    s.regfalsi()
    s.sec()
    s.newtonrapson()
        
        
if __name__== '__main__':
     escopo()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        