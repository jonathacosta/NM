#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Ponto flutuante

Versão 01 - Utilizando comandos geminados e string em lugar de lista.
Código converte um valor decimal para binário no formato de precisão simples pela IEEE 754/2008
Sintaxe:
'sinal + (exponte com bias) + mantissa'
"""

decimal = float(input('Informe um valor em decimal:'))

#********************************************
# 1.0 Verifica o sinal do número
#********************************************
if decimal < 0:
    sinal_bit = '1'
    decimal = -decimal
else:
    sinal_bit = '0'
    
#********************************************
# 2.0 Separa a parte inteira e a parte decimal
#********************************************
parte_inteira = int(decimal)
parte_fracionaria = decimal - parte_inteira

# 2.1 Converte a parte inteira para binário
#********************************************
parte_inteira_bin = bin(parte_inteira)[2:]       # Utilizando [2:] para suprimir o 0b da string.

# 2.2 Converte a parte fracionária para binário
#********************************************
mantissa_bin = ''                # Define um string vazia
if parte_fracionaria != 0:    
    while parte_fracionaria > 0:
        parte_fracionaria *= 2                # Multiplica o valor por 2
        bit = int(parte_fracionaria)          # Guarda o valor da parte inteira em bit 
        mantissa_bin += str(bit)              # Armazena bit como string na string 
        parte_fracionaria -= bit              # Remove a parte inteira

#********************************************
# 32 bits - Calcula o expoente e a fração precisão simples
#********************************************
bias_s = 127
exponente_s = format(len(parte_inteira_bin) -1 + bias_s,'08b') # Utilizar -1 para reduzir o expoente de 1 unidade      
mantissa_s = (parte_inteira_bin[1:] + mantissa_bin).ljust(23, '0') 
ieee754_bin_s = sinal_bit +'|'+ exponente_s + '|'+ mantissa_s      # Formata o resultado conforme IEEE754

#********************************************
# 64bits - Calcula o expoente e a fração precisão dupla
#********************************************
bias_d = 1023
exponente_d = format(len(parte_inteira_bin) - 1 + bias_d,'011b')
mantissa_d = (parte_inteira_bin[1:] + mantissa_bin).ljust(52, '0')  
ieee754_bin_d = sinal_bit +'|'+ exponente_d + '|'+ mantissa_d    

#********************************************
# Resultados
#********************************************
print("Valor decimal informado:", decimal)
print("Representação IEEE754 com precisão simples (32 bits):", ieee754_bin_s)
print("Representação IEEE754 com precisão dupla (64 bits):", ieee754_bin_d)