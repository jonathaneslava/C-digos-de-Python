from datetime import datetime #Nos sirve para trabajar con fechas y horas en python

fecha_hora = datetime.now() #Llamamos a la funcion para que nos de la hora y fecha actual
print(f'Fecha y hora actual {fecha_hora}') 
#Mostramos la fecha de forma legible utilizando strftime
#%d dia con 2 digitos, %m mes con dos digitos y %Y año con 4 digitos
#%H formato de 24 hrs, %M minutos con 2 digitos y %S segundos con dos digitos
print("Fecha y hora actual:", fecha_hora.strftime("%d/%m/%Y %H:%M:%S"))