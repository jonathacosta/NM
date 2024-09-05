#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mon Apr 19 11:21:18 2021
@author: Jonatha Rodrigues da Costa

Sistemas de numeração e conversão entre sistemas

"""
#%% Função
# =============================================================================
def Conv_num(num=81):
    '''
    Conversão de decimal para binario,octal e hexa 
    '''
    binario = bin(num)   # Binário
    octal = oct(num)     # Octal
    hexa = hex(num)      # Hexadecimal 
    print(f'O número {num} é {binario,octal,hexa}, respectivamente nas base 2,8 e 10.')

    return (binario,octal,hexa)

def conv_num2dec(binario,octal,hexa):   
    
    # Conversões para decimal
    dec_bin = int(binario, 2)   # Binário para decimal 
    dec_oct = int(octal, 8)     # Octal para decimal
    dec_hex = int(hexa, 16)     # Hexadecimal para decimal
    print()
    print(f"Binário {binario} para decimal: {dec_bin}")
    print(f"Octal {octal} para decimal: {dec_oct}")
    print(f"Hexadecimal {hexa} para decimal: {dec_hex}")
    if ((dec_bin == dec_oct) & (dec_oct == dec_hex)):
        return print('\nO número de entrada é {dec_bin}, base 10.')


#%% Chamada
#=============================================================================
num=42
binario,octal,hexa = Conv_num(num)
conv_num2dec(binario,octal,hexa)


