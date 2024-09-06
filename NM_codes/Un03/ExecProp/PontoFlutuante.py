#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classe base utilizada no exercício anterior
"""
class Num2ieee():
    '''
    Classe contém métodos conversores de um número decimal para o formato 
    IEEE 754/2008 com precisão de 32 e 64 bits.
    '''
    def sinal_bit(num):        
        sinal_bit = '0'
        if num < 0: sinal_bit = '1'
        
        return sinal_bit
    
    def int_frac(num):
        
        sinal = Num2ieee.sinal_bit(num)
        parte_inteira = int(num)
        parte_fracionaria = abs(num - parte_inteira)                     
        parte_inteira_bin = bin(parte_inteira)[2:]         
        parte_fracionaria_bin = ''
        
        if parte_fracionaria != 0:        
            while parte_fracionaria > 0:
                    parte_fracionaria *= 2                # Multiplica o valor por 2
                    bit = int(parte_fracionaria)          # Guarda o valor da parte inteira em bit 
                    parte_fracionaria_bin += str(bit)     # Armazena bit como string na string 
                    parte_fracionaria -= bit   

        return parte_inteira_bin, parte_fracionaria_bin, sinal

    def NumRes32bits(parte_inteira_bin, mantissa_bin, sinal_bit):        
        
        bias = 127
        exponente = format(len(parte_inteira_bin) -1 + bias,'08b') # Utilizar -1 para reduzir o expoente de 1 unidade      
        mantissa = (parte_inteira_bin[1:] + mantissa_bin).ljust(23, '0') 
        ieee754_bin = sinal_bit +'|'+ exponente + '|'+ mantissa      # Formata o resultado conforme IEEE754
        return ieee754_bin
    
    def NumRes64bits(parte_inteira_bin, mantissa_bin, sinal_bit):        
        bias = 1023
        exponente = format(len(parte_inteira_bin) -1 + bias,'011b') # Utilizar -1 para reduzir o expoente de 1 unidade      
        mantissa = (parte_inteira_bin[1:] + mantissa_bin).ljust(52, '0') 
        ieee754_bin = sinal_bit +'|'+ exponente + '|'+ mantissa      # Formata o resultado conforme IEEE754
        return ieee754_bin
                
