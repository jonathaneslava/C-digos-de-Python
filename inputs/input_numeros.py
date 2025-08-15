#input es pedirle un dato al usuario y input siempre nos va devolver un texto
numero = input("Escribe un numero: ")

#Multiplicar el numero que escribio el usuario
#Se tiene que convertir a int el numero ya que el dato que esta pasando el usuario es un texto
#Por ejemplo, el usuario escribio 2 y multiplicamos el texto por 2. el resultado es 22, muestra el resultado dos veces
#Si convertimos a numero el dato que escribio el usuario entonces tenemos 2*2 es 4
resultado_int = int(numero)*2
print(resultado_int)
#Si quiero el numero en flotante lo convertimos en flotante
resultado_float = float(numero)*2
print(resultado_float)
