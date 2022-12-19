



from ast import main


def Tribonnaci(*args, n):
    lista=[]
    for i in range(len(args)):
        lista.append(args[i])

    for i in range(3,n+1):
        lista[i]=sum(((lista[::-1])[0:3]))
        lista.append(lista[i+3])
    return lista
#probamos el codigo
print(Tribonnaci(1,2,3, n=3))

if __name__=='__main__':
   main()