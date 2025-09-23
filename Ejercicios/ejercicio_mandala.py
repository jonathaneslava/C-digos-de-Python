import turtle, colorsys
turtle.bgcolor("black") #Coloca el color de fondo de negro
t=turtle.Turtle() 
t.speed(0) #Se coloca la velocidad con la que se dibujaran los circulos
turtle.colormode(255) #Configura el sistema de color para usar valores RGB de 0 a 255
n=36 #Numero de pasos de color
h=0 #Valor inicial
for i in range(72): #Repite 72 veces para crear una figura simétrica rotada.
    col = colorsys.hsv_to_rgb(h,1,1) #h: cambia en cada iteración (para cambiar el color). s = 1: saturación máxima. v = 1: brillo máximo.
    t.pencolor(int(col[0]*255),int(col[1]*255),int(col[2]*255)) #Asigna el color
    for _ in range(6): t.circle(60); t.left(60) #Dibuja 6 circulos, cada círculo gira 60°, cerrando el ciclo de 360°
    t.left(5); h+=1/n; h%=1 #Gira toda la figura 5° a la izquierda, h para cambiar de color (1/36 por iteración), h %= 1: asegura que el valor se mantenga en el rango [0,1].
    
turtle.done() #Finaliza y mantiene la ventana abierta
        