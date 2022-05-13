'''Se necesita desarrollar Programa(función)que presupueste cuánto saldrá el alambrado de un
campo. Para ello ingresar las medidas del terrero y el precio del metro de alambre. Crear un
módulo para calcular la cantidad de metros necesarios y calcular el costo del alambrado y
mostrar el costo. '''

from ejercicio10b import presupuesto


largo = int(input("Coloca la medida del largo del terreno: mts"))
ancho = int(input("Coloca la medida del ancho del terreno: mts"))
metro = int(input("Coloca el costo del metro del alambre: $"))

presupuesto(largo,ancho,metro)


