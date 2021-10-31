# Para el prime cateto
a = int(input("Ingrese el valor del primer cateto: "))

# Para el segundo cateto
b = int(input("Ingrese el valor del segundo cateto: "))

# Ecuación para determinar la hipotenusa
hipotenusa = (a**2 + b**2)**(1/2)

# Para aproximar a dos cifras decimales
hipotenusa = round(hipotenusa, 2)

# Mostrar el valor de la hipotenusa
print("El valor de la hipotenusa es:", hipotenusa)