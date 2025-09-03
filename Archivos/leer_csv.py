import csv #Importamos csv para acceder a los metodos que contiene

with open("Archivos\\datos_prueba.csv") as archivo:
    reader = csv.reader(archivo)
    print(reader)
    #Si queremos recorrer fila por fila el csv se usa
    for row in reader:
        print(row)