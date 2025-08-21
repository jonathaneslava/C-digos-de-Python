#Se crea el diccionario
diccionario = {
    "nombre" : "Jonathan",
    "apellido" : "Eslava",
    "edad" : 24
}
#Si se deja el for de esta forma solo nos muestra la clave y no los valores asignados
for key in diccionario:
    print(key)
#Para visualizar los valores que tiene asignados cada una de las claves del diccionario
for key in diccionario.items():
    print(key)
#Si queremos mostrar la calve valor por medio de un mensaje al usuario colocamos
for datos in diccionario.items():
    key = datos[0] #Es la clave
    valor = datos[1] #Es el valor
    print(f'La clave es {key} y el valor {valor}')