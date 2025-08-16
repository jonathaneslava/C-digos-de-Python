#Dado un numero, revisar si es par o impar
numero = input("Escribe un numero: ")

numero_del_usuario = int(numero)

if numero_del_usuario%2 == 0:
    print("Es par")
else:
    print("Es impar")