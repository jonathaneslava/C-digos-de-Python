#Operadores logicos

#AND
verdadero_verdadero = True & True #Devuelve True
print(verdadero_verdadero)
falso_verdadero = False & True #Devuelve False
print(falso_verdadero)
verdadero_falso = True & False #Devuelve False
print(verdadero_falso)
falso_falso = False & False #Devuelve False
print(falso_falso)

#OR
verdadero_verdadero = True | True #Devuelve True
print(verdadero_verdadero)
falso_verdadero = False | True #Devuelve True
print(falso_verdadero)
verdadero_falso = True | False #Devuelve True
print(verdadero_falso)
falso_falso = False | False #Devuelve False
print(falso_falso)

#NOT
no_verdadero = not True #Devuelve False
print(no_verdadero)
no_falso = not False #Devuelve True
print(no_falso)

compara = not 1 > 3 #Devuelve true ya que se niega el resultado correcto que es false
print(compara)