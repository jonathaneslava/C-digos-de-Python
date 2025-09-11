import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leemos el archivo csv, colocamos la ruta y se lee
df = pd.read_csv("Archivos_problemas_graficos\\dispersion.csv")
#indicamos que realizaremos un grafico de dispersion con scatterplot
#Especificamos los ejes de la grafica, busca la columna tiempo y la establece como eje x
#Busca la columna dinero y la establece como eje y, finalmente de donde se obtiene la informacion
#Se coloca df ya que es el documento csv donde estan los datos
sns.scatterplot(x="tiempo",y="dinero",data=df)

plt.show() #Con esto mostramos el grafico