# Para el tamaño del triángulo
# Primer triángulo
n = int(input("Ingrese el tamaño del triángulo: "))

for i in range(n+1):
    print("*"*i)

print()
# Segundo triángulo
for i in range(n, 0, -1):
    print("*"*i)