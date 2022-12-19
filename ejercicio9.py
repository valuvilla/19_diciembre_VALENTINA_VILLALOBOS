from datetime import datetime


def lunes():
    #Contar los lunes que hay desde el cumplaños hasta el dia de hoy
    
    #pedir fecha de cumpleaños
    cumple = input("Ingrese su fecha de cumpleaños (dd/mm/aaaa): ")
    cumple = datetime.strptime(cumple, "%d/%m/%Y")

    #pedir fecha de hoy
    hoy = input("Ingrese la fecha de hoy (dd/mm/aaaa): ")
    hoy = datetime.strptime(hoy, "%d/%m/%Y")

    #calcular edad (aprximada)
    edad = hoy.year - cumple.year

    if edad in range(22,79):
        diferencia = hoy - cumple
        lunes = diferencia.days // 7
        return lunes

    else:
        return 0

#Probamos el codigo
print(lunes())

if __name__ == '__main__':
    lunes()
