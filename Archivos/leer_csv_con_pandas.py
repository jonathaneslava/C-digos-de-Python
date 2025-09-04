#Cuando usamos la libreria de pandas comunmene se usan las siglas pd
import pandas as pd
print(type(pd))
#Colocamos el nombre de la variable como df que significa data frame
#Data frame son estructuras de datos bidimensionales similares a una hoja de calculo, tiene dos valores que se accede, filas y columnas
#Si queremos cambiar los encabezados de nuestras columas lo que hace es considerar ahora como datos
#Los antiguos nombres de nuestras columnas 
df = pd.read_csv("Archivos\\datos_prueba.csv", names=["name","lastname","age"])
print(df)
#Si queremos que solo muestre la columna nombre
nombres = df["name"]
print(nombres)