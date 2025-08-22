#Encontrando el numero mayor en una lista
numeros = [4,7,1,42,15]
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#Encontrando el numero menor en una lista
numero_menor = min(numeros)
print(numero_menor)

#Redondeando a 6 decimales usando round
#A round le pasamos el numero que queremos redondear y por defecto nos da un numero entero
#Si queremos que nos muestre mas decimales colocamos el numero y la cantidad de decimales
numero = round(12.3456,2)
print(numero)

#Bool, Retornar false -> 0, vacio, false, None / True -> distinto de 0, True, cadena con datos
resultado_bool = bool(0) 
print(resultado_bool)

#All, Retorna True si todos los valores son verdaderos
resultado_all = all([234,"true",[344,23]])
print(resultado_all)

#Sum, Suma los valores de una lista
suma_total = sum(numeros)
print(suma_total)