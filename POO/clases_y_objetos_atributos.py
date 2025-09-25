class Celular:
    #Creamos un metodo
    #Cada que se instancia una clase se ejecuta este metodo automaticamente, es decir cuando se crea un objeto se ejecuta el metodo
    #Metodo constructor, self es una forma de hacer referencia a si mismo. al mismo objeto
    def __init__(self, marca, modelo, camara):
        #Definimos las propiedades
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
#Se pasan las propiedades al crear el objeto
celular1 = Celular("Samsumg","S23","48MP")
celular2 = Celular("Iphone","17 pro","58MP")
print(celular1.marca)
print(celular2.marca)