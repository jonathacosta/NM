#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mon Apr 19 11:21:18 2021
@author: Jonatha Rodrigues da Costa

Sistemas de numeração e conversão de uma base (2 <= base <= 16)qualquer 
para decimal.

"""
#%% Função
# =============================================================================

def base2decimal(numero_str, base):
    '''
    Função para converter um número de qualquer base (2 a 16) para decimal
    '''
    try:        
        dec=int(numero_str, base)
        print(f"Base {base}: {numero_str}")
        print(f"Decimal: {dec}")
        
        return dec
    except ValueError:
        return "Número ou base inválidos."
      
# =============================================================================
num = "FF"
base = 16
base2decimal(num,base)
