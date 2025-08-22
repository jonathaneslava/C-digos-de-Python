#Explicacion de funciones lambda
#Lambda crea funciones anonimas que despues podemos almacenar en variables
#Beneficio, lo podemos usar cuando queremos hacer algo sencillo y rapido
#No son aptas cuando queremos colocar mas de una instruccion
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(44))

#--------------------------------------------------------------------------------------

numeros=[1,2,3,4,5,6,7,8,9,10]
#Creando una funcion comun que me diga si los numeros son pares o no
def es_par(num):
    if(num%2==0):
        return True
#Si utilizamos filter es como usar un bucle artificial ya que pasamos la lista de numeros
#Recorrre esa lista y nos devuelve una lista con los numeros que son pares
#A filter le pasamos como parametro la funcion y la lista que va revisar para ver si es par o no
numeros_pares = filter(es_par,numeros)
print(list(numeros_pares))

#-------------------------------------------------------------------------------------

#Si deseamos hacer lo mismo que la funcion es par pero usando lamdba
#lambda colocamos el valor a utilizar numero: agregamos la condicion u operacion que tiene que realizar
#Por ultimo esa funcion creada con lambda nos devuelve los numeros que cuplan la condicion
numeros_pares_con_lambda = filter(lambda numero:numero%2==0,numeros)
print(list(numeros_pares_con_lambda))