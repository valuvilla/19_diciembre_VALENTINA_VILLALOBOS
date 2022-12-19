from ast import main
from sympy import sympify, solve, Symbol, pprint

from string import ascii_lowercase

sym1=ascii_lowercase.replace('','')
sym2=sym1.split()

sym2=Symbol('sym1')

def ecuacion():
    ecuacion = (input('Introduzca la ecuacion: '))
    ecuacion.split()
    for i in ecuacion:
        if i in ascii_lowercase:
            i=Symbol(i)
    ecuacion.replace('','*')
    ecuacion.replace('**','^')
    return sympify(ecuacion)

#probamos el codigo
# print(ecuacion())


def symplify():
    ecuacion = (input('Introduzca la ecuacion: '))
    sympify(ecuacion)

#probamos el codigo
print(symplify())

if __name__=='__main__':
   main()


