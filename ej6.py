




#calcular eñ area del parche circular
from math import pi


def area_circulo(diametro):
    radio=diametro/2
    area = pi * radio ** 2
    return area

def area_parche(diametro, porcentaje):
    area_circulo(diametro)
    area_parche = area_circulo(diametro) * porcentaje
    return area_parche

def circunferencia(diametro, porcentaje):
    area_parche(diametro, porcentaje)
    circunferencia = pi * diametro
    #aproximar circinferencia
    circunferencia = round(circunferencia, 0)
    return circunferencia

#probamos el codigo
print("El area del parche circular es: ", area_parche(10, 0.5))


if __name__=='__main__':
    print("El area del parche circular es: ", area_parche(10, 0.5))
    print("La circunferencia del parche circular es: ", circunferencia(10, 0.5))