# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:44:40 2017

@author: franco
"""

#probando la libreria que cree
import ctypes as C 
math = C.CDLL('./libdinamic.so')

b = math.add_float(C.c_float(5.3),C.c_float(6.4))

print b 
