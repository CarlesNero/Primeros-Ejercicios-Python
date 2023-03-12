titulo = "Bienvenido al test del queso"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")
puntuacion = 0

opcion = input("Pregunta 1: ¿Que haces cuando ves una tabla de quesos ?\n"
"A - Salgo corriendo \n"
"B - Pruebo alguno\n"
"C - Me lo zampo to\n")

if opcion == "A":
    puntuacion += 0

elif opcion == "B":
        puntuacion += 5

elif opcion == "C":
            puntuacion += 10
else:
    print("Las opciones deben ser A, B o C")
    exit()

opcion = input("Pregunta 2: ¿Como te gusta la hamburguesa?\n"
"A - Sin queso \n"
"B - Con un poco de queso\n"
"C - Mucho queso\n")


if opcion == "A":
    puntuacion += 0

elif opcion == "B":
        puntuacion += 5

elif opcion == "C":
            puntuacion += 10
else:
    print("Las opciones deben ser A, B o C")
    exit()

opcion = input("Pregunta 3: ¿Tienes intolerancia a la lactosa?\n"
"A - Me cago encima \n"
"B - si, pero me la pela\n"
"C - QUEEEESOOOO\n")


if opcion == "A":
    puntuacion += 0

elif opcion == "B":
        puntuacion += 5

elif opcion == "C":
            puntuacion += 10
else:
    print("Las opciones deben ser A, B o C")
    exit()


if puntuacion >= 25:
    print("Tendremos que esconder el queso! tu puntuación es {}!!".format(puntuacion))

elif puntuacion >= 15:
    print("Felicidades fanático de los quesos tu puntuación es {}!!".format(puntuacion))

else:
    print("Tus muertos tu puntuación es {}!!".format(puntuacion))