# Escribir un programa que pregunte el nombre de un producto,
# su precio y un número de unidades y muestre por pantalla
# una cadena con el nombre del producto seguido de su
# precio unitario con 6 dígitos enteros y 2 decimales,
# el número de unidades con tres dígitos y el coste total
# con 8 dígitos enteros y 2 decimales.

producto = str(input("Escribe el producto: "))
precio = float(input("Introduce el precio del producto: "))
numero_unidades = int(input("Introduce el número de unidades: "))
total = numero_unidades * precio

print('{} : {:6.2f}€ x {:3d} unidades = {:8.2f}€'.format(producto, precio, numero_unidades, total))
