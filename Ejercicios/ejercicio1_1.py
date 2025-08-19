#Ejercicio obtener la diferencia de porcentaje duracion de los cursos en python, en internet
#Promedio de duracion
otros_cursos_min = 2.5 #Curso con duracion 2.5, el mas rapido
otros_cursos_max = 7 #Curso con duracion 7, el mas lento
otros_cursos_promedio = 4 #Curso con duracion 4, cursos promedio
curso_actual = 1.5 #Curso actual 1.5, aprendido de forma independiente 

#Diferencia de duracion
#Se calcula el porcentaje
diferencia_con_min = 100 - curso_actual / otros_cursos_min *100
diferencia_con_max = 100 - curso_actual / otros_cursos_max *100
diferencia_con_promedio = 100 - curso_actual / otros_cursos_promedio *100
print(f"El curso actual dura un {diferencia_con_min}% menos que el curso mas rapido")
print(f"El curso actual dura un {diferencia_con_max}% menos que el curso mas lento")
print(f"El curso actual dura un {diferencia_con_promedio}% menos que el curso promedio")
print("--------------------------------")

#Duracion de videos sin edicion
sin_edicion_promedio = 5
sin_edicion_actual = 3.5

#Porcentaje de tiempo vacio
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // sin_edicion_promedio / 10
tiempo_vacio_actual = 100 - curso_actual * 1000 // sin_edicion_actual / 10

#Diferencia de video removido 
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de video vacio')
print(f'El curso actual elimina un {tiempo_vacio_actual}% de video vacio')
print("--------------------------------")

#Mostrando diferencia si los cursos duraran 10 horas
print(f'Ver 10 horas del curso actual equivale a ver {otros_cursos_promedio * 100 // curso_actual / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {curso_actual * 100 // otros_cursos_promedio / 10} horas de teste curso')

