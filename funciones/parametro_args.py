#Creamos una funcion que sume 2 numeros
def suma(a,b):
    return a+b
#Llamamos a la funcion creada
resultado = suma(5,5)
print(f'El resultado de la suma es: {resultado}')

#Para sumar numeros de una lista utilizamos la siguiente funcion
def sumar_lista(lista): #Pasamos como parametro una lista
    numeros_sumados = 0 #Creamos una variable que nos ayudara para sumar los elementos de la lista
    for numero in lista: #Se crea un bucle que nos ayudara a recorrer la lista
         numeros_sumados = numeros_sumados + numero
         #En esta variable se actualiza el valor cada que avanza el bucle
         #Si nuestra lista es de [10,5,1]
         #Numeros sumados comienza con el valor cero
         #Numeros sumados = 0 + 10
         #Numeros sumados ahora es 10
         #Numeros sumados = 10 + 5
         #Numeros sumados ahora es 15
         #Numeros sumados = 15 + 1
         #Resultado final de numeros sumados es 16
    return numeros_sumados

resultado_de_lista = sumar_lista([10,5,1])
print(f'El resultado de la suma de la lista es: {resultado_de_lista}')
#-------------------------------------------------------------------------------------

#Utilizando el opeador * como argumento (*args)
def suma_con_args(*numeros):
    return sum(numeros)

resultado_con_args= suma_con_args(1,2,3,4,5)
print(f'La suma usando args es: {resultado_con_args}')
#------------------------------------------------------------------------------------

#Tambien podemos usar (*args) dentro de nuestra funcion y no solo como parametro
def suma_con_args_dentro_de_funcion(numeros):
    return sum([*numeros]) #Para este caso si tenemos que crear la lista 

resultado_con_args_dentro_de_funcion = suma_con_args_dentro_de_funcion([1,2,3,4,5])
print(f'La suma usando args dentro de la funcion es: {resultado_con_args_dentro_de_funcion}')

#------------------------------------------------------------------------------------
#Utilizando el opeador * como argumento (*args) y colocando mas parametros
#Nota: si deseamos utilizar mas parametros en la funcion se deben colocar antes de args
#El parametro que este despues de args no se va ejecutar porque considera args como infinito
def suma_con_args_y_nombre(nombre,*numeros):
    return f'{nombre}, El resultado de tu suma es: {sum(numeros)}'

resultado_con_args_y_nombre = suma_con_args_y_nombre("Jona",1,2,3,4,5)
print(resultado_con_args_y_nombre)