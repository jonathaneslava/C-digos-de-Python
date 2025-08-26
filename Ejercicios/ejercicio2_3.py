#Mostrar la serie fibonacci del 0 hasta un numero dado

def fibonacci(num): #Creamos la funcion que recibe como parametro un numero
    num1,num2 = 0,1 #Creamos las variables numero 1 y 2 que son los que se suman
    lista_fibonacci = [0] #Creamos la lista donde se van almacenar los numeros
    for i in range (num): #El bucle comienza en 0 hasta el numero que le demos
        if num2 > num: #Si el numero 2 es mas grande que el numero dado entonces nos regresa la lista
            return lista_fibonacci 
        else: #Si no se cumple la condicion del if entonces
            lista_fibonacci.append(num2) #Se agrega el numero 2 a la lista
            num1,num2 = num2,num1+num2 #Se actualizan los valores de numero 1 y 2
            
resultado_de_serie = fibonacci(34) #Llamamos a la funcion y le pasamos un numero
print(resultado_de_serie) #Muestra la serie de fibonacci