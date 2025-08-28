#Si se importan funciones de otro modulo de importan de la sig forma
import funciones_buenas.saludo
#Si deseamos importar desde otras carpetas atras se tiene que revisar la ruta del archivo
import sys
#print (sys.path) Esto nos ayuda para saber las rutas en las que se encuentran nuestros archivos
sys.path.append('c:\\Users\\Jonathan Eslava\\Desktop\\Python\\funciones_de_prueba_en_modulos')
import funciones_matematicas

#Para llamar al metodo saludar se debe colocar toda la ruta donde se encuentra para poder acceder de forma correcta
print(funciones_buenas.saludo.saludar("Jonathan"))

#Para llamar al metodo suma entonces colocamos 
print(funciones_matematicas.suma(2,30))