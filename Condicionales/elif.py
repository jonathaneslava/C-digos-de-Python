#El if-else en python se escribe como elif
#Ejemplos de if anidados y elif
ingreso_mensual = 72000
gasto_mensual = 71000
#Si la primera condicion no funciona no pasa directamente al else, revisa la otra condicion 
if ingreso_mensual > 10000: #Si el ingreso mensual es mayor a 10000 es verdadero
    print("Estas bien en cualquier parte del mundo")
    if ingreso_mensual-gasto_mensual < 0: #Si la resta es menor a 0 muestra que no alcanza
        print("No alcanza")
    elif ingreso_mensual-gasto_mensual > 3000: #Si la resta es mayor a 3000 muestra que es aceptable
        print("Es aceptable")
    else: #Si no cumple con las dos condiciones anteriores entonces muestra hay que ver si alcanza
        print("Hay que ver si alcanza")
    
elif ingreso_mensual > 1000: #Si el ingreso mensual es mayor a 1000 es verddadero
    print("Estas bien en latinoamerica")
    
elif ingreso_mensual > 500: #Si el ingreso mensual es mayor a 500 es verdadero
    print("Estas bien en Argentina")
    
elif ingreso_mensual > 200: #Si el ingreso mesual es mayor a 200 es verdadero
    print("Estas bien en Venezuela")

#Se pueden colocar varias condiciones antes de caer en un else
else: #Si no se cumplio ninguna de las condiciones anteriores entonces ya muestra el mensaje del else
    print("Bajo sueldo")
