#Para escribir en un archivo es necesario colocar la ruta del archivo y tambien colocar "w"
#"w" significa write y hacemos referencia a que solicitamos permisos para escribir en el archivo
with open("Archivos\\texto_de_prueba.txt","w",encoding="UTF-8") as archivo:
    #Con write se sobreescribe el archivo que se esta modificando 
    #Con el permiso de w si no encuentra el archivo lo crea
    #archivo.write("Con write se sobreescribe el archivo que se esta modificando ")
    #Para escribir colocamos writelines y le pasamos una lista con el contenido que queremos guardar
    archivo.writelines(["Hola, que tal \n","Hello \n"]) #Escribimos 2 lineas
    #Si colocamos mas writelines se van acumulando, es decir, nuestro archivo no se sobreescribe
    #Se va acumulando la informacion
    archivo.writelines(["Se acumulara nueva informacion \n","Nuevo salto de linea \n"]) #Escribimos lineas
    #Es importante dejar un salto de linea al finalizar una linea