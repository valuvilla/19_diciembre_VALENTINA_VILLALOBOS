
def hollow_triangle ( n ): # n es el numero de filas de la piramide
    for i in range(1,n+1):
        if i==1:
            print('_'*(n-1)+'#'*1+'_'*(n-1))
        elif i!=n:
            print('_'*(n-2)+'#'*1+'_'*(2**(i-2))+'#'*1+'_'*(n-2))
        else:
            print('#'*(2*n-1))

hollow_triangle(5)