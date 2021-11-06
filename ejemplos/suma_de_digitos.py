# Crear una función que calcule la suma de los digitos
# de un número dado


def suma_de_digitos(n):
    acumulador = 0

    n = str(n)
    lista = list(n)

    for elemento in lista:
        acumulador = acumulador + int(elemento)
    
    print(f"La suma de los dígitos de {n} es: {acumulador}")

numero = int(input("Ingrese un número: "))

suma_de_digitos(numero)

