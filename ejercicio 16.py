
'''
Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la primera
letra de cada palabra a mayúscula y las demás letras a minúscula, dejando
inalterados los demás caracteres. Precondición: el separador de palabras es el
espacio: " ". Agregar doctests con suficientes casos de prueba para validar que la
función retorna el valor esperado ante distintos argumentos.
'''

def titulo(frase):
    frase = frase.split(" ")
    for i in range(len(frase)):
        frase[i] = frase[i].capitalize()
    return " ".join(frase)


print (titulo("Bienvenidos a la prueba de capitalizar todas las palabras!!"))
print (titulo("Buenos dias a la funcion de capitalizar!!!!"))
print (titulo("Hola mundo este es un prueba!!"))
print (titulo("Habia una vez un programa que ejecutaba una funcion"))