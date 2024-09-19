#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Interpolação de Newton
Prof. Jonatha Costa

Conceito basilares:
    O polinômio interpolador de Newton é construído usando uma fórmula baseada
    em diferenças divididas. O grau do polinômio é diretamente relacionado ao 
    número de pontos usados para a interpolação:
        
    Número de Pontos n: Se você tem n pontos de interpolação, o polinômio 
    interpolador de Newton terá exatamente o grau n−1.
    
Fórmula do Polinômio Interpolador:
    O polinômio de Newton é construído usando diferenças divididas, e a forma 
    geral do polinômio é:
        
        P(x)=a0+a1(x−x0)+a2(x−x0)(x−x1)+…+an−1(x−x0)(x−x1)⋯(x−xn−2)
        
        Aqui, cada ai é um coeficiente obtido das diferenças divididas, 
        e o grau do polinômio é o máximo grau dos termos 
        (x−x0)(x−x1)⋯(x−xi−1)(x−x0​)(x−x1​)⋯(x−xi−1​)

Vantagens e Desvantagens:
    - Vantagens
    Atualização Fácil: Pode adicionar novos pontos sem recalcular todo o 
    polinômio do início.
    Avaliação Eficiente: A forma de Horner permite uma avaliação rápida do polinômio.
    Flexível: Permite modificar o polinômio de forma incremental. 

    -Desvantagens
    Instabilidade Numérica: Pode oscilar e ter erros significativos para muitos
    pontos.
    Coeficientes Complexos: Cálculo das diferenças divididas pode ser complicado 
    e propenso a erros.
    Grau Alto: Polinômios de alta ordem podem ser imprecisos e complexos de 
    avaliar.
    Aproximação Limitada: Pode não se ajustar bem a funções complexas com poucos 
    pontos.

"""
# =============================================================================
import numpy as np
def PolInterNewton(x,y,p):
    '''
    Exibe o resultado objetivo da interpolação de Newton para um valor 'p' 
    num pares de vetores X,Y.
    '''
    a,s= [y[0]],y                                # s é vetor das divisoes
    for i in range(len(x)-1):
        y=s                                      # Atualiza o vetor y
        s=(y[1:]-y[:-1])/(x[(1+i):]-x[:-(1+i)])  # Reduz o vetor x
        a.append(s[0])    
    xn,Yint=1,a[0]
    for k in range(1,len(x)):
        xn=xn*(p - x[k-1])
        Yint=Yint+a[k]*xn
    
    return Yint

def GerPolIntNewton(x,y):
    '''
    Exibe o polinômio Interpolador de Newton a partir na dimensão do vetor
    de entrada x espaçado num espaço linear de 100 unidades.
    '''
    import sympy as sp
    p = sp.symbols('x')    
    a,s= [y[0]],y                                # s é vetor das divisoes
    for i in range(len(x)-1):
        y=s                                      # Atualiza o vetor y
        s=(y[1:]-y[:-1])/(x[(1+i):]-x[:-(1+i)])  # Reduz o vetor x
        a.append(s[0])    
    xn,Yint=1,a[0]
    for k in range(1,len(x)):
        xn=xn*(p - x[k-1])
        Yint=Yint+a[k]*xn
    # Simplifica o polinômio
    P = sp.simplify(Yint)
    print(f"Polinômio interpolador: {P}")

def GraphPolIntNewton(x,y):
    '''
    Percepção gráfica para um espaço linear a partir do vetor de entrada x.
    Note que o grau do polinomio muda em função dos pontos do espaço linear
    
    O resultado gráfico é gerado a partir de um novo vetor x linearmente espa-
    çado em 100 partes. O grau o polinômio passa a ser função da quantidade de pontos do 
    vetor de entrada x.
    '''    
    import matplotlib.pyplot as plt
    # Plotando os pontos e o polinômio interpolador
    x_values = np.linspace(min(x), max(x), 100)
    y_values = [PolInterNewton(x, y, i) for i in x_values]    
    plt.plot(x_values, y_values, label='Polinômio Interpolador')
    plt.scatter(x, y, color='red', label='Pontos Dados')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.legend()
    plt.title('Interpolação de Newton')
    plt.grid(True)
    plt.show()
    
#%%
if __name__=="__main__":    
    # Ponto de interpolação e vetores de entrada x,y
    p=3; 
    x=np.array([1,2,4,5,7,8]); y=np.array([52,5,-5,-40,10,5])    
    # Resultado da interpolação do ponto 'p'
    Yint= PolInterNewton(x,y,p)
    print('\nA aproximação encontrada para f(%.2f) = %.2f'%(p,Yint))   
    # Percepção do grau do polinômio
    GerPolIntNewton(x,y)
    # Percepção gráfica 
    GraphPolIntNewton(x, y)  
