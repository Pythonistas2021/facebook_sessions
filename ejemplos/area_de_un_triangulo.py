# Pedir la base del triángulo
base = float(input("Escriba el valor de la base: "))

# Para la altura
altura = float(input("Escriba la altura: "))

# Para calcular el área de triángulo
area = base*altura/2

# Para trabajar con dos dígitos después del punto decimal
area = round(area,2)

# Para mostrar el área
print("El área es:", area)