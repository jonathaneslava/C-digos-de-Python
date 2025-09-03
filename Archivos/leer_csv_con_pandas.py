#Cuando usamos la libreria de pandas comunmene se usan las siglas pd
import pandas as pd
print(type(pd))
archivo = pd.read_csv("Archivos\\datos_prueba.csv")
print(archivo)