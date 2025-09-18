import re
#Escribimos una cadena de texto para usar las expresiones regulares
texto = "The Nightmare Before Chrismas"
#Buscamos que the este al inicio, seguirle caracteres que no sean espacios en linea y finalmente que Chrismas este al final
busca = re.search("^The.*Chrismas$",texto)

if busca:
    print("SI") #Si lo cumple nos muestra si
else:
    print("NO") #Si no lo cumple muestra no