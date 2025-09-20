#Se dibujara un espiral de colores
import turtle
t = turtle.Turtle()
t.speed(0) #Establecemos la velocidad de dibujo instantanea
turtle.bgcolor("black") #Establecemos el color de fondo de la ventana 
#Se definen los colores que se van a utilizar
colores = ["red","yellow","blue","green","purple","orange"]
#Creamos un bucle que se repetira 200 veces
for i in range(200):
    t.color(colores[i % 6]) #Los colores se repiten en secuencia de 6, lo que permite repetirse cuando se muestran todos
    t.circle(i) #Dibuja un circulo de radio i, los circulos crecen con cada iteracion
    t.left(59) #Después de cada círculo, gira 59 grados a la izquierda.
    
turtle.done() #Finaliza el dibujo y mantiene la ventana abierta hasta que la cierres manualmente.