import random
numero = int(input("¿Cual es el número secreto (1 al 10)? "))
numero_secretro = random.randint(1, 10)

if numero != numero_secretro:
    print("¡Has fallado! el número secreto es {}".format(numero_secretro))
else: print("Enhorabuena máquina")