#Creando un conjunto con set
conjunto = set(["dato1","dato2"])
print(conjunto)

#Set no permite colocar listas dentro ni tampoco diccionarios
#Si queremos colocar un conjunto dentro de otro conjunto lo hacemos con frozenset
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)

#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1}
#Verificar si un conjunto es un subconjunto de otro
#Se usa el metodo issubset nos devuelve si el conjunto 2 es un subconjunto del conjunto 1
#Nos da un resultado booleano
resultado = conjunto2.issubset(conjunto1)
print(resultado)

#Otra forma de revisar si el conjunto 2 es un subconjunto del conjunto 1 es usar mayor igual
resultado = conjunto2 <= conjunto1
print(resultado)

#Verificar si un conjunto es un superconjunto de otro
#Se usa el metodo issuperset nos devuelve si el conjunto 2 es un superconjunto del conjunto 1
#Nos da un resultado booleano
resultado = conjunto2.issuperset(conjunto1)
print(resultado)

#Otra forma de revisar si el conjunto 2 es un superconjunto del conjunto 1 es usar mayor igual
resultado = conjunto2 > conjunto1
print(resultado)

#Si queremos revisar si solo un elemento coincide 
#Nos devuelve true si los elementos no coinciden, nos devuelve false si conincide al menos un elemento
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)