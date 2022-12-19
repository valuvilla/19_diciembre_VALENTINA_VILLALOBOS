from ast import main
from string import ascii_lowercase
from sympy import Symbol, sympify, solve, pprint


sym1=ascii_lowercase.replace('','')
sym2=sym1.split()

sym2=Symbol('sym1')


def do_math(n):
    #ordenar alfabeticamente una lista
    
    
    for i in n:
        if i in ascii_lowercase:
            n.pop(i)

        print(n)
       
        
do_math(n=input('Ingrese la ecuacion: '))

if __name__=='__main__':
   main()