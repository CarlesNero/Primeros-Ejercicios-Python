import random
titulo = "El laberinto\n"
print( "\n" + titulo + "\n" + "-" * len(titulo) + "\n")

print("Bienvenido al laberinto, en esta historia tendrás que conseguir escapar de un laberinto \n"
      "infestado de animales salvajes, a traves de las diferentes estancias del laberinto tendreis que\n"
      "superar diferentes desafíos y tomar decisiones vitales para el resultado de la historia.\n"
      "Na mas entrar al laberinto te encuentras con 2 caminos\n"
      "\n"
      "A la izquierda un camino con bonitas flores que invita a entrar en el [A]\n"
      "A la derecha un camino que emana un olor a podredumbre [B]\n")

opcion = input("OPCIÓN [A]\n"
               "OPCIÓN [B]")
if opcion == "A":
    print("\n"
          "Escoges el camino mas apetecible, ante ti se abre un camino de flores, con diferentes animales correteando\n"
          "entre ellas, aun que no puedes distinguir que animales son, al fondo puede distinguir dos salidas, \n"
          "una puerta pintada de azul celeste [A] y un portal que parece llevar a una pequeña sala en una torre [B] \n")
    opcion = input("Puerta celeste [A]\n"
                   "Portal desconocido [B]")
    if opcion == "A":
        print("\nTras abrir la puerta, uno de los animales te empuja y ves que, tras la opción que parecía mas segura \n"
              "solo se ve un vacío interminable al que caes hasta morir\n"
              "💀💀FIN💀💀")
        exit()
    elif opcion == "B":
        print("\nDecides entrar en el portal y en menos de lo que esperabas apareces en aquella sala que se percibía \n"
              "desde el exterior, la sala está repleta de libros, pero uno llama tu atención mas que los demas \n"
              "debido a el brillo que emite, LIBRO DE LAS OPERACIONES IMPOSIBLES, es lo que puedes leer en la portada\n"
              "parece un libro mágico que te otorga la capacidad de resolver adivinanzas relacionadas con calculos \n"
              "matemáticos\n")
        libro = False
        opcion = input("¿Coges el libro? [S/N]")
        if opcion == "S":
            libro = True
            print("\n"
                  "Coges el libro y sigues decides bajar por la escalera de la torre, tras un largo rato de bajar, \n"
                  "terminas en una especie de sala del tesoro y ante ti se muestra un Buho con gadas de listillo, \n"
                  "se presenta y te propone un trato, si adivinas el número en el que está pensando sumado al número \n"
                  "de ladrillos de la torre te dará todo el tesoro que encuentras en la sala.\n")
            opcion = input("Aceptas el desafío del Buho? [S/N]")
            if opcion == "S":
                numero_magico_c = random.randint(1, 50) * random.randint(1, 100)
                numero_magico_f = 666
                print("Aceptas el desafío, confías en el poder de el libro que acabas de conseguir, \n"
                      "Abres el libro y aparecen dos números:\n{} [A]\n{} [B]".format(numero_magico_c, numero_magico_f))

                opcion = (input("¿Cual de los números eliges para resolver el acertijo?"))
                if opcion == "A":
                    print("Muy bien listillo, coge todo lo que quiereas y avanza a la siguiente sala\n"
                          "\n"
                          "Continuas andando, la puerta por la que acabas de pasar se cierra de golpe y ante ti se \n"
                          "muestra un dragón enorme que se despierta nada mas sentir tu presencia\n")
                    opcion = input("El dragón es agresivo y empieza a atacarte, intenteas huir pero el único lugar \n"
                                   "por el que parece que puedes escapar está justo detrás del dragón y se trata de\n"
                                   "un agujero que emite una tenue luz.\n"
                                   "\n¿Que opción eliges?\n"
                                   "\nLuchar contra el dragón inutilmente [A]\n"
                                   "Intentar llegar al agujero [B]\n")
                    if opcion == "A":
                        print("\n Luchas contra el dragón no era buena idea, pero eso ya lo sabías al tomar la \n"
                              "decisión, el dragón te chamusca y mueres de forma agónica\n"
                              "💀💀FIN💀💀")
                    elif opcion == "B":
                        print("\n Tratas de llegar por todos los medios posibles al agujero y tras sortear de manera\n"
                              "increible al dragón y sus ataques te cuelas por el agujero...\n"
                              "El agujero resulta ser un pozo de lava en el que caes sin remedio y mueres quemado\n"
                              "💀💀FIN💀💀")

                elif opcion == "B":
                    print("¡¿HAS ESCOGIDO EL NÚMERO DE LA BESTIA!? ¡¿Como lo has sabido!?\n"
                          "Muy bien aventurero, por tu audacia te recompensaré con los tesoros de esta sala y te\n"
                          "devolveré a tu mundo original, disfruta de la recompensa\n"
                          "¡¡¡¡🐉HAS GANADO🐉!!!!")
                    exit()

            else: print("El Buho te mira fijamente y sacude las alas hasta que crea una ráfaga de viento lo\n"
                        "suficientemente fuerte como para estampar tu debil cuerpo contra las paredes hasta\n"
                        "que mueres por la insolencia de rechazar la prueba\n"
                        "💀💀FIN💀💀")

        elif opcion == "N":
            print("\n"
                  "Pasas del libro, no parece importante y sigues decides bajar por la escalera de la torre, tras un\n"
                  "largo rato de bajar, terminas en una especie de sala del tesoro y ante ti se muestra un Buho con\n"
                  "gafas, se presenta y te propone un trato, si adivinas el número en el que está pensando\n"
                  "sumado al número de ladrillos de la torre te dará todo el tesoro que encuentras en la sala.\n")


            opcion = input("Aceptas el desafío del Buho? [S/N]\n")
            if opcion == "S":
                print("\nTe das cuenta de que deberías haber cogido el libro de la sala superior, pero es demasiado\n"
                      "tarde, decides jugartela y adivinar el número\n")
                numero_magico_c = random.randint(1, 10) * random.randint(1, 100)
                opcion = int(input("¿Cual es el número secreto?"))
                if opcion == numero_magico_c:
                    print("Muy bien listillo, coge todo lo que quiereas y avanza a la siguiente sala\n"
                          "\n"
                          "Continuas andando, la puerta por la que acabas de pasar se cierra de golpe y ante ti se \n"
                          "muestra un dragón enorme que se despierta nada mas sentir tu presencia\n")
                    opcion = input("El dragón es agresivo y empieza a atacarte, intenteas huir pero el único lugar \n"
                                   "por el que parece que puedes escapar está justo detrás del dragón y se trata de\n"
                                   "un agujero que emite una tenue luz.\n"
                                   "\n¿Que opción eliges?\n"
                                   "\nLuchar contra el dragón inutilmente [A]\n"
                                   "Intentar llegar al agujero [B]\n")
                    if opcion == "A":
                        print("\n Luchas contra el dragón no era buena idea, pero eso ya lo sabías al tomar la \n"
                              "decisión, el dragón te chamusca y mueres de forma agónica\n"
                              "💀💀FIN💀💀")
                    elif opcion == "B":
                        print("\n Tratas de llegar por todos los medios posibles al agujero y tras sortear de manera\n"
                              "increible al dragón y sus ataques te cuelas por el agujero...\n"
                              "El agujero resulta ser un pozo de lava en el que caes sin remedio y mueres quemado\n"
                              "💀💀FIN💀💀")

                else: print("Fallaste, el número secreto es {} el Buho comienza a sacudirte hasta que acaba contigo\n"
                            "💀💀FIN💀💀".format(numero_magico_c))
                exit()
            else:
                print("El Buho te mira fijamente y sacude las alas hasta que crea una ráfaga de viento lo\n"
                      "suficientemente fuerte como para estampar tu debil cuerpo contra las paredes hasta\n"
                      "que mueres por la insolencia de rechazar la prueba\n"
                      "💀💀FIN💀💀")

if opcion == "B":
    print("Avanzas por un camino tenebroso, lleno de animales con la piel podrida y los ojos de un rojo brillante.\n"
          "Algunos animales intentan atacarte pero están tan débiles que consigues zafarte facilmente de ellos\n"
          "y consigues llegar a lo que parece la salida del laberinto, pero hay algo extraño.\n")
    opcion = input("\nHay algo extraño en la salida del laberinto, decides salir de todas formas ? [S/N]")
    if opcion == "S":
        print("\nTe dispones a dar el primer paso fuera del laberinto, pero en cuanto pones un pie fuera notas que la \n"
              "piel empieza a escocerte, intentas volver atrás pero es demasiado tarde, en cuestión de segundos tu\n"
              "piel empieza a descomponerse y mueres\n"
              "💀💀FIN💀💀")
    elif opcion == "N":
        print("Te quedas en la salida del laberinto pensando que puedes hacer para salir y por otro lugar,\n"
              "a los pocos minutos aparece tras de ti un perro, este se presenta con el nombre de Duna y te plantea \n"
              "un acertijo, si aceptas y lo adivinas promete sacarte de allí de forma segura, de lo contrario\n"
              "se irá para no volver nunca y te dejará allí sin ningún tipo de ayuda.\n")
        opcion = input("\nDuna te plantea la opción del acertijo, ¿Aceptas? [S/N]\n")
        if opcion == "S":
            print("\nHas aceptado y Duna procede a plantearte el acertijo, se trata de una operación básica, con la\n"
                  "dificultad de que tienes que adivinar uno de los números de la misma")
            numero_duna = 2 * 3
            opcion = int(input("Uno de los números es 2 y lo tienes que multiplicar por el número de veces que \n"
                               "sale Duna a pasear al día\n"
                               "\n¿Cual es tu respuesta ante el desafío?"))
            if opcion == numero_duna:
                print("\n¡¡Has acertado!! Duna cumple con su promesa y te saca del laberinto para llevarte a un lugar\n"
                      "seguro\n"
                      "¡¡¡¡🐉HAS GANADO🐉!!!!")
            if opcion != numero_duna:
                print("\n Has fallado, Duna se va, dejandote a tu suerte y terminas por morir al intentar alimentarte\n"
                      "de uno de los animales podridos del laberinto\n"
                      "💀💀FIN💀💀")
        else: print("Duna se retira y te abandona a tu suerte, terminas por morir al intentar alimentarte\n"
                    "de uno de los animales podridos del laberinto\n"
                    "💀💀FIN💀💀")
    else:
        print("\nTerminas por morir al intentar alimentarte\n"
              "de uno de los animales podridos del laberinto fruto de la desesperación\n"
              "💀💀FIN💀💀")
