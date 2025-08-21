#Creamos un contador que se va incrementar en el bucle while
contador = 0
#El bucle while funciona cuando una condicion es verdadera, en caso contrario termina
while (contador < 10): #Mientras contador sea menor a 10
    print(contador) #Muestra el valor de contador
    contador = contador +1 #Incrementa el valor de contador sino se vuelve un bucle infinito

print("Fuera del bucle while")