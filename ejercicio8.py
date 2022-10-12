# Escribir un programa que pregunte por consola el precio
# de un producto en euros con dos decimales y muestre por
# pantalla el número de euros y el número de céntimos del precio introducido.

precio = str(input("Introduce el precio del producto: "))

print("El precio del producto es", precio[0:precio.find(".")], "euros con",
      precio[precio.find(".")+1:], "céntimos")
