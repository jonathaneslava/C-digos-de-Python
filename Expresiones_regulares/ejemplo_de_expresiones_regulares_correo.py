import re
#Escribimos un correo electronico de ejemplo
email = "example@example.com"
#Colocamos las coincidencias que debe tener correo para ser valido
#Son validas las coincidencias de a-zA-Z0-9,todo lo que no sea un espacio en linea "."
#El % es valido, el "+" busca una o mas coincidencias, con el "-" busca al menos una coincidencia 
#+@ busca al menos una vez una coincidencia de lo que se explico anteriormente y busca un @
#\. buscamos todo menos espacios en linea y un punto
#[a-zA-Z]{2,} buscamos al menos dos veces letras despues del punto, apartir de 2 es ilimitado
coincidencia = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
#Buscamos las coincidencias especificadas en el email
resultado = re.match(coincidencia,email)
#Colocamos la condicion de que si el resultado coincide entonces es valida, si no no es valida
if resultado:
    print("Direccion de correo electronico valida")
else:
    print("Direccion de correo electronico invalida")
