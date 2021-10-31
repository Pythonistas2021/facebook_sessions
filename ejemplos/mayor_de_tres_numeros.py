print("\tPrograma para determinar el mayor de 3 números")
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

if a > b:
    mayor = a
    if a > c:
        mayor = a
    else:
        mayor = c
else:
    mayor = b
    if b > c:
        mayor = b
    else:
        mayor = c

print(f"El número mayor entre: {a}, {b}, {c} es:", mayor)