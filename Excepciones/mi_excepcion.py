#Creamos una excepcion propia
class MiExcepcion:
    def __init__(self,err):
        print(f"Cometiste el siguiente error {err}")
        
#Lanzando mi propia excepcion utilizando raise
#raise MiExcepcion("Esta es mi propia excepcion")
#Manejando mi excepcion
try:
    raise MiExcepcion("Esta es mi propia excepcion en Try")
except:
    print("Cometiste un error")