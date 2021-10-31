# Concurso de programación

# Para almacenar los datos
lista = []

# Para poder salir del bucle
condicion = True

while condicion:
    print()
    print("\tSobre el concurso")
    print("1. Inscribirse")
    print("2. Mostrar concursantes")
    print("3. Salir")
    print()

    opcion = int(input("Ingrese opción: "))

    if opcion == 1:
        nom_ape = input("Nombres y Apellidos: ")
        lista.append(nom_ape)
        i = 1
    elif opcion == 2:
        for dato in lista:
            print(f"{i}-.{dato}")
            i = i + 1
    else:
        condicion = False