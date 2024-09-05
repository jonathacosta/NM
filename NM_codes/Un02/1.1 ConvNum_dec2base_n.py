#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mon Apr 19 11:21:18 2021
@author: Jonatha Rodrigues da Costa

Sistemas de numeração e conversão de decimal
para um base qualquer de 2 a 16.

"""
#%% Função
def decimal2base(numero, base):
    '''
    Função para converter um número decimal para qualquer base de 2 a 16
    '''
    
    
    if base < 2 or base > 16:
        return "Base inválida. Escolha uma base entre 2 e 16."
    
    digitos = "0123456789ABCDEF"
    resultado = ""
    
    while numero > 0:
        resto = numero % base
        resultado = digitos[resto] + resultado
        numero //= base    # // divisão inteira
    
    return resultado 
# =============================================================================
numero,base = 32,2

print(f"Decimal: {numero}")
print(f"Base {base}: {decimal2base(numero, base)}")
