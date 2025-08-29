#Ejercicio de dibujar un triangulo rectangulo
n=10 #Definimos el limite de base que tendra el triangulo
for i in range (1,n): #El ciclo va de i=1 hasta el limite de base de nuestro triangulo
    i=i+1 #Incrementamos nuestra variable ahora i=2
    for j in range (1,i): #El segundo ciclo j=1 hasta i dibuja la cantidad de "*" del triangulo
        j=j+1
        print("*",end="")        
    print()#Realiza el salto de linea para dibujar los nuevos "*" del triangulo

