#Cuando usamos la libreria de pandas comunmene se usan las siglas pd
import pandas as pd
print(type(pd))
#Colocamos el nombre de la variable como df que significa data frame
#Data frame son estructuras de datos bidimensionales similares a una hoja de calculo, tiene dos valores que se accede, filas y columnas
#Si queremos cambiar los encabezados de nuestras columas lo que hace es considerar ahora como datos
#Los antiguos nombres de nuestras columnas 
#df = pd.read_csv("Archivos\\datos_prueba.csv", names=["name","lastname","age"])
df = pd.read_csv("Archivos\\datos_prueba.csv")
df2 = pd.read_csv("Archivos\\datos_prueba.csv") #Suponemos que tenemos 2 dataframes
print(df)
#Si queremos que solo muestre la columna nombre
nombres = df["nombre"]
print(nombres)

#Creamos una cadena para otro ejemplo
cadena = "0123456789"
#Si queremos ver todos los valores que contiene la cadena colocamos [:]
print(cadena[:]) #[Este lado indica de donde iniciamos : Este lado indica el valor hasta donde queremos que termine]
print(cadena[:3]) #Muestra desde 0 hasta la posicion 3

#Volviendo al uso del dataframe, si deseamos ordenar por edades de forma ascendente
#Por defecto si colocamos sort_values comienza ordenar de forma ascendente
df_orden_ascendente = df.sort_values("edad")
print(df_orden_ascendente)
#Si deseamos ordenar de forma descendente se tiene que colocar un segundo parametro
#En este caso df.sort_values("edad",ascending=False)
df_orden_descendente = df.sort_values("edad", ascending=False)
print(df_orden_descendente)

#Si deseamos concatenar 2 dataframes
df_concatenado = pd.concat([df,df2])
print(df_concatenado)

#Accediendo a las filas de arriba para abajo con head()
#Si usamos head sin ningun parametro nos muestra todos los datos df.head()
#Si colocamos un parametro nos mostrara los datos hasta esa posicion df.head(1) nos mostrara los datos de la posocion 0 y 1
primeras_fila = df.head(1)
print(primeras_fila)

#Accediendo a las filas de abajo hacia arriba con tail()
#Si usamos tail sin ningun parametro nos muestra todos los datos df.tail()
#Si colocamos un parametro nos mostrara los datos hasta esa posicion df.tail(2) nos mostrara los datos hasta la posicion 2
ultimas_filas = df.tail(2)
print(ultimas_filas)

#Accediendo a las filas y columnas con shape, nos muestra (cantidad de filas, cantidad de columnas)
filas_columnas_totales = df.shape
print(filas_columnas_totales)
filas_totales = df.shape[0]
columnas_totales = df.shape[1]
print(filas_totales)
print(columnas_totales)

#Obteniendo data estadistica del dataframe, usamos df.describe()
df_info = df.describe()
print(df_info)
