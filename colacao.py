print("Me voy a la cocina")

print("Abro la nevera")

hay_leche = input("¿Hay leche (S/N) ?")
hay_colacao = input("Hay colacao? (S/N)")

if hay_leche != "S" or hay_colacao != "S":
    print("Al super...")
    if hay_leche != "S":
        print("Compra leche")
    if hay_colacao != "S":
        print("Compra colacao")


if hay_colacao == "S" and hay_leche == "S":
    print("Ponemos la leche en el vaso")
    print("Ponemos el colacao en el vaso")
    print("Mezclamos")


