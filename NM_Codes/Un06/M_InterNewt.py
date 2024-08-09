#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Interpolação de Newton'
Prof. Jonatha Costa
"""
# =============================================================================
import numpy as np
x=np.array([1,2,4,5,7])
y=np.array([52,5,-5,-40,10])
print('\014')
xint=3
a,s= [y[0]],y                                # s é vetor das divisoes
for i in range(len(x)-1):
    y=s                                      # Atualiza o vetor y
    s=(y[1:]-y[:-1])/(x[(1+i):]-x[:-(1+i)])  # Reduz o vetor x
    a.append(s[0])    
xn,Yint=1,a[0]
for k in range(1,len(x)):
    xn=xn*(xint - x[k-1])
    Yint=Yint+a[k]*xn
print('\nA aproximação encontrada para f(%.1f) = %.2f'%(xint,Yint))

#%%
'''
>> Raciocínio de construção de solução

#yint= (vetor de div).T * (vec de coef.)
#
#a[0]=y[0]
#s=(y[1:]-y[:-1])/(x[1:]-x[:-1])
#a[1]=s[0]
#
#y=s
#s=(y[1:]-y[:-1])/(x[2:]-x[:-2])
#a[2]=s[0]
#
#y=s
#s=(y[1:]-y[:-1])/(x[3:]-x[:-3])
#a[3]=s[0]
#
#
#y=s
#s=(y[1:]-y[:-1])/(x[4:]-x[:-4])
#a[4]=s[0]
#a=np.zeros(len(x))

#y=s
    #s=(y[1:]-y[:-1])/(x[4:]-x[:-4])
#a[4]=s[0]
    
#Código alternativo   


#
#quant_pontos=int(input('Quantidade de pontos:'))
#pontos,f_pontos=[],[]
#tabela=[]
#for i in range(quant_pontos):
#    ponto=float(input("x%d="%i))
#    f_ponto=float(input("f(x%d)="%i))
#    pontos.append(ponto)
#    f_pontos.append(f_ponto)
#tabela.append(f_pontos)
#print(tabela)
#
#x=float(input("Ponto x a ser estimado:"))
#print()   
#passo=1
#for n in range(quant_pontos-1):
#    ordem=[]
#    for m in range(len(tabela[n])-1):
#        dif_dividida=(tabela[n][m+1]-tabela[n][m])/(pontos[m+passo]-pontos[m])
#        ordem.append(dif_dividida)
#    tabela.append(ordem)
#    passo+=1
#for k in range(len(tabela)):
#      print("Ordem %d:"%k,tabela[k])
#print()
#
#aprox=0
#grau=0
#for i in range(len(tabela)):
#    fator=tabela[i][0]
#    for j in range(grau):
#        fator*=(x-pontos[j])
#    grau+=1
#    aprox+=fator
#print('A aproximação encontrada para f(%f)=%f'%(x,aprox))
#      
    
'''
