import math # Para poder usar sqrt()

# Para el valor de a
a = float(input("Digite el valor para a: "))

# Para el valor de b
b = float(input("Digite el valor para b: "))

# Para el valor de c
c = float(input("Digite el valor para c: "))

# Para la primera solución de la ecuación de 2do grado
x1 = (-b + math.sqrt(b**2 -4*a*c))/(2*a)

# Para la segunda solución de la ecuación de 2do grado
x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

print()
# Muestro los valores de x1 y x2
print("La primera solución es:", x1)
print("La segunda solución es:", x2)