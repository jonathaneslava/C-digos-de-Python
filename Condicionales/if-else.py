#Uso del if-else
edad = 30
#Este bloque se ejecuta si la condicion es verdad
if edad >=18:
    print("Puedes pasar")
    print("Forma parte del if")
#Si la condicion del if no es verdadera se ejecuta else
else:
    print("No puedes pasar")
    print("Forma parte del else")
#Debido a la identacion esto no forma parte del if-else
print("Esta fuera del if-else")   

#------------------------------------------------------------------------------------
contrasenia_amacenada = "Jonathan"
contrasenia_escrita = 'jonathan'
#La contrasenia debe ser escita tal cual ya sea en mayuscula o minuscula
if contrasenia_amacenada == contrasenia_escrita:
    print("Iniciando sesion...")
else:
    print("Contrasenia equivocada, intente de nuevo") 