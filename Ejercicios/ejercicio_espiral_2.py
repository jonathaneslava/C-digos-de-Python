import turtle, math, colorsys
t=turtle.Turtle()
t.speed(0) #Velocidad con la que se dibujara 
turtle.bgcolor("black") #Fondo de color negro
turtle.colormode(255) #Es para trabajar con colores RGB en rango de 0–255.

for i in range(300): #Bucle para crear 300 puntos
    color=colorsys.hsv_to_rgb(i/300,1,1) #Genera un color del espectro HSV, cambiando el tono (i/300) gradualmente para que se vea como un arcoiris.
    t.pencolor(int(color[0]*255),int(color[1]*255),int(color[2]*255)) #Convierte HSV a RGB y lo escala a valores entre 0 y 255.
    t.penup() #No dibuje líneas cuando se mueva a una nueva posición.
    r=i*0.5 #Calcula el radio de la espiral en esta iteración.
    t.goto(r*math.cos(i*math.pi/30), r*math.sin(i*math.pi/30)) #calculan la dirección del punto en el círculo.
    t.pendown() #cualquier acción que dibuje (como dot()) tenga efecto.
    t.dot(i%10+5) #Dibuja un punto (dot) en la posición actual.
    
turtle.done() #Termina el dibujo y deja abierta la ventana hasta que el usuario la cierre
