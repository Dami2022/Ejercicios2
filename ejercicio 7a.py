'''7- Modificar utilizando dos archivos independientes para las funciones y el programa principal
utilizando import '''

from ejercicio7b import perimetro, superficie


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

