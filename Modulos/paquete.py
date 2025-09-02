#Para que python detecte que una carpeta es un paquete lo que se tiene que hacer es
#Crear un archivo con el nombre de "__init__.py" el archivo no debe contener nada python lo visualiza como paquete 
import paquete.saludar

print(type(paquete))

#Accedemos primero al paquete despues a la funcion y le pasamos el parametro que solicita la funcion
print(paquete.saludar.saludar("Jonathan"))

#Si tenemos un paquete y un archivo con el mismo nombre se le da prioridad al paquete