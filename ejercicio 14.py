'''
Se necesita desarrolla un programa para facturar. Ingresar Artículo, precio unitario y cantidad
llamar a una función que calcule el importe total de la venta. También desarrollar una función
de determine si se le debe realizar un descuento o no. Si la venta es superior a $15000 debe
realizar un descuento del 8% si es mayor a $30000 15%. Mostrar el total de la venta y el
descuento.
'''

def importeTotal (art,precio,cant):
    resultado = precio * cant
    return resultado

def descuento (importe):
    if importe > 15000:
        print("Se le realiza un descuento del 8%")
        return importe * 0.08
    elif importe > 30000:
        print("Se le realiza un descuento del 15%")
        return importe * 0.15
    else:
        print("No hay decuentos")
        return 0

articulo = input("Ingrese el articulo: ")
precio = int(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))


print("El articulo ingresado es el siguiente: " ,articulo)
print("El importe total de la venta es: $", importeTotal(articulo, precio, cantidad))
print("El descuento es de: %", descuento(importeTotal(articulo, precio, cantidad)))


