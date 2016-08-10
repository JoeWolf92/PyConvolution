from sympy import *
init_printing(use_unicode=False, wrap_line = False, no_global = True)
x = Symbol('x')
print(integrate(1/x,x))