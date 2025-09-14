import tkinter as tk

#Creamos el cuadro donde estaran las luces del semaforo
root = tk.Tk()
root.title("Semaforo")
canvas = tk.Canvas(root, width=200, height=400, bg="black")
canvas.pack()

#Creamos los ovalos que seran las luces roja, amarilla y verde
red_light = canvas.create_oval(50, 50, 150, 150, fill="grey")
yellow_light = canvas.create_oval(50, 160, 150, 260, fill="grey")
green_light = canvas.create_oval(50, 270, 150, 370, fill="grey")

# Función para encender una luz
def turn_on_light(color):
    canvas.itemconfig(red_light, fill="red" if color == "red" else "grey") #Si el color actual es 'red', entonces pinta la luz roja de rojo; si no, píntala de gris (apagada)".
    canvas.itemconfig(yellow_light, fill="yellow" if color == "yellow" else "grey") #Si el color actual es 'yellow', entonces pinta la luz amarilla de amarillo; si no, píntala de gris (apagada)".
    canvas.itemconfig(green_light, fill="green" if color == "green" else "grey") #Si el color actual es 'green', entonces pinta la luz verde de verde; si no, píntala de gris (apagada)".

# Función para cambiar las luces en orden
def traffic_light_sequence():
    turn_on_light("red") #Enciende la luz roja inmediatamente.
    root.after(1000, lambda: turn_on_light("yellow")) #Espera 1000 milisegundos (1 segundo) y luego enciende la luz amarilla.
    root.after(2000, lambda: turn_on_light("green")) #Espera 2 segundos desde el inicio (no desde el amarillo) y enciende la luz verde.
    root.after(3000, traffic_light_sequence) #Después de 3 segundos, vuelve a llamar a sí misma → así la secuencia se repite infinitamente.

# Iniciar la secuencia
traffic_light_sequence()

# Iniciar el bucle principal de la interfaz
root.mainloop() #Se encarga de mostrar la ventana, manejar los eventos (como cerrar la ventana, actualizar la interfaz, etc.)