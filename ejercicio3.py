#escribir numero como letra

from ast import main


def numberOfLetter():
    n='30'
    n=n.split('')#separa el numero en una lista
    for i in n:
        if i in '0123456789':
            i=chr(int(i)+96)
    return n
#probamos el codigo
print(numberOfLetter())
                
if __name__=='__main__':
   main()
   
