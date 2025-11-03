
codigo = input("Ingrese el código del producto: ")
nombre = input("Ingrese el nombre del producto: ")


cantidad = int(input("Ingrese la cantidad del producto: "))
precio_unitario = float(input("Ingrese el precio unitario del producto: "))


subtotal = cantidad * precio_unitario
igv = subtotal * 0.18
total = subtotal + igv


print("\n Detalle del producto ingresado:")
print("Código:", codigo)
print("Nombre:", nombre)
print("Cantidad:", cantidad)
print("Precio unitario: S/", round(precio_unitario, 2))
print("Subtotal: S/", round(subtotal, 2))
print("IGV (18%): S/", round(igv, 2))
print("Total a pagar: S/", round(total, 2))