#Creando una funcion con tres parametros
def frase (nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido} eres {adjetivo}'

#Utilizando keyword arguments
#En este caso al momento de pasar los argumentos se define cual sera cada uno sin importar el orden
frase_obtenida = frase(adjetivo = "Alto", nombre = "Jonathan", apellido = "Eslava")
print(frase_obtenida)

#-------------------------------------------------------------------------------------

#Creando una funcion con tres parametros
def frase_con_adjetivo_fijo (nombre,apellido,adjetivo="Bajo"):
    return f'Hola {nombre} {apellido} eres {adjetivo}'

#Utilizando keyword arguments
#En este caso al momento de pasar los argumentos se define cual sera cada uno sin importar el orden
frase_obtenida_con_adjetivo_fijo = frase_con_adjetivo_fijo("Jonathan","Eslava")
print(frase_obtenida_con_adjetivo_fijo)
#Se puede cambiar el valor fijo que nos da la funcion agregando uno adjetivo propio
frase_obtenida_con_adjetivo_fijo_y_cambiando_adjetivo = frase_con_adjetivo_fijo("Jonathan","Eslava",adjetivo="Altooo")
print(frase_obtenida_con_adjetivo_fijo_y_cambiando_adjetivo)