from sympy import sympify, solve, Symbol, pprint

from string import ascii_lowercase

sym1=ascii_lowercase.replace('','')
sym2=sym1.split()

sym2=Symbol('sym1')

def ecuacion():
    ecuacion = (input('Introduzca la ecuacion: '))
    for i in ecuacion:
        if i in sym2:
            i=Symbol(i)
    ecuacion.replace('','*')
    ecuacion.replace('**','^')
    return sympify(ecuacion)

print(ecuacion())