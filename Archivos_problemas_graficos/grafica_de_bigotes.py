import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leemos el archivo csv, colocamos la ruta y se lee
df = pd.read_csv("Archivos_problemas_graficos\\bigotes.csv")
#indicamos que realizaremos un grafico de bigotes con boxplot, muestra la dispersion de datos en cuartiles
#Especificamos los ejes de la grafica, busca la columna categoria y la establece como eje x
#Busca la columna valor y la establece como eje y, finalmente de donde se obtiene la informacion
#Se coloca df ya que es el documento csv donde estan los datos
sns.boxplot(x="categoria",y="valor",data=df)

plt.show() #Con esto mostramos el grafico