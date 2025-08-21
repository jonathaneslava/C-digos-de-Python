#Ejemplo de bucle con for

#Creamos un conjunto 
animales = {"gato", "perro", "loro","cocodrilo","pez"}
#Se crea el bucle for para recorrer el conjunto de animales
#la variable animal se crea para que tome el valor del elemento de la conjunto cada que se itere
for animal in animales:
    print(f'Ahora la variable animal es: {animal}')
    
#Creamos una nueva conjunto para iterar pero esta vez con numeros
#Queremos que cada elemento en el conjunto sea multiplicado por 2
numeros = {15,20,25,30,35}
#Se crea el bucle
for numero in numeros:
    resultado = numero *2 #La variable numero se multiplica x2 cada que se itera el conjunto
    print(f'El numero en la conjunto es: {resultado}')
    
#Si queremos iterar dos conjuntos al mismo tiempo utilizamos zip
#Para que esto funcione necesitamos que los conjuntos tengan la misma cantidad de elementos
for animal,numero in zip(animales,numeros):
    print(f'Iterando la conjunto de animales: {animal}')
    print(f'Iterando la conjunto de numeros: {numero}')
    
#Para usar range en un for
#Los parametros que solicita es donde comienza y donde termina el bucle aunque el ultimo elemento no se muestra solo es un n-1
for num in range(1,10):
    print(num)
#Si solo le colocamos 1 parametro va comenzar desde cero hasta el numero colocado
for num in range (20):
    print(num)
    
#Forma correcta de recorrer un conjunto con su indice
for anima in enumerate(animales): #Nos da una tupla como resultado (indice, valor)
    indice = anima[0] #Colocar anima[0] nos muesta el indice que tiene la tupla
    valor = anima[1] #Colocar anima[1] nos muesta el valor que tiene la tupla
    print(f'el indice es {indice}, el valor es {valor}')

#Usar for/else se ejecuta el else cuando ya se itero toda el conjunto
for numero in numeros:
    print(f'Valor actual del bucle {numero}')
else:
    print("El bucle termino")