#Se crea una tupla y una lista
datos_en_tupla = ("Jonathan","Adrian",123456789)
datos_en_lista = ["Jonathan","Adrian",123456789]
#Se desempaqueta cada uno de los elementos de la tupla, siempre y cuando coincida el numero con la cantidad de elementos
nombre,apellidos,numero=datos_en_tupla
nombre,apellidos,numero=datos_en_lista
#Se muestra el elemento
print(numero)
