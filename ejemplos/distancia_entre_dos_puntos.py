# Para el primer punto
x1 = float(input("Digite el valor de x1: "))
y1 = float(input("Digite el valor de y1: "))

# Para el segundo punto
x2 = float(input("Digite el valor de x2: "))
y2 = float(input("Digite el valor de y2: "))

# Para la distancia entre los dos puntos
d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Para aproximar a dos cifras decimales
d = round(d, 2)

# Para mostrar el valor de d
print(f"La distancia entre {x1, y1} y {x2, y2} es:", d)