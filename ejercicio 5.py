'''5- Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si
quiere calcular y mostrar su perímetro o su superficie y en función de eso llame a la función
perímetro o superficie.
'''


def perimetro(lado):
    return lado * 4

def superficie(lado):
    return lado * lado
    

PERIMETRO = 1
SUPERFICIE = 2

print(''' Programa que calcula el perimetro o superficie de un cuadrado
1) Perimetro
2) Superficie
''')
opc = int(input("Selecciona una opcion: "))

lado = int(input("Ingrese el lado: "))


if opc == PERIMETRO:
    print (f'Perimetro = {perimetro(lado)}')
if opc == SUPERFICIE:
    print (f'Superficie = {superficie(lado)}')





