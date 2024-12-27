"""
 Los investigadores de la escuela ECAPMA de la UNAD están desarrollando un estudio para verificar si existe temporada 
 de heladas en sabana de Bogotá y le han solicitado su ayuda para la construcción de un programa que solicite la temperatura 
 de los últimos 20 días. Por cada día se debe validar y mostrar acorde a la temperatura registrada en qué temporada queda clasificado
 Menor o igual a 6 grados => Temporada de heladas
 Mayor a 6 y menor o igual a 11 grados =>Temporada proxima a heladas
 Mayor a 11 grados => No hay temporada de heladas
 
 Al finalizar el registro de todas las temperaturas, se debe mostrar la cantidad de días que registraron temperaturas 
 menores o iguales a 6 grados, la cantidad de días que quedaron en temperaturas entre 7 y 11 y la cantidad de días que quedaron 
 mayores a 11 grados. También debe mostrar el promedio de temperaturas.

"""

contador_heladas = 0
contador_prox_heladas = 0
contador_no_heladas = 0
promedio = 0
contador = 0

for i in range (20):
  temperatura = float(input (f"Digite la temperatura del dia {i+1}: "))
  promedio += temperatura
  contador += 1
  if temperatura <= 6:
      contador_heladas += 1
  elif 6 < temperatura <= 11:
      contador_prox_heladas += 1
  else:
      contador_no_heladas += 1
  
print (f"{contador_heladas} dias se registraron temperaturas menores a 6 grados")
print (f"{contador_prox_heladas} dias se registraron temperaturas entre 7 y 11 grados")
print (f"{contador_no_heladas} dias se registraron temperaturas mayores a 11 grados")
print (f"El promedio de las temperaturas fue: {(promedio/contador)} grados")