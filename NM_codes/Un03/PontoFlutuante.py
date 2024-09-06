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
    
    3. **Mantissa/Fração (23 bits):** Representa a parte fracionária do número. 
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
        parte_fracionaria_bin = ''                    # Define um string vazia
        
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
                
#%%    ÁREA DE TESTES
num=81
a,b,c = Num2ieee.int_frac(num)
print('Estrutra: \t\ sinal | expoente | mantissa  ')
print('Precisão de 32 bits:',Num2ieee.NumRes32bits(a,b,c))
# print('Precisão de 64 bits:',Num2ieee.NumRes64bits(a,b,c))
    