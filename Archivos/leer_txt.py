#Para leer un archivo en python se tiene que colocar el open y la ruta en la que esta el archivo
#UTF-8 es para leer caracteres especiales y que no nos de algo extraño
archivo_sin_leer = open("Archivos\\texto_de_prueba.txt",encoding="UTF-8")
#Una vez que esta en una variable para leerlo es necesario colocar .read()

#Leemos el archivo completo
#archivo = archivo_sin_leer.read()

#Leer linea por linea
#lineas = archivo_sin_leer.readlines()
#Nos da como resultado
#['Este es un archivo de texto.\n', 'Es una prueba para leer archivos en python.']
#Representa que son 2 lineas ya que el "\n" significa que es un salto de linea

#Leer solo una linea del archivo
linea = archivo_sin_leer.readline() #Si colocamos sin parametro el readline nos muestra toda la linea de texto completa
#En caso de colocarle un numero a readline() lo que nos va mostrar es la cantidad de caracteres que pedimos y que hay en esa linea

#Cerrar el archivo de texto
archivo_sin_leer.close()
#Si despues de cerrar el archivo lo queremos volver a leer con .read() marcara error ya que el archivo ya se leyo y se cerro
#Es importante cerrar el archivo para no perder informacion o almacenar nueva informacion
print(linea) 