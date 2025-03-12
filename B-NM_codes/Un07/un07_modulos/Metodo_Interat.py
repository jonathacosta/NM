#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tue May 18 17:28:19 2021
@author: Jonatha Rodrigues da Costa
Métodos iterativos
"""
import numpy as np
class  MetIter: 
    
    def __init__(self,A,Y,n=20):
        self.A = A 
        self.Y = Y 
        self.n = n
        print('Objeto instanciado!')     
    def met_jacobi(self):                  
        a,b,c,err = 0, 0, 0, 0.001
        x1,x2,x3 = 0, 0, 0
        
        print('\n****** Método Iterativo de Jacobi ******\n')
        print(' k \t  x1 \t  x2 \t  x3')                             
        for k in range(1,self.n):
            a=(self.Y[0]-(self.A[0,1]*x2 + self.A[0,2]*x3))/self.A[0,0]           # Atualiza a e usa Xi anterior
            b=(self.Y[1]-(self.A[1,0]*x1 + self.A[1,2]*x3))/self.A[1,1]           # Atualiza b e usa Xi anterior
            c=(self.Y[2]-(self.A[2,0]*x1 + self.A[2,1]*x2))/self.A[2,2]           # Atualiza c e usa Xi anterior
            if((abs(x1-a) < err) and (abs(x2-b))<err and (abs(x3-c))<err):
                break
            x1,x2,x3 = a,b,c
            print('%2.d \t%.3f \t%.3f \t%.3f\n'%(k,x1,x2,x3))
    
# =============================================================================    
     
    def met_gauss(self):                  
        a,b,c,err = 0, 0, 0, 0.001
        x1,x2,x3 = 0, 0, 0
        print('\n***** Método Iterativo de Gauss-Seidal *****\n\n')
        print(' k \t  x1 \t  x2 \t  x3')
           
        for k in range(1,self.n):
            a,x1 = x1, (self.Y[0]-(self.A[0,1]*x2 + self.A[0,2]*x3))/self.A[0,0]           # Atualiza a e usa Xi anterior
            b,x2 = x2, (self.Y[1]-(self.A[1,0]*x1 + self.A[1,2]*x3))/self.A[1,1]           # Atualiza b e usa Xi anterior
            c,x3 = x3, (self.Y[2]-(self.A[2,0]*x1 + self.A[2,1]*x2))/self.A[2,2]           # Atualiza c e usa Xi anterior
            if((abs(x1-a) < err) and (abs(x2-b))<err and (abs(x3-c))<err):
                break
            print('%2.d \t%.3f \t%.3f \t%.3f\n'%(k,x1,x2,x3))
 
    
# =============================================================================
# Chamada do main    
# =============================================================================
def escopo():
       
    A=np.array([[10,2,1],[1,5,1],[2,3,10]])
    Y=np.array([7,-8,6])   
    n=20
         
    sel = MetIter(A,Y,n)
    sel.met_jacobi()
    sel.met_gauss()

if __name__ == "__main__":
    escopo()
 