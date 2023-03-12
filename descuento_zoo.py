edad = int(input("Digame su edad: "))
tipo_carnet = input("Digame su tipo de carnet(E Estudiante / P Pensionista / F Familia numerosa / N Nada): ")

if (35 <= edad >= 25 and tipo_carnet == "E") or \
        edad <= 10 or \
        (edad > 65 and tipo_carnet == "P") or \
        (tipo_carnet == "F"):
    print("Se te aplica el descuento.")
else:
    print("Te comes una mierda crack")

