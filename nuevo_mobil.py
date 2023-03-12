opcion= input("¿Prefieres un movil:\n"
                "Android (A)"
                "IOS (I)")

if opcion == "A":
    opcion = input("¿Tines dinero? (S/N)")
    if opcion == "S":
        opcion = input("¿Te immporta la camara? (S/N)")
        if opcion == "S":
            print("Deberías comprarte un Google Pixel")
        else: print("Comprate un buen Android Calidad-Precio")
    else: print("Comprate un Android chino de 100€")

elif opcion == "I":
    opcion = input("¿Tines dinero? (S/N)")
    if opcion == "S":
        print("Deberías comprarte el último Iphone Pro Max")
    else: print("Comprate un reacondicionado")





