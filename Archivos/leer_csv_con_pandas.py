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