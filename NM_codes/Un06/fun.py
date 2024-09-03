#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Thu May 20 15:09:14 2021
@author: Jonatha Rodrigues da Costa
"""
import sympy as sym
x=sym.Symbol('x')
# =============================================================================
# Substituir a função polyout do octave
# p(x)= x**2 + 2*x - 3 
# input = vetor numérico de coeficientes
# =============================================================================

def pol(p):
        s=''
        import sympy as sym
        x=sym.Symbol('x')
        for i in range(len(p)):          
            if p[i]==p[-1]:
                px=str(p[i])
            else:
                if p[i]==1.:
                    px=str(x**(len(p)-1-i))              
                else:    
                    px=str(p[i]*x**(len(p)-1-i))                                 
            if i==0:
                s=s + px    
            elif p[i]>0:
                s=s+' + '+px
            else:
                s=s +' '+ px    
        return sym.Symbol(s)


