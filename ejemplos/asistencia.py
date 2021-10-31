print("\t\tRegistro de asistencia")


lista = ["ejemple@gmail.com",
        7777777, "estafacil"]

value = True
while value:
    usuario = input("Nombres y Apellidos: ")
    ID = int(input("Ingrese su ID: "))
    contraseña = input("Contraseña: ")

    if usurio.upper() != lista[0]:
        print("{} es incorrecto".format(nom_ape))
        value = False

    if ID == lista[1]:
        print("{} es incorrecto".format(ID))
        value = False
    if contraseña != lista[2]:
        print("Su contraseña es incorrecta")
        value = False
    else:
        print("Se registró exitosamente!")
        value = False
