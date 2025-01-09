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
        
        '''             
        Método separa as partes inteiras e fracionárias do número e
        retorna as partes em binário.
        '''
        parte_inteira = int(self.num)
        parte_fracionaria = self.num - parte_inteira                     
        parte_inteira_bin = bin(parte_inteira)[2:] 
        parte_fracionaria_bin =''
        
        if parte_fracionaria != 0:
            while parte_fracionaria > 0 and len(parte_fracionaria_bin) < 52:
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
               
if __name__ == "__main__":
    print("jrc")
    Num2ieee(0.1)      
        
#%%
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conversor de número decimal para IEEE 754
"""

class Num2IEEE:
    """
    Classe para converter números decimais para formato IEEE 754 (32 e 64 bits).
    """

    def __init__(self, num):
        self.num = float(num)  # Garantir que o número seja um float
        self.bit_sinal = '1' if self.num < 0 else '0'
        self.num = abs(self.num)

        self.parte_inteira, self.parte_fracionaria = self._separar_partes()
        self.parte_inteira_bin, self.parte_fracionaria_bin = self._converter_para_binario()
        self.num_normalizado, self.expoente = self._normalizar_numero()

        self.ieee754_32bits = self._calcular_ieee754(32)
        self.ieee754_64bits = self._calcular_ieee754(64)

        print(f"Precisão de 32 bits: {self.ieee754_32bits}")
        print(f"Precisão de 64 bits: {self.ieee754_64bits}")

    def _separar_partes(self):
        """Separa o número em parte inteira e fracionária."""
        parte_inteira = int(self.num)
        parte_fracionaria = self.num - parte_inteira
        return parte_inteira, parte_fracionaria

    def _converter_para_binario(self):
        """Converte a parte inteira e fracionária para binário."""
        parte_inteira_bin = bin(self.parte_inteira)[2:] if self.parte_inteira != 0 else '0'
        parte_fracionaria_bin = ''

        fracao = self.parte_fracionaria
        while fracao > 0 and len(parte_fracionaria_bin) < 52:  # Limitar a 52 bits para precisão dupla
            fracao *= 2
            bit = int(fracao)
            parte_fracionaria_bin += str(bit)
            fracao -= bit

        return parte_inteira_bin, parte_fracionaria_bin

    def _normalizar_numero(self):
        """Normaliza o número em formato 1.x * 2^exp."""
        if self.parte_inteira_bin != '0':
            shift = len(self.parte_inteira_bin) - 1
            num_normalizado = self.parte_inteira_bin + self.parte_fracionaria_bin
            print(shift)
            print(self.parte_inteira_bin)
            print(self.parte_fracionaria_bin)
            print(num_normalizado)
            
        else:
            # Corrigir caso em que parte_fracionaria_bin é vazia
            if not self.parte_fracionaria_bin:
                raise ValueError("Não é possível normalizar um número com parte fracionária zero.")
            shift = -self.parte_fracionaria_bin.find('1') - 1
            num_normalizado = self.parte_fracionaria_bin.lstrip('0')

        return num_normalizado, shift

    def _calcular_ieee754(self, bits):
        """Calcula a representação IEEE 754 para o número."""
        if bits == 32:
            bias = 127
            mantissa_bits = 23
            expoente_bits = 8
        elif bits == 64:
            bias = 1023
            mantissa_bits = 52
            expoente_bits = 11
        else:
                raise ValueError("O formato deve ser de 32 ou 64 bits.")

        expoente = format(self.expoente + bias, f'0{expoente_bits}b')
        mantissa = self.num_normalizado[1:1 + mantissa_bits].ljust(mantissa_bits, '0')

        return f"{self.bit_sinal}|{expoente}|{mantissa}"


# Teste
if __name__ == "__main__":
    print("chat")
    # print('Numero: 502.619831')
    # Num2IEEE(501.64654)
    print("Numero 0.1")
    Num2IEEE(0.1)
     
    
    
