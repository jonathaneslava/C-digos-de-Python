#With open nos ayuda en que no tenemos que estar cerrando el archivo manualmente
#Cada ue abrimos un archivo se abre como lectura
#Si queremos renombrar toda la ruta para que sea mas sencillo el uso colocamos as y el nuevo nombre
with open("Archivos\\texto_de_prueba.txt",encoding="UTF-8") as archivo:
    #Leemos el contenido del archivo
    contenido = archivo.read()
    #Mostramos el contenido
    print(contenido)
    