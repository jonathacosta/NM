#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos
Diferenciação via exercícios 01
Prof. Jonatha Costa
"""
import matplotlib.pyplot as plt
print('\14')
# =============================================================================
# Dados de entrada
# =============================================================================
def deriv(x,y):
    dx=[]
    dx.append((y[1]-y[0])/(x[1]-x[0]))
    for i in range(1,len(x)-1):                 # dif. central
        dx.append( (y[i+1] - y[i-1])/(x[i+1]-x[i-1] ) )
    dx.append( (y[-1]-y[-2])/(x[-1]-x[-2]) )
    return dx

if __name__ ==  "__main__":

    p=0.2
    t=[4. , 4.2, 4.4, 4.6, 4.8, 5. , 5.2, 5.4, 5.6, 5.8, 6. , 6.2, 6.4,
       6.6, 6.8, 7. , 7.2, 7.4, 7.6, 7.8, 8.] 
    x=[-5.87,-4.23,-2.55,-0.89,0.67,2.09,3.31,4.31,5.06,5.55,5.78,5.77,
       5.52,5.08,4.46,3.72,2.88,2.00,1.10,0.23,-0.59]
    vel=deriv(t,x)
    acc=deriv(t,vel)
    
    fig,(ax1,ax2,ax3)=plt.subplots(3)            # Atenção, subplots no plural
    ax1.set_title('Deslocamento')
    ax1.plot(t,x,'ro')
    ax1.grid()
    
    ax2.set_title('Velocidade')
    ax2.plot(t,vel,'b--')
    ax2.grid()
    
    ax3.set_title('Aceleração')
    ax3.plot(t,acc,'go')
    ax3.grid()
    
    for j in [5.,6.]:
        i=t.index(j)
        print(f'A velocidade para t={j} é : {round(vel[i],3)} cm/s')

