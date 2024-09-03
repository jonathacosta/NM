#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Ponto flutuante

Versão 00 - Utilizando passo-a-passo de deslocamento de vírgula e lista para mantissa
Código converte um valor decimal para binário no formato de precisão simples pela IEEE 754/2008
Sintaxe:
'sinal + (exponte com bias) + mantissa'


comando:
    * format(valor_decimal,'valor de preenchimento a esquerda + comprimento da string + base do sistema')
    * ljust() preenche os espaços a direita da string com (comprimento de 23, valor=0)
    * ''.join([str(i) for i in mantissa_bin] converte os elementos da lista 'mantissa_bin' para uma só string
"""

decimal = 81
#********************************************
# 1.0 Verifica o sinal do número
#********************************************
sinal_bit = '0'
if decimal < 0: sinal_bit = '1'
    
#********************************************
# 2.0 Separa a parte inteira e a parte decimal
#********************************************
parte_inteira = int(decimal)
parte_fracionaria = decimal - parte_inteira

# 2.1 Converte a parte inteira para binário
#********************************************
parte_inteira_bin = bin(parte_inteira)[2:]               # Utilizando [2:] para suprimir o 0b da string.
desloc_virgula = len(parte_inteira_bin) - 1              # Deslocamentos da virgula
num_antes_virgula = parte_inteira_bin[:-desloc_virgula]                # 10000101 -> '1','0000101'
num_depois_virgula = parte_inteira_bin[:desloc_virgula]

# 2.1 Converte a parte fracionária para binário
#********************************************
mantissa_bin = []                                        # Define uma lista vazia
if parte_fracionaria != 0:    
    while parte_fracionaria > 0:
        parte_fracionaria *= 2                           # Multiplica o valor por 2
        bit = int(parte_fracionaria)                     # Guarda o valor da parte inteira em bit 
        parte_fracionaria -= bit   
        mantissa_bin.append(bit)                         # Armazena bit como string na string                 
mantissa_bin = ''.join([str(i) for i in mantissa_bin])   # Converte a lista numa única string

# 32 bits - Calcula o expoente e a fração precisão simples
#********************************************
bias_s = 127
exponente_s = format(desloc_virgula + bias_s,'08b')        # Utilizar -1 para reduzir o expoente de 1 unidade      
mantissa_s = (num_antes_virgula + mantissa_bin).ljust(23, '0') 
ieee754_bin_s = sinal_bit +'|'+ exponente_s + '|'+ mantissa_s      # Formata o resultado conforme IEEE7
ieee754_bin_s

# 64 bits - Calcula o expoente e a fração precisão simples
#********************************************
bias_s = 1023
exponente_d = format(desloc_virgula + bias_s,'011b')        # Utilizar -1 para reduzir o expoente de 1 unidade      
mantissa_d = (num_antes_virgula + mantissa_bin).ljust(52, '0') 
ieee754_bin_d = sinal_bit +'|'+ exponente_d + '|'+ mantissa_d      # Formata o resultado conforme IEEE7

# Resultados
#********************************************
print("Valor decimal informado:", decimal)
print("Representação IEEE754 com precisão simples (32 bits):\n", ieee754_bin_s)
print("Representação IEEE754 com precisão dupla (64 bits):\n", ieee754_bin_d)
