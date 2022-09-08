from py21_operations.sum_func import summation as summ
from py21_operations.sub_func import subtraction as sub


#Modules
"""
The module is a simple Python file that contains collections of functions 
and global variables and with having a .py extension file.

ex : sum_func.py , sub_func.py are modules
"""

#Package
"""
The package is a simple directory having collections of modules. 
This directory contains Python modules and also having __init__.py

ex : py21_operations is a package
"""

#Library 
"""
A library is a collection of packages.
The library is having a collection of related functionality of codes that allows 
you to perform many tasks without writing your code.

ex: pandas[dataframe operations] , numpy[Mathematical operations] 
"""


var_a = int(float(input('please enter "a" value')))
var_b = int(float(input('please enter "b" value')))

summ(var_a,var_b)

sub(var_a,var_b)
