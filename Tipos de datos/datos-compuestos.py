#Los datos compuestos son datos que tienen otros datos adentro
#La lista es un conjunto de datos, usa []
lista = ["Jonathan","Eslava",True,1.65]
print (lista)
#Si quiero solo un elemento de la lista
print (lista[1])
#Si quiero modificar un elemento de la lista
lista[3]="positivo"
print (lista[3])
#En las listas el primer elemento se considera como 0
#lista = [elemento1, elemento2, elemento3, elemento4, elemento5]
#lista = [0,1,2,3,4]
#---------------------------------------------------------------------------
#Otro tipo de dato compuesto Tuplas, usa ()
#La tupla no se puede modificar
tupla=("Jonathan","Eslava",True,1.65)
print (tupla[0])
#Un elemento de una tupla no puede cambiar
#tupla[0] = "Hola" ERROR
#Para mostrar un elemento siempre se usan los corchetes
#---------------------------------------------------------------------------
#Creando un conjunto set, usa {}
conjunto = {"Jonathan","Eslava",True,1.65}
#No se pueden modificar los elementos del conjunto
#conjunto[0]="Luis" ERROR
#No se muestran los elementos del conjunto por medio de un indice
#No se pueden repetir elementos, no se visualizan
#Para acceder a los elementos del conjunto se puede por medio de un bucle
#---------------------------------------------------------------------------
#Creando un diccionario (dict)
diccionario = {
    'nombre': "Jonathan",
    'edad' : 24,
    'happy' : False,
    'nombre_duplicado' : "Jonathan"
}
#Para ver un elemento del dicionario lo hacemos con el nombre asignado
print(diccionario["edad"])
#En este caso no se hace por medio de indices