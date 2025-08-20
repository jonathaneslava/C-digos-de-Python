#Creando diccionarios con dict
#Dict funciona con clave valor, es decir la clave es nombre y el valor es Jonathan
diccionario = dict(nombre = "Jonathan", apellido = "Eslava")
print(diccionario)

#Si queremos crear diccionarios vacios entonces se debe realizar con set
#Las listas no pueden ser claves, una tupla puede ser una clave
diccionario = {("Jonathan","Eslava"): "Ja"}
print(diccionario)

#Creando diccionario con fromkeys
#Si colocamos el los elementos sin  corchete, el primer elemento sera algo que se pueda iterar y el
#segundo elemento sera su valor
diccionario = dict.fromkeys("nombre","apellido")
print(diccionario)
#Si colocamos corchetes los elementos tendran un valor por defecto de none para cada elemento
diccionario = dict.fromkeys(["nombre","apellido"])
print(diccionario)