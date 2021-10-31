# Creando un triángulo con números

# Para el tamaño del triángulo
n = int(input("Ingrese el valor máximo del triángulo: "))

# Para el primer número
for i in range(1,n+1):
    for j in range(i):
        print(j+1, end=" ")
    print()
# Para el salto de línea
print()

# Para el segundo triángulo
for i in range(n, 0, -1):
    for j in range(i):
        print(j+1, end=" ")
    print()