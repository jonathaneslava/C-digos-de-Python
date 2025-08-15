#Metodos y funciones en python
cadena1 = "Hola soy Jonathan"
cadena2 = "Bienvenido,Jonathan"

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

#Buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
#COUNT cuenta las veces que encuentra una cadena en otra cadena que coincida o caracteres que coincidan
contrar_coinicidencias = cadena1.count("Hola")
print(contrar_coinicidencias)

#Funcion Len, Contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)
print(contar_caracteres)

#Startswitch, verificamos si una cadena empieza con una cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("H")
print(empieza_con)

#Endswitch, verificamos si una cadena termina con una cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("Jonathan")
print(termina_con)

#Replace, remplaza un pedazo de la cadena dada, por otra cadena 
#Si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
#Si no encuentra coincidencias entonces no modifica nada y regresa el valor original
cadena_nueva = cadena1.replace("h","J")
print(cadena_nueva)
#Sirve para remplazar comas por espacios en una cadena
cadena_nueva1 = cadena2.replace(","," ")
print(cadena_nueva1)
#Sirve para quitar mayusculas en caso de encontrarlas en una cadena
cadena_nueva2 = cadena_nueva1.capitalize()
print(cadena_nueva2)

#Split, Separa cadenas con la cadena que le pasemos
#Si nuestra cadena dice "Hola, Jonathan" nos da 2 elementos en lista porque esta separada por una coma, tenemos dos elementos
cadena_separada = cadena2.split(",")
print(cadena_separada)