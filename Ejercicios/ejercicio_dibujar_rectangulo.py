#Ejercicio dibujar un rectangulo
n=5 #Se define el tamaño del rectangulo
for i in range(n): #Recorre cada fila del 0 al 4 
    for j in range (n): #Recorre cada columna del 0 al 4
        if (i==0 or i==n-1 or j==0 or j==n-1): #Si nos encontramos en los bordes 
            print("*",end="") #Muestra los "*" completos 5 en fila y 5 en columna sin salto de linea
        else:
            print(" ",end="") #Si estamos en el interior del rectangulo imprime blanco sin salto de linea
    print() #Salto de linea al terminar la fila