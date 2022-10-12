# Escribir un programa que pregunte por consola por los productos
# de una cesta de la compra, separados por comas, y muestre por
# pantalla cada uno de los productos en una línea distinta.

compra = str(input("Escribe los productos de la compra: "))

print(compra.replace(", ", "\n"))
