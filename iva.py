"""
Las tiendas “descuéntalo” le han solicitado su ayuda para crear un programa que permita calcular 
el IVA de n productos. Para esto, usted debe solicitar la cantidad del producto, el valor del producto 
y mostrar el valor a pagar incluyendo el IVA. Posterior al cálculo, se debe preguntar al usuario si desea 
registrar otro producto. El ciclo finaliza cuando el usuario responda que no desea registrar más productos.

"""
iva = 1.19
cant_producto =0
valor_producto = 0
resultado =0
bienvenida = int (input ("Bienvenid@ a tiendas descuentalo. \n Ingrese una opcion\n 1. Registrar productos\n 2. Salir del programa \n"))

while bienvenida == 1 :
  decision = int(input("Que operacion desea hacer:\n Presione 1 Calcular precio producto.\n Presione 2 Salir del programa \n"))
  if decision == 1:
    cant_producto = float (input("Ingrese la cantidad de producto que desea adquirir \n"))
    valor_producto = float(input("Ingrese el valor del producto sin puntos ni comas \n"))
    resultado = cant_producto*valor_producto*iva
    print(f"El valor total del producto incluyendo IVA es $ {resultado}")
  else:
    print ("Saliendo del programa...")
    break