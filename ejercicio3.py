#escribir numero como letra

def numberOfLetter():
    n='30'
    n=n.split('')#separa el numero en una lista
    for i in n:
        if i in '0123456789':
            i=chr(int(i)+96)
    return n

                

print(numberOfLetter())
