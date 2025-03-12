#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métodos numéricos: Solução de equações não lineares
Métodos diversos
Prof. Jonatha Costa
"""

from metodos import MetSol
import numpy as np
# =============================================================================
# Intervalor de analise 
# =============================================================================
a, b, imax = 2, 3, 30
Err, tol= 1e-3, 1e-3
f=lambda x: 8-4.5*(x - np.sin(x))

s=MetSol(a,b,imax,Err,tol,f)

s.bissec()
s.regfalsi()
s.sec()
s.newtonrapson()
