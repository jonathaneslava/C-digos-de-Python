import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leemos el archivo csv, colocamos la ruta y se lee
df = pd.read_csv("Archivos_problemas_graficos\\peso.csv")
#indicamos que realizaremos un grafico lineal con lineplot
#Especificamos los ejes de la grafica, busca la columna fecha y la establece como eje x
#Busca la columna peso y la establece como eje y, finalmente de donde se obtiene la informacion
#Se coloca df ya que es el documento csv donde estan los datos
sns.lineplot(x="fecha",y="peso",data=df)

#Si quiero marcar el punto mas alto de mis datos se coloca:
#La fecha en la que esta el peso mas alto, despues el peso y finalmente la marca "o" que es un punto
plt.plot("01-09",72,"o")

plt.show() #Con esto mostramos el grafico