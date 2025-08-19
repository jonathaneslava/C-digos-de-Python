#Creando diccionarios con dict
#Dict funciona con clave valor, es decir la clave es nombre y el valor es Jonathan
diccionario = dict(nombre = "Jonathan", apellido = "Eslava")
print(diccionario)
#Si queremos crear diccionarios vacios entonces se debe realizar con set
#Las listas no pueden ser claves, una tupla puede ser una clave
diccionario = {("Jonathan","Eslava"): "Ja"}
print(diccionario)