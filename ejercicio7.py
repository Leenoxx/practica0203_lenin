# Escribir un programa que pregunte el correo electrónico
# del usuario en la consola y muestre por pantalla otro
# correo electrónico con el mismo nombre (la parte
# delantera de la arroba @) pero con dominio ceu.es.

correo = str(input("Escribe tu correo electrónico: "))

print(correo[0:correo.find("@")] + "@ceu.es")
