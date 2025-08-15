#Listas en python
#Funcion List, crea una lista
lista = list (["Hola", "Jona", 24, True])
print(lista)

#Metodo LEN devuelve la cantidad de elementos que tenemos en la lista
cantidad_elementos = len(lista)
print(cantidad_elementos)

#Metodo append agrega elementos a nuestra lista
lista.append("Ja")
print(lista)

#Metodo insert agrega un elemento a la lista en un indice en especifico
lista.insert(2,"Nuevo elemento")
print(lista)

#Metodo extend agrega varios elementos a la lista, agregamos una lista con elementos a otra lista
lista.extend([False,34])
print(lista)

#Metodo pop, eliminamos un elemento de la lista por su indice
lista.pop(7)
print(lista)
#Si queremos eliminar el ultimo elemento de la lista colocamos -1
#Si queremos eliminar el penultimo elemento de la lista colocamos -2
#Si queremos eliminar el antepenultimo elemento de la lista colocamos -3 y asi sucesivamente
lista.pop(-1)
print(lista)

#Metodo remove, elimina el elemento de la lista por su valor, si no encuenta el valor no borra nada y lanza una excepcion
lista.remove("Jona")
print(lista)

#Metodo clear, elimina todos los elementos de la lista
lista.clear()
print(lista)

#Funcion sort, ordena los elementos de la lista de forma ascendente
#No funciona si hay cadena de texto
lista_nueva = list([True, 10, 56, 3, False])
lista_nueva.sort()
print(lista_nueva)
#Si queremos ordenar los elementos de la lista de forma descendente entonces colocamos reverse
lista_nueva.sort(reverse=True)
print(lista_nueva)

#Reverse, invirtiendo los elementos de la lista
lista_nueva.reverse()
print(lista_nueva)

#En una tupla solo podemos buscar elementos y contarlos, no se pueden usar otros metodos
#Las tuplas son inmutables por lo que no se puede modificar nada de ellas.
#En los conjuntos solo se pueden borrar elementos