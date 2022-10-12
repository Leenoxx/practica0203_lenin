# Escribir un programa que pregunte al usuario la fecha de
# su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
# el día, el mes y el año. Adaptar el programa anterior
# para que también funcione cuando el día o el mes
# se introduzcan con un solo carácter.

fecha = str(input("Introduce tú fecha de nacimiento: "))
fecha_dos = fecha[fecha.find("/")+1:]
dia = fecha[:fecha.find("/")]
mes = fecha_dos[:fecha_dos.find("/")]
año = fecha_dos[fecha_dos.find("/")+1:]
print("Día:", dia + "\nMes:", mes + "\nAño:", año)
