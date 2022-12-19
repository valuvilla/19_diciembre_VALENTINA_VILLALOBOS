
def hollow_triangle ( n ): # n es el numero de filas de la piramide
    for i in range(1,n+1):
        if i==1:
            print('_'*(n-1)+'#'*1+'_'*(n-1))
        elif i!=n:
            print('_'*(n-i)+'#'*1+'_'*(i-1)+'#'*1+'_'*(n-i))
        else:
            print('#'*(2*n-1))

hollow_triangle(5)