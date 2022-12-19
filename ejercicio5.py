#https://github.com/valuvilla/19_diciembre_VALENTINA_VILLALOBOS.git


def hollow_triangle ( n ): # n es el numero de filas de la piramide
    for i in range(1,n+1):
        if i!=n and i!=1:
            print('_'*(n-i)+'#'+'_'*(2*(i-2)+1)+'#'+'_'*(n-i))
        elif i==1:
            print('_'*(n-1)+'#'+'_'*(n-1))
        else:
            print('#'*(2*i-1))

if __name__=='__main__':
    hollow_triangle(n=int(input('Ingrese el numero: ')))

 #'_____#_____', '____#_#____', '___#___#___', '__#_____#__', '_#_______#_', '###########']