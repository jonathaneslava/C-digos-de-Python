#Cambiar el tipo de dato de una columna
import pandas as pd
#Leemos el archivo csv
df = pd.read_csv("Archivo_problemas_resueltos\\datos_prueba.csv")
#Convertir a string los tipos de datos de una columna, de int a string
df ['edad'] = df ['edad'].astype(str)
#Mostrar el tipo de dato del primer elemento de la columna string
print(type(df['edad'][0])) #Da como resultado <class 'str'> y si no estuviera daria como resultado <class 'numpy.int64'>
#Si queremos remplazar un elemento del archivo lo podemos hacer de la siguiente forma
#Colocamos de que columna es el dato y remplazamos el antiguo elemento por el nuevo
df['nombre'].replace("Jonathan","Adrian",inplace=True)
print(df['nombre'])

#Eliminando filas con datos faltantes
df = df.dropna()

#Eliminando filas repetidas
df = df.drop_duplicates()

#Creando un CSV con el datafrme resultante (limpio)
df.to_csv("Archivo_problemas_resueltos\\datos_prueba_actualizado.csv")