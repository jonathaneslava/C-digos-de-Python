#Para escribir en un archivo y no sobreesribirlo usamos append "a"
#"a" significa append y hacemos referencia a que solicitamos permisos para agregar en el archivo
with open("Archivos\\texto_de_prueba.txt","a",encoding="UTF-8") as archivo:
    #Con append no se sobreescribe el archivo que se esta modificando 
    #Agregando el archivo
    #Para escribir colocamos writelines y le pasamos una lista con el contenido que queremos guardar
    archivo.write("Nuevo texto \n") #Escribimos 2 lineas
    #Podemos usar un bucle para agregar mas texto en el archivo
    for i in range(5):
        archivo.write(f'Agregando linea {i}, nuevo texto \n')
    