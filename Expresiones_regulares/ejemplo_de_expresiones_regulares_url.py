import re
#Escribimos un ejemplo de direccion de pagina web
url = "Este es un ejemplo de pagina web: https://www.example.com"
#Busca https, ? busca una coincidencia o no y lo muestra, despues debe de haber ://
#Despues busca al menos una vez alguna de estas coincidencias [a-zA-Z0-9.-]
#Despues debe de haber un punto y finalmente busca al menos 2 de [a-zA-Z]{2,}
coincidencia = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
#Busca las coincidencias especificadas y si encuentra muestra la url
resultado =  re.findall(coincidencia,url)
print(resultado)
