'''
Escribir una función que, dado un número de DNI, retorne True si el número es válido y False
si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígito'''


def dni_correcto (dni):
    if len(dni) == 7 or len(dni) == 8:
        print("DNI valido")
        return True
    else:
        print("DNI invalido")
        return False

dni = str(input("Coloque el DNI: "))
dni_correcto(dni)



