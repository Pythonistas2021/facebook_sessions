# C = K - 273.15
# K = C + 273.15

# Para ingresar la temperatura en Celsius
C = float(input("Escriba la temperatura en Celsius: "))

# Escribir la ecuación de conversión
K = C + 273.15

# Para redonder K
K = round(K,3) 

# Mostramos la conversión
print("La temperatura en Kelvin es:", K)