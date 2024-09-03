#!/usr/bin/env python
# coding: utf-8
""" Métodos Numéricos - Unidade 06: Ajuste de curvas </font>

# ## Objeto:
# 
# * Apresentar conteúdo de Ajuste de Curvas
#     * Interpolação e extrapolação
#     * Regressão Linear por Mínimos Quadrados
#     * Linearização de Equações não lineares
#     * Polinômio de Lagrange e de Newton
#     * Spline Linear, quadrática e cúbica

# # Estrutura de classe
# ## Interpoladores
"""
# =============================================================================

# import warnings
# warnings.filterwarnings("ignore")

import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Interporladores():
    def __init__(self,x,y,p,m=3):
        self.x = x
        self.y = y
        self.p = p
        self.m = m
               
    def interLagrange(self):
        try:
            k=np.ones(len(self.x))                          
            for i in range(len(self.x)):
                for j in range(len(self.x)):
                    if (i!=j):          
                        k[i]=k[i]*(self.p-self.x[j])/(self.x[i]-self.x[j])    
            yint=sum(self.y*k)
            #print('\nInterpolação de Lagrange: A aproximação encontrada para f(%.1f) = %.2f'%(self.p,yint))
            return yint
        except:
            return '-'
           
    def newton(self):
        try:
            a,s = [self.y[0]], self.y                                # s é vetor das divisoes
            for i in range(len(self.x)-1):
                y=s                                                  # Atualiza o vetor y
                s=(y[1:] - y[:-1])/(self.x[(1+i):] - self.x[:-(1+i)])          # Reduz o vetor x
                a.append(s[0])    
            xn,Yint = 1,a[0]
            for k in range(1,len(self.x)):
                xn = xn*(self.p - self.x[k-1])
                yint = Yint+a[k]*xn
            #print('\nInterpolação de Newton: A aproximação encontrada para f(%.1f) = %.2f'%(self.p,yint))
            return yint
        except :
            return '-'


# Regressores    
class Regressores(Interporladores):
    def __init__(self,x,y,p,m):
         Interporladores.__init__(self,x,y,p,m)
                  
    def reglin(self):
        try:

            if (len(self.x)!=len(self.y)):
                print('Falha! X e Y tem dimensões diferentes!') 

            else:
                n = len(self.x)
                Sx ,Sy  = sum(self.x)   , sum(self.y)
                Sxy,Sxx = sum(self.x*self.y) , sum(self.x**2)
                a1 = (n*Sxy-Sx*Sy)/(n*Sxx-Sx**2)
                a0 = (Sxx*Sy-Sxy*Sx)/(n*Sxx-Sx**2)
            coef = [a1,a0]
            """
            ATENÇÃO: 
            O comando p = np.polyfit(x,y,1) retorna os coeficientes de 'p', acima como as linhas acima.
            Na prática, pode ser utilizada uma ou outra métrica! 

            """
            #y2=np.polyval(coef,self.x)   # O comando aplica os valores de 'x' no polinômio 'p' e retorna a imagem.

            m = sym.Symbol('m')
            P = round(coef[0],4)*m + round(coef[1],4)

            print(f'O polinômio correspondente por Regressão Linear é: {P}')            
            # print('\nA aproximação encontrada para f(%.1f) = %.2f'%(self.p , np.polyval(coef,self.p)))
            yint = np.polyval(coef,self.p)
            return yint
        
        except:
            return '-'

    def pol(self,p):
        s=''
        import sympy as sym
        x=sym.Symbol('x')
        for i in range(len(p)):          
            if p[i]==p[-1]:
                px=str(p[i])
            else:
                if p[i]==1.:
                    px=str(x**(len(p)-1-i))              
                else:    
                    px=str(p[i]*x**(len(p)-1-i))                                 
            if i==0:
                s=s + px    
            elif p[i]>0:
                s=s+' + '+px
            else:
                s=s +' '+ px    
        return sym.Symbol(s)

      
    def regpol(self):
        """
        Regressão polinomial utilizando funções polyfit e polyval
        """
        try:
            c = np.polyfit(self.x,self.y,self.m)               # Coef. de p(x) proposto   
            #v = np.polyval(c,self.x)                           # Imagem do novo domínio
            sol = self.pol(c)       
            yint = np.polyval(c,self.p)   
            print('Polinômio via Regressão Polinomial é : \n',sol)
            print()
            return yint
        
        except:     
            return '-'

# ## Ajuste por splines

class SPline(Regressores):    
    def __init__(self,x,y,p,m):
        Regressores.__init__(self,x,y,p,m)
                
    def spl_linear(self):
        try:
            # Busca do intervalo que contem o ponto 'p'
            for i in range(len(self.x)):
                if self.p < self.x[i+1]:
                    i+=1
                    break 

            # Calcula a interpolação no intervalo            
            yint=(self.p - self.x[i])* self.y[i-1]/ (self.x[i-1] - self.x[i]) + (self.p - self.x[i-1])*self.y[i]/(self.x[i]-self.x[i-1]) 
            #print('\nA aproximação encontrada para f(%.1f) = %.2f'%(self.p,yint))

            return yint
        except:
            return '-'
    def spl_quad(self):
        try:
            n=len(self.x)
            for i in range(len(self.x)):
                if self.p < self.x[i+1]:
                    i+=1
                    break

            intervalo = i+2*(i-1)      # Posiciona os 3 coeficientes no intervalo
            #pos = i
            eq0 = 2*(n-1)          # Quant. spline por intervalo 
            eq1 =  n-2             # Quant. de nós
            eq = eq0+eq1           # Total de equações         
            #**************************************%***************************************
            A=np.arange(eq*(eq+1)).reshape(eq,eq+1)   # Coluna adicional
            d,k,A[:] = 0,0,0

            for b in range(int(eq0/2)):           # bloco   
                for i in range(2):                # linha
                    for j in range(3):            # coluna
                        A[i+k,j+d]=self.x[i+b]**abs(j-2)
                d+= 3
                k+= 2      
            m,d = 1,0

            for k in range(eq0,eq):              # linha/bloco
                for j in range(2):               # coluna
                    A[k,j+d] = (2*self.x[m])**abs(j-1)
                    A[k,j+d+3] = -A[k,j+d]
                m+=1
                d+=3
            A = A[: , 1:]                          # Exclui a coluna extra

            B=[]                                   #Matriz B
            for i in range(n):
                for j in range(2):
                    B.append(self.y[i])
            del(B[0])
            del(B[-1])
            for j in range(eq1):
                B.append(0)
            B = np.array(B)

            coef=list(np.linalg.inv(A)@B.T) # ou coef=list(np.linalg.solve(A,B))
            coef.insert(0,0)

            j = intervalo-1
            yint = coef[j]*self.p**2 + coef[j+1]*self.p + coef[j+2]

            #print("\nMétodo Interpolação Quadrática resulta em\nf(%.2f) = %.2f \n\n"%(self.p,yint))

            return yint
        except:
            return '-'
       

## RNA
from sklearn.linear_model import LinearRegression

class Network(SPline):
    def __init__(self,x,y,p,m):
        SPline.__init__(self,x,y,p,m)
        
   
    def sk_reglin(self):
        try:
            modelo = LinearRegression()

            X = self.x
            X = X.reshape(len(self.x),1)   # Input de x deve ser 2D
            Y = self.y
            modelo.fit(X, Y)
            sol = modelo.predict([   [self.p]   ])

            #print('Coeficiente Regressão Linear - sklearn: ', modelo.coef_)                      # Coeficientes
            #print("MSE: %.2f" % np.mean((modelo.predict(X) - Y) ** 2))  # MSE (mean square error)
            #print('Score de variação: %.2f' % modelo.score(X, Y))       # Score de variação: 1 representa predição perfeita

            return (round(float(sol),2))
        except:
            return '-'


## Resumo

class Resultados(Network):
    def __init__(self,x,y,p,m):
        self.fun = ['Inter_Larange','Inter_Newton','Reg_Linear','Reg_Polinomial','SP_Linear','SP_Quadratica', 'Reglin_SK'] 
        Network.__init__(self,x,y,p,m)
        
    def compare(self):
        lista = [self.interLagrange() , self.newton(), self.reglin(), self.regpol(), self.spl_linear(),self.spl_quad(), self.sk_reglin()]
        df = pd.DataFrame()
        df['Métodos'] = self.fun
        df['Resultados'] = lista
        print()
        print(df)
        return lista
        
    
    def graf(self,lista):
        plt.figure(figsize=(15,8))
        plt.plot(self.x,self.y,'*b',label = 'Dados de medições')
        for i,j in enumerate(lista):
            plt.plot(self.p,j,'o',label = f'{self.fun[i]}')
            plt.legend()            
            plt.title('Interpolação métodos variados')


## Escopo de chamadas dos métodos

if __name__ == "__main__":
   
    x=np.arange(0,110,10)
    y=np.array([ 0.94, 0.96, 1.0, 1.05, 1.07, 1.09, 1.14, 1.17, 1.21, 1.24, 1.28])       
    m = 3   # Grau do polinomio  
 
    #p = float(input(f'\nInforme um ponto a interpolar no intervalo de x ({min(x)} e {max(x)}) ou <enter> para encerrar: '))  
    p = 12.7
    if p <= min(x) or p >= max(x):
        print('Alerta!\nValor de entrada fora do domínio de X.')
    curvas = Resultados(x,y,p,m)
    lista = curvas.compare()
    curvas.graf(lista)
  
