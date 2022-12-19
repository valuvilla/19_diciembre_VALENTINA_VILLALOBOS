
def Tribonnaci(*args, n):
    for i in range(n):
        if n == 1:
            return args[0]
        elif n == 2:
            return args[1]
        elif n == 3:
            return args[2]
        else:
            args[i]=Tribonnaci(*args, n=i-1) + Tribonnaci(*args, n=i-2) + Tribonnaci(*args, n=i-3)
    return args

print(Tribonnaci(1,2,3, n=5))