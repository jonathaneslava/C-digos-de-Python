#Para definir una clase en python se recomienda colocar pascalcase en el nombre
#Las clases nos ayudan a definir como seran las caracteristicas de los objetos que creemos
class Celular():
    #Los atributos son variables que pertenecen a una clase 
    #Atributos estaticos, porque para todos los objetos van a ser iguales
    marca = "Samsumg" #Cada una de las variables es real solo para los objetos celulares
    modelo = "S23"
    camara = "48MP"
    
#Un objeto es una instancia de una clase
celular1 =Celular() #Se crea un objeto
print(celular1.marca) #Accedemos a la marca, se creo el objeto y le preguntamos sus propiedades
print(celular1.modelo) #Accedemos a la modelo, se creo el objeto y le preguntamos sus propiedades
print(celular1.camara) #Accedemos a la camara, se creo el objeto y le preguntamos sus propiedades

#Propiedades de instancia, nosotros las definimos cuando instanciamos una clase