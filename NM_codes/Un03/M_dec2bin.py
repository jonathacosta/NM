#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Ponto flutuante
Prof. Jonatha Costa
"""

print('\14')
# =============================================================================
# Converter um número decimal para Ponto flutuante (PF) binário
# =============================================================================
def convbin(num):
    if num >1:
        convbin(num // 2)
    print(num %2,end='')
x=-1                    # declaração inicial para o laço
while(x<0):
    x=int(input('Informe um inteiro positivo no sistema decimal:'))
    
convbin(8)
print()
#%% =============================================================================
#  Função nativa
# =============================================================================
print(f'Utilizando a função nativa bin(x)\n{bin(x)}')