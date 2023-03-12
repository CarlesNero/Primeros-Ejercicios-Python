pregunta = int(input("Dime un número: "))

pregunta2 = int(input("Dime otro número: "))

pregunta3 = int(input("Dime un último número: "))

print("El número mas grande entre {}, {} y {} es {} y el mas pequeño es {}".format(pregunta,pregunta2,pregunta3,
                                                                            max(pregunta, pregunta2, pregunta3),
                                                                            min(pregunta,pregunta2,pregunta3)))
