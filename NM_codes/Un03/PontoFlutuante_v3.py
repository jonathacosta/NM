#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Ajuste de curvas
Ponto flutuante

"""
class Num2ieee():
    '''
    Classe contém métodos conversores de um número decimal para o formato IEEE 754/2008 com precisão de 32 e 64 bits.
    '''
    def __init__(self,num):
        self.num = num
        self.bit_sinal = '1'if self.num < 0 else '0'
        self.int_frac()      
        self.NumRes32bits()
        self.NumRes64bits()
        
    def int_frac(self):
        parte_inteira = int(self.num)
        parte_fracionaria = self.num - parte_inteira                     
        parte_inteira_bin = bin(parte_inteira)[2:] 
        parte_fracionaria_bin ='0'
        
        if parte_fracionaria != 0:
            parte_fracionaria_bin = ''                            # Define um string vazia
            while parte_fracionaria > 0:
                    parte_fracionaria *= 2                # Multiplica o valor por 2
                    bit = int(parte_fracionaria)          # Guarda o valor da parte inteira em bit 
                    parte_fracionaria_bin += str(bit)     # Armazena bit como string na string 
                    parte_fracionaria -= bit   

        self.parte_inteira_bin = parte_inteira_bin
        self.parte_fracionaria_bin = parte_fracionaria_bin    
  
    def NumRes32bits(self):        
        bias = 127
        exponente = format(len(self.parte_inteira_bin) -1 + bias,'08b') # Utilizar -1 para reduzir o expoente de 1 unidade      
        mantissa = (self.parte_inteira_bin[1:] + self.parte_fracionaria_bin).ljust(23, '0') 
        ieee754_bin = self.bit_sinal +'|'+ exponente + '|'+ mantissa      # Formata o resultado conforme IEEE754
        self.ieee754_32bits = ieee754_bin
        print('Precisão de 32 bits:',ieee754_bin)
        
    def NumRes64bits(self):        
        bias = 1023
        exponente = format(len(self.parte_inteira_bin) -1 + bias,'011b') # Utilizar -1 para reduzir o expoente de 1 unidade      
        mantissa = (self.parte_inteira_bin[1:] + self.parte_fracionaria_bin).ljust(52, '0') 
        ieee754_bin = self.bit_sinal +'|'+ exponente + '|'+ mantissa      # Formata o resultado conforme IEEE754
        self.ieee754_64bits = ieee754_bin
        print('Precisão de 64 bits:',ieee754_bin)        
        
        
#%%
x=Num2ieee(81.5)    


"""

Aplicação proposta

1. Escreva os números a seguir nos seguintes formatos: (a) Formato binário; (b) Representação em ponto flutuante na base 2. (c) Cadeia de 32 bits em precisão simples conforme a norma IEEE–754.
    a. 81
    b. 66,25
    c. -0,625
    d. 0,533203125
    
2. Escreva os números a seguir nos seguintes formatos (a) Formato binário; (b) Representação em ponto flutuante na base 2. (c) Cadeia de 64 bits em precisão dupla conforme a norma IEEE–754.
    a. 256,1875
    b. –30952
    c. 0,33203125
    d. 0,001220703125



"""


    