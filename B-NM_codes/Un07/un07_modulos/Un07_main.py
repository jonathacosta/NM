#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações lineares
Métodos iterativos
Prof. Jonatha Costa
"""

from Metodo_Interat import MetIter
import numpy as np
# =============================================================================
# Intervalor de analise 
# =============================================================================

# A=np.array([[10,2,1],[1,5,1],[2,3,10]])
# Y=np.array([7,-8,6])   



A = np.array([[4, 1],
              [2, 3]])

Y = np.array([1, 5])

n=20
     
sel = MetIter(A,Y,n)
sel.met_jacobi()
sel.met_gauss()