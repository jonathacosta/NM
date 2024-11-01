#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos Numéricos
Prof. Jonatha Costa

Ponto flutuante - representação IEEE 754

A IEEE 754 é uma norma amplamente utilizada para a representação de números 
em ponto flutuante em computadores. Foi criada pelo Institute of Electrical 
and Electronics Engineers (IEEE) e padroniza a forma como números reais 
(com parte fracionária) são armazenados e manipulados em sistemas de 
computação, facilitando a interoperabilidade entre diferentes plataformas.
----------------------------------------------------------------
Formato Básico (Precisão Simples - 32 bits):
----------------------------------------------------------------
    Um número em ponto flutuante conforme a norma IEEE 754 de precisão simples 
    é representado em 32 bits, divididos em três partes:

    1. Sinal (1 bit): Define se o número é positivo (0) ou negativo (1).
    
    2. Expoente (8 bits): Usado para determinar a faixa de valores 
    (magnitude) do número. O expoente é armazenado com um "bias" (127 no 
     caso de precisão simples), o que significa que o valor armazenado no c
    ampo de expoente é deslocado em relação ao valor real.
    
    3. Mantissa/Fração (23 bits): Representa a parte fracionária do número. 
    A mantissa é normalizada, o que significa que o bit mais significativo é 
    sempre 1 e, portanto, não precisa ser armazenado explicitamente (isso é
    conhecido como bit implícito).
----------------------------------------------------------------
    - Fórmula de Conversão:
        Um número em ponto flutuante IEEE 754 pode ser descrito pela fórmula:
        
        Número = (-1)^(sinal) x 1.{mantissa} x 2^(expoente -bias)

    - Exemplo:
        No caso de precisão simples (32 bits):
        - Um número positivo `3.14` seria representado em binário, 
        com `sinal = 0`, `expoente = 128` (ou 10000000 em binário), 
        e uma mantissa correspondente a `1.10010001111010111000011`.

     Vantagens:
        - Ampla Faixa de Representação - A IEEE 754 permite representar 
        números muito grandes ou muito pequenos, com precisão ajustável.
        - Padronização - Garante que diferentes computadores, sistemas 
        operacionais e linguagens de programação tratem números de maneira consistente.

         Porém, devido à natureza da representação em ponto flutuante, 
         alguns números decimais não podem ser representados com exatidão, 
         resultando em pequenos erros de arredondamento em cálculos.
         Isso implica o estudo de erro de truncamento, arredondamento, erros
         residuais, erro relativo e erro total em operações de cálculo numérico.

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
        parte_fracionaria_bin =''
        
        if parte_fracionaria != 0:
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
if __name__ == "__main__":
    Num2ieee(81.5)    
