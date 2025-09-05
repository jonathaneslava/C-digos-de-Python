#2 listas, una con nombres y una con apellidos
nombres = ["Jonathan","Adrian","Raul","Samuel","Jose"]
apellidos = ["Eslava", "Arroyo", "Martinez", "Hernandez","Rodriguez"]

#Registrar esta informacion en un TXT de forma optima
with open("nombres_y_apellidos.txt","w") as archivo:
    archivo.writelines("Los archivos son: \n")
    #Realizamos un bucle for que agregara los nombres y apellidos en el txt
    [archivo.writelines(f'nombre:{n}\napellido:{a}\n--------------------\n') for n,a in zip(nombres,apellidos)]