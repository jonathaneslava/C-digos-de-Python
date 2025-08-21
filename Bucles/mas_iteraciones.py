#Creamos una lista de frutas
frutas = ["platano", "manzana", "uva", "granada", "pera", "fresa"]
#Recorremos la lista de frutas
for fruta in frutas:
    print(f'La fruta que me comere es {fruta}')
    
#Si queremos excluir una fruta de nuestra lista creada podemos usar la sentencia continue
for fruta in frutas:
    if fruta == "fresa": #Cuando la fruta sea fresa continue salta la instruccion evitando que muestre el mensaje
        continue
    print(f'La fruta que me gusta es {fruta}')
    
#Si queremos que el bucle finalize cuando encuentre una fruta en especifico usamos la sentencia break
for fruta in frutas:
    if fruta == "uva": #Si se encuentra uva entonces break termina el bucle
        break
    print(f'La fruta es {fruta}')
else: #Si se coloca un for/else entonces tampoco se ejecuta cuando se coloca un break
    print("Bucle terminado")
    
#Iterar una cadena de texto
cadena = "Hola Jonathan"
for caracter in cadena:
    print(caracter)
    
#Si queremos duplicar las cantidades que tenemos en una lista podemos hacerlo de la sig forma
numeros = [2,4,6,8,10]
#Primero colocamos la operacion que deseamos hacer y despues colocamos el bucle
numeros_multiplicados_por_dos = [x*2 for x in numeros]
print(numeros_multiplicados_por_dos)