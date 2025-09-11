#Creando funcion que sume dos numeros
def sumar_dos():
    #Esta dentro de un ciclo por si el usuario coloca texto en vez de un numero
    #Si sucede eso entonces se ciclara hasta que el usuario coloque numeros 
    while True: 
        num1 = input("Numero 1: ")
        num2 = input("Numero 2: ")
        #Para usar las excepciones tenemos que hacer uso de try y de exception
        #Try se enfoca en intentar hacer la parte del codigo que posiblemente lance la excepcion
        try:
            resultado = int(num1) + int(num2)
            #break #Si se cumple entonces no se cicla y se termina el ciclo
        except: #Nos muestra el mensaje en dado caso de que encuentre la excepcion
            print("Escribe un numero no un texto")
        else: #Se ejecuta si no se ejecuta el except 
            break 
        finally:
            print("El finally siempre se ejecuta, ya sea que funcione el codigo o se ejecute el except")
    return resultado

print(sumar_dos())