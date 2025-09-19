import re
#Colocamos una cadena de texto
texto = "Reemplazando todas las vocales por asteriscos"
print("El texto inicial es: ",texto) #Mostramos el texto inicial
#Se realiza el cambio de las vocales por asteriscos del texto inicial
#Si colocamos solo "aeiou" sin los corchetes busca literalmente una coincidencia escrita asi
#Con los corchetes busca por separado cada una de las vocales en el texto
nuevo_texto = re.sub("[aeiou]","*",texto)
#Mostramos el nuevo texto
print("El nuevo texto es: ",nuevo_texto)
