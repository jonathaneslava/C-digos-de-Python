#Variables son espacios que se almacenan en la memoria de nuestro programa
#Se llaman variables porque van cambiando si se requiere.
a = 5
b = 8
c = a + b
print(c)

nombre = "Jonathan"
print(nombre)

d = 20 + 30
print(d)
#-------------------------------------------------------------------------------
#Declarar variables 
apellido = "Eslava" # declara variable = "se define"
#-------------------------------------------------------------------------------
#Se redefine la variable
segundo_nombre = "Adrian"
segundo_nombre = "Jadrian"
print(segundo_nombre)
#------------------------------------------------------------------------------
#Concatenar con +
bienvenida = "Hola " + nombre + " Como estas"
print(bienvenida)
#Otra forma de concatenar es colocando fstrings "Toma un dato y lo convierte en texto"
segunda_bienvenida = f"Hola {nombre} Como estas"
print(segunda_bienvenida)
#------------------------------------------------------------------------------
#Borra el contenido de la variable
del nombre
#------------------------------------------------------------------------------
#Operadores de pertenencia
#in y not in solo dan true o false dependiendo el caso
#Para ver si un texto se encuentra en una variable colocamos 
#Da como resultado true o false
print ("ola" in segunda_bienvenida) #True
print ("Jose" not in segunda_bienvenida) #True
#------------------------------------------------------------------------------
#Definiendo una variable con camelCase
#La separacion de cada palabra se escribe con mayuscula 
nombreDelUsuario= "Javier"
#Lo recomendable en python es usar snake_case
nombre_del_usuario="Manuel"