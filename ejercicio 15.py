
'''
Escribir un programa que permita al usuario obtener un identificador para cada uno de los
socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio,
indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.
Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse
más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más
de un apellido, el usuario sólo ingresará uno.

Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa
debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer
nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI. Ejemplo:
Nombre: Alba María Linares
DNI: 25834910
Alba7258
'''

def identificador_usuario (nombre_completo,dni):
    if len(nombre_completo.split(" ")) <=2:
        nombre = nombre_completo.split(" ")[0]
        apellido = nombre_completo.split(" ")[1]
        identificador = nombre + str(len(apellido)) + dni[:4]
    if len(nombre_completo.split(" ")) >2:
        nombre = nombre_completo.split(" ")[0]
        apellido = nombre_completo.split(" ")[2]
        identificador = nombre + str(len(apellido)) + dni[:4]

    return identificador

def dni_valido (dni):
    if len(dni) == 7 or len(dni) == 8:
        return True
    else:
        return False

while True:
    nombreCompleto = int(input("Ingrese el nombre completo: (nombre1) (nombre2) (apellido)"))
    if nombreCompleto == "":
        print("No se puede colocar nombre vacio")
        break
    dni = int("Coloque su DNI: ")
    while not dni_valido:
        dni = int("Coloque DNI valido: ")

print(" Datos del socio: ", identificador_usuario(nombreCompleto,dni))