import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leemos el archivo csv, colocamos la ruta y se lee
df = pd.read_csv("Archivos_problemas_graficos\\ingresos.csv")
#indicamos que realizaremos un grafico de barras con barplot
#Especificamos los ejes de la grafica, busca la columna fuente y la establece como eje x
#Busca la columna ingreso y la establece como eje y, finalmente de donde se obtiene la informacion
#Se coloca df ya que es el documento csv donde estan los datos
sns.barplot(x="fuente",y="ingreso",data=df)

#Obteniendo el total de ingresos 
total_ingresos = df['ingreso'].sum() #Indica la columna de los datos que se van a sumar
#Mostramos la suma total de ingresos en la consola
print(f'La suma total de los ingresos es de: {total_ingresos}')
plt.show() #Con esto mostramos el grafico