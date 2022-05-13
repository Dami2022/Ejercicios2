'''6- Modificar el código anterior para que en función retorne el valor calculado.
'''

def perimetro(lado):
    lado = lado * 4
    return lado

def superficie(lado):
    lado = lado * lado
    return lado
    

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