import re

#Escribimos una cadena de texto que se usara para las expresiones regulares
fecha = "La fecha es 17/09/2025 y el telefono es +1-555-555-5555"
print("Texto inicial: ",fecha)

#El patron que vamos a buscar sera la fecha 
#Primero buscamos 2 numeros y una diagonal, despues 2 numeros y una diagonal y finalmente 4 numeros
busca_fecha = r"\d{2}/\d{2}/\d{4}"

#Texto que usaremos para reemplazar la fecha
reemplaza_fecha = "Fecha oculta exitosamente"

#Reemplazamos la fecha con el nuevo texto en la cadena inicial
nuevo_texto = re.sub(busca_fecha,reemplaza_fecha,fecha)

#Muestra el resultado
print("Texto modificado: ",nuevo_texto)

