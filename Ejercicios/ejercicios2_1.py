#El profesor falto y los encargados de dar la clase son los alumnos
#Pedir el nombre y la edad de los compañeros que vinieron a clase
#El mayor de la clase sera el profesor y el menor su asistente

#Creamos la funcion que pedira la cantidad de alumnos
def obtener_alumnos(cantidad_de_alumnos):
    alumnos = [] #Creamos la lista en la que se va almacenar los valores
    for i in range (cantidad_de_alumnos): #Creamos un bucle que pedira el nombre y edad de los alumnos considerando que son 7
        nombre = input("Escribe tu nombre ") #Pide el nombre al alumno
        edad =int(input("Escribe tu edad ")) #Pide la edad pero recordemos que input nos da string por eso se convierte a entero
        alumno = (nombre,edad) #Almacenamos los valores en alumno
        alumnos.append(alumno) #Agregamos a la lista
        
    alumnos.sort(key=lambda x:x[1]) #Pedimos que se ordenen a los alumnos por su edad que eso es x[1] ya que es el segundo parametro
    asistente = alumnos[0][0] #Para buscar al asistente que es el menor de la clase lo que hacemos es 
                              #Pedir la posicion 0 ya que en la lista que nos crea lamda el primer valor es el de la edad y [0] es el primero
                              #Despues pedimos el [0] ya que es el nombre
    profesor = alumnos[-1][0] #Para buscar al profesor que es el mayor de la clase lo que hacemos es 
                              #Pedir la posicion -1 ya que en la lista que nos crea lamda el ultimo valor es el de la edad y [-1] es el ultimo
                              #Despues pedimos el [0] ya que es el nombre
    return asistente,profesor #Retornamos una tupla con asistente y profesor

#Llamamos a la funcion y desempaquetamos lo que nos devuelve
#Creamos dos variables que se van a recibir que es asistente y profesor y llamamos a la funcion
asistente,profesor = obtener_alumnos(5)
#Mostramos en pantalla quien es el asistente y quien es el profesor
print(f'El asitente de la clase es {asistente}')
print(f'El profesor de la clase es {profesor}')
print(f'El profesor de la clase es {profesor} y su asistente es {asistente}')
    
      