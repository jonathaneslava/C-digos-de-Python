#Para llamar las funciones de otro archivo, tenemos que importar el archivo solo con el nombre no con la extension
import modulo_saludar as m_saludar #as nos sirve para colocar un nombre diferente al modulo del que estemos importando
#Nos evita conflicto en caso de que tengamos variables con el mismo nombre que el nombre del modulo
#La funcion que tenemos en el modulo saludar pasa a ser un metodo ahora en el archivo actual

#Si no queremos importar todo el modulo con todas sus funciones
#Lo que hacemos es seleccionar solo la funcion que deseemos y solo se importa eso
#from modulo_saludar import saludar
#Si igual deseamos renombrar el nombre de una funcion podemos usar as
#from modulo_saludar import saludar as nuevo_nombre_saludo
#Si queremos importar todo usando from, aunuque esto es una mala practica pero lo hacemos como 
#from modulo_saludar import *
saludo = m_saludar.saludar("Jonathan") #Para llamar al metodo colocamos el nombre del modulo.nombre de la funcion y finalmente el parametro
saludo_banda = m_saludar.saludar_banda("Jonathan") #Para llamar al metodo colocamos el nombre del modulo.nombre de la funcion y finalmente el parametro
print(saludo)
print(saludo_banda)