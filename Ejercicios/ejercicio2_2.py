#Creando una funcion que nos devuelva los numeros primos
#Entre 0 y el argumento que le pasemos
def es_primo(num):
    for i in range (2,num-1): #El bucle comienza en 2 ya que queremos ver si el numero no es divisible por otro numero que 1
                              #Ademas num-1 ya que el numero es divisible entre el mismo numero
                              #Queremos revisar que no sea divisible por ningun numero
        if (num%i==0): return False #Si esto es falso quiere decir que si es divisible y termina la funcion
    return True

#Revisamos si funciona la funcion
resultado = es_primo(13)
print(resultado)

#Ahora creamos una funcion que nos devuelva la lista de los numeros primos hasta el numero que digamos
def lista_de_primos(num):
    primos= [] #Creamos la lista que nos va almacenar los numeros primos
    for i in range(3,num+1): #Colocamos que desde el 3 comienza el bucle para no considerar el 1 y 2, hasta num+1
        resultado = es_primo(i) #Llamamos a la funcion para ver si es primo
        if (resultado == True): #Si resultado es true entonces 
            primos.append(i) #Almacenamos el numero en la lista de primos
    return primos #Retornamos la lista de numeros primos

resultado_lista = lista_de_primos(13) #Llamamos a la funcion y colocamos hasta que numero queremos la lista
print(resultado_lista)
            
            