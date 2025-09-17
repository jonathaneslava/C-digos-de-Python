import re #Modulo que utilizamos para manejar expresiones regulares
texto = '''Esta es la linea 1 de texto.
Esta es la linea 2 de texto.
Esta es la linea 3 de texto.
'''
#Realizando busquedas simples
resultado_con_search = re.search("Esta",texto)#Busca coincidencias (busca, en la cadena de texto)
print(resultado_con_search)
#si queremos que nuestra busqueda sea sin importar mayusculas o minusculas colocamos
#re.findall("Esta",texto,flags=re.IGNORECASE)
resultado_con_findall = re.findall("Esta",texto)#Muestra todas las coincidencias con la palabra buscada en texto
print(resultado_con_findall)

#\d busca digitos numericos del 0-9
#r nos indica que vamos usar las expresiones regulares, "\d" voy a buscar del 0-9 en texto
resultado = re.findall(r"\d",texto)
print("\d Busca digitos numericos del 0-9")
print(resultado)

#\D busca TODO MENOS digitos numericos del 0-9
#r nos indica que vamos usar las expresiones regulares, "\D" voy a buscar TODO MENOS numeros del 0-9 en texto
resultado = re.findall(r"\D",texto)
print("\D Busca TODO MENOS digitos numericos del 0-9")
print(resultado)

#\w busca caracteres alfanumericos [a-z A-Z 0-9 _]
#r nos indica que vamos usar las expresiones regulares, "\w" busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w",texto)
print("\w Busca caracteres alfanumericos [a-z A-Z 0-9 _]")
print(resultado)

#\W busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
#r nos indica que vamos usar las expresiones regulares, "\W" busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W",texto)
print("\W Busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]")
print(resultado)

#\s busca espacios en blanco -> espacios, tabs, saltos de linea
#r nos indica que vamos usar las expresiones regulares, "\s" busca espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r"\s",texto)
print("\s Busca espacios en blanco -> espacios, tabs, saltos de linea")
print(resultado)

#\S busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea
#r nos indica que vamos usar las expresiones regulares, "\S" busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r"\S",texto)
print("\S Busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea")
print(resultado)

#. busca TODO menos saltos de linea
#r nos indica que vamos usar las expresiones regulares, "." busca TODO menos saltos de linea
resultado = re.findall(r".",texto)
print(". Busca Todo menos saltos de linea")
print(resultado)

#\n busca saltos de linea
#r nos indica que vamos usar las expresiones regulares, "." busca saltos de linea
resultado = re.findall(r"\n",texto)
print(". Busca saltos de linea")
print(resultado)

#\. Cancela caracteres especiales, cancelando la funcion del punto y buscando puntos
#r nos indica que vamos usar las expresiones regulares, "\." Cancela caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado = re.findall(r"\.",texto)
print("\ Cancela caracteres especiales, cancelando la funcion del punto y buscando puntos")
print(resultado)

#Armando una cadena que busque un numero, seguido de un punto y un espacio en linea 