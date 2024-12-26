"""
Resolver el siguiente ejercicio usando una función: 
Construir una función que permita saber el porcentaje de 
estudiantes que han aprobado un curso. Para esto, la función 
debe recibir como parámetro la cantidad total de estudiantes del 
curso y la cantidad de estudiantes que aprobaron el curso y con 
estos datos, la función debe calcular el porcentaje de aprobación 
del curso.
 
"""

def porcentaje_estudiantes(cantidad_estudiantes,estudiantes_aprobados):
    porcentaje = (estudiantes_aprobados / cantidad_estudiantes)*100
    print ("El porcentaje de estudiantes aprobados es: ", porcentaje, "%" )
    return porcentaje

cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
estudiantes_aprobados = int(input("Ingrese la cantidad de estudiantes aprobados: "))

porcentaje_estudiantes(cantidad_estudiantes,estudiantes_aprobados)
