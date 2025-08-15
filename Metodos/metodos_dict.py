#Metodos de diccionarios
diccionario = {
    "nombre" : 'Jonathan',
    "apellido" : "Eslava",
    "Edad" : 24
}

#Keys devuelve las claves, tambien nos sirve para iterar
claves = diccionario.keys()
print(claves)

#Get nos devueve un valor solicitado, si no encuentra algo nos devuelve none y el programa continua sin lanzar excepciones
claves_get = diccionario.get("nombre")
print(claves_get)

#Pop elimina un elemento de un diccionario
diccionario.pop("nombre")
print(diccionario)

#Obteniendo un elemento de dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

#Clear elimina todo lo del diccionario
diccionario.clear()
print(diccionario)