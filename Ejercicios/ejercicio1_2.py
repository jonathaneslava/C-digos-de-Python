#Pedir una frase al usuario y calcular cuanto tiempo tardaria en decirla
frase = input("Dime una frase y calculare cuento tiempo tardaras en decirla: ")
#Separamos las palabras por medio de los espacios
palabras_separadas = frase.split(" ")
#Contamos las palabras sin los espacios
cantidad_de_palabras = len(palabras_separadas)
print(f'dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirla')
print(f'Yo lo diria en {cantidad_de_palabras * 100 // 2*1.3 / 100} segundos')

#Si son mas de 120 palabras tardaria mas de un minuto en decirlas y se le manda un aviso
if cantidad_de_palabras > 120:
    print("Son demasiadas palabras para una frase, tardas mas de un minuto en decir esto")