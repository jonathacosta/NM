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

def pol(p,digitos_coef):
        s=''
        import sympy as sym
        x=sym.Symbol('x')
        for i in range(len(p)):          
            if p[i]==p[-1]:
                px=str(round(p[i],digitos_coef))
            else:
                if p[i]==1.:
                    px=str(x**(len(p)-1-i))              
                else:    
                    px=str(round(p[i],digitos_coef)*x**(len(p)-1-i))                                 
            if i==0:
                s=s + px    
            elif p[i]>0:
                s=s+' + '+px
            else:
                s=s +' '+ px    
        return sym.Symbol(s)

if __name__== "__main__":
    p=[3.141517,2.345345,-3.3454,3.141517,2.345345,-3.3454]
    digitos_coef=3;
    print(pol(p,digitos_coef))
    
