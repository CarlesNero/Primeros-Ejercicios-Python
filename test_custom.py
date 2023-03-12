titulo = "Bienvenido al test de Duna"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")
puntuacion = 0

opcion = input("¿De que color tiene el pelo Duna?\n"
"Opción A: Yo que se tio\n"
"Opción B: Negro\n"
"Opción C: Marrón claro\n")

if opcion == "A":
    puntuacion += 0

elif opcion == "B":
    puntuacion += 50

elif opcion == "C":
    puntuacion += 100

else:
    print("las opciones son A, B o C tontito")
    exit()

opcion = input("¿Que pide Duna siempre después de la cena?\n"
               "Opción A: Yo que se tio\n"
               "Opción B: Un bistec\n"
               "Opción C: Un premio\n")

if opcion == "A":
    puntuacion += 0

elif opcion == "B":
    puntuacion += 50

elif opcion == "C":
    puntuacion += 100

else:
    print("las opciones son A, B o C tontito")
    exit()

opcion = input("¿En que época del año se cansa antes Duna?\n"
               "Opción A: Yo que se tio\n"
               "Opción B: Invierno\n"
               "Opción C: Verano\n")

if opcion == "A":
    puntuacion += 0

elif opcion == "B":
    puntuacion += 50

elif opcion == "C":
    puntuacion += 100

else:
    print("las opciones son A, B o C tontito")
    exit()

if puntuacion >= 250:
    print("¡¡Máximo conocedor de Duna, tu puntuación es de {}!!🐕‍🦺🐕‍🦺".format(puntuacion))
elif puntuacion >= 150:
    print("Conoces un poco a Duna, tu puntuación es de {}🤩🤩".format(puntuacion))
else:
    print("No tienes ni puta idea, tu puntuación es de {}!!🤬🤬".format(puntuacion))