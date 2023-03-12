euro_dollar = 0.91
euro_libra = 1.18


opcion = input("Que transacción quieres realizar? \n"
               "(A) Euro a Dollar\n"
               "(B) Dollar a Euro\n"
               "(C) Euro a Libra\n"
               "(D) Libra a Euro\n")

texto_usuario = "Introduzca la cantidad de {} que desea convertir"

if opcion == "A":
    cantidad = float(input(texto_usuario.format("€")))
    print("Tras la conversión la cantidad será de {} $".format(cantidad / euro_dollar))

elif opcion == "B":
    cantidad = float(input(texto_usuario.format("$")))
    print("Tras la conversión la cantidad será de {} €".format(cantidad * euro_dollar))

elif opcion == "C":
    cantidad = float(input(texto_usuario.format("€")))
    print("Tras la conversión la cantidad será de {} ₤".format(cantidad / euro_libra))

elif opcion == "D":
    cantidad = float(input(texto_usuario.format("₤")))
    print("Tras la conversión la cantidad será de {} €".format(cantidad * euro_libra))

else:
    print("DEBES ELEGIR UNA DIVISA VÁLIDA")