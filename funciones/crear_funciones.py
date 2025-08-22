#Creando una funcion simple
def saludar():
    print("Hola Jonathan, que tal")
    
#Para llamar a la funcion creada solo colocamos
saludar()

#Creando funcion con parametros
def saludo(nombre,sexo):
    sexo = sexo.lower() #Convierte en minusculas
    if(sexo == "mujer"):
        adjetivo = "linda"
        print(f'Hola {nombre}, amiga, que tal {adjetivo}')
    elif(sexo == "hombre"):
        adjetivo = "Genio"
        print(f'Hola {nombre}, amigo, que tal {adjetivo}')
    else:
        adjetivo ="no se que seas"
        print(f'Hola {nombre}, que tal {adjetivo}')
        
saludo("Jadrian", "Hombre")
saludo("Camila", "Mujer")
saludo("Frank", "ni idea")

#Crear una funcion que nos retorne valores
def crea_una_contrasenia_random(num):
    listado_de_caracteres = "abcdefghij"
    numero_entero = str(num) #Convertimos el numero a entero
    num = int(numero_entero[0]) #Toma solo el primer numero que le pasemos por ejemplo pasamos 21 solo toma el 2
    caracter_1 = num -2
    caracter_2 = num
    caracter_3 = num -5
    contrasenia = f'{listado_de_caracteres[caracter_1]}{listado_de_caracteres[caracter_2]}{listado_de_caracteres[caracter_3]}{num*2}'
    #Si queremos que la contrasenia no se muestre al usuario y usarla para otros fines
    #Colocamos return y podemos usar la funcion ahora como un valor
    return contrasenia
       
crea_una_contrasenia_random(98)
#Para obtener el valor de la contrasenia y utilizarla en una variable lo podemos hacer:
password = crea_una_contrasenia_random(98)
print(f'Tu contraenia creada es: {password}')
    