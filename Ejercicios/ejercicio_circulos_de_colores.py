import turtle, colorsys 
t=turtle.Turtle() #Es con lo que se dibujara en pantalla
turtle.bgcolor("black") #Establecemos el color de fondo
t.speed(0) #Ajusta la velocidad de dibujo, 0 es la mas rapida
#Creamos una lista de colores usando tono, saturacion y valor
colors = [] #Creamos una lista 
for i in range(36):
    rgb = colorsys.hsv_to_rgb(i / 361, 1, 1) #En cada vuelta del bucle, se calcula un color usando el modelo HSV (Hue, Saturation, Value).
    colors.append(rgb) #El resultado rgb (una tupla como (r, g, b)) se agrega a la lista colors.

#Creamos un bucle para generar 36 circulos
for i in range(36):
    t.color(colors[i]) #Se establece el color del borde del circulo 
    t.circle(100) #Dibuja un circulo de radio de 100 pixeles
    t.left(10) #Gira 10 grados a la izquierda para que el nuevo circulo gire con respecto al anterior
    
turtle.done() #Finaliza y mantiene la ventana abierta hasta que el usuario la cierre