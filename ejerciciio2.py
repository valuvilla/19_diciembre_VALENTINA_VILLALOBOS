from sympy import sympify, solve, Symbol, pprint

from string import ascii_lowercase

sym1=ascii_lowercase.replace('','')
sym2=sym1.split()

sym2=Symbol('sym1')

def ecuacion():
    ecuacion = int(input('Introduzca la ecuacion: '))
    ecuacion.replace('','*')
    return sympify(ecuacion)

print(ecuacion())