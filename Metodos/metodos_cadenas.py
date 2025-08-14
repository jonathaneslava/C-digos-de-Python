#Metodos y funciones en python
cadena1 = "Hola soy Jonathan"
cadena2 = "Bienvenido"

#Dir es una funcion de python, devuelve la lista de atributos validos del objeto pasado
resultado = dir(cadena1)
print(resultado)

#UPPER es un metodo de python, devuelve todo en mayusculas y se escribe de la sig. forma
#Dato.metodo()
mayuscula = cadena1.upper()
print(mayuscula)

#LOWER es un metodo de python, devuelve todo en minuscula y se escribe de la sig. forma
#Dato.metodo()
minuscula = cadena1.lower()
print(minuscula)

#Capitalize es un metodo de python, devuelve primer letra en mayusculas y se escribe de la sig. forma
#Dato.metodo()
primer_letra_en_mayuscula = cadena1.capitalize()
print(primer_letra_en_mayuscula) #Primero convierte todo en minuscula y despues pone la primer letra en mayuscula

#Buscamos una cadena en otra cadena
#Find nos devuelve la posicion de la palabra, un espacio tambien se considera posicion
busqueda_find = cadena1.find("z")
print(busqueda_find)#Si no encuentra nada entonces devuelve -1

#Buscamos una cadena en otra cadena
#Find nos devuelve la posicion de la palabra, un espacio tambien se considera posicion
busqueda_index = cadena1.index("a")
print(busqueda_index)#Si no encuentra nada entonces devuelve una excepcion, diferencia entre find y index es que index manda una excepcion en caso de no encontrar nada

#Isnumeric, si es numerico devuelve true, en caso de que no entonces devuelve false
es_numerico = cadena1.isnumeric()
print(es_numerico)

#isalpha, si es alfanumerico devuelve true, en caso de que no entonces devuelve false
es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico) #Los espacios no son alfanumericos por eso el resultado es false, en caso de no tener espacios devuelve true
