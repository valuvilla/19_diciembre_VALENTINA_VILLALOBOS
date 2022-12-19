




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

def circunferencia(diametro):
    circunferencia = pi * diametro
    return circunferencia


