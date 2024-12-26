"""
Resolver el siguiente ejercicio con listas: 
El profesor Juan ha solicitado su ayuda para calcular el promedio 
de notas de 12 estudiantes. Usted debe construir un programa 
que permita almacenar en una lista la nota de cada estudiante. 
Después de almacenar las 12 notas debe mostrar el promedio 
del grupo. 

"""

notas_estudiantes = []

for i in range(12):
    notas_estudiantes.append(float(input(f"Ingrese la nota del estudiante {i+1}: ")))

promedio = sum(notas_estudiantes) / len(notas_estudiantes)

print ("Las notas del grupo son : ", notas_estudiantes)

print("El promedio del grupo es:", promedio)


