#Detectando un numero CABA y ocultandolo
import re
texto = "Hola Jona, mi numero es: +54 11 4321-4321"
print("Texto inicial: ",texto)
#Colocamos las coincidencias que vamos a cambiar
#Primero buscamos el mas \+, despues \d{2} busca dos numeros, despues busca un espacio \s,
#despues \d{2} busca dos numeros, despues busca un espacio \s,
#despues \d{4} busca cuatro numeros, buscamos un guion medio -,
#finalmente \d{4} busca cuatro numeros
coincidencia = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'
#Reemplazamos las cincidencias por un nuevo texto en el texto inicial
reemplazo = re.sub(coincidencia,"(Numero oculto)",texto)
#Mostramos el nuevo texto despues del cambio
print("Texto actualizado: ",reemplazo)
