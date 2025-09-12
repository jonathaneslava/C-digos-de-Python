import re #Modulo que utilizamos para manejar expresiones regulares
texto = '''Esta es la primera linea de texto
Esta es la segunda linea de texto
Esta es la tercera linea de texto
'''
#Realizando busquedas simples
resultado_con_search = re.search("Esta",texto)#Busca coincidencias (busca, en la cadena de texto)
print(resultado_con_search)
#si queremos que nuestra busqueda sea sin importar mayusculas o minusculas colocamos
#re.findall("Esta",texto,flags=re.IGNORECASE)
resultado_con_findall = re.findall("Esta",texto)#Muestra todas las coincidencias con la palabra buscada en texto
print(resultado_con_findall)