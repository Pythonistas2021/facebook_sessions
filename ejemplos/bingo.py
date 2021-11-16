from datetime import datetime
from random import randint as rd
import pandas as pd
# Para almacenar los datos
datos = {}
lista_nombres = []
lista_cantidad = []
lista_fechas = []
lista_num_series = []
lista_total = []

# Cada información con su respectiva casilla
datos["Nombre"] = lista_nombres
datos["Cantidad"] = lista_cantidad
datos["FechaHora"] = lista_fechas
datos["Num. Serie"] = lista_num_series
datos["Total (S/.)"] = lista_total
# Para salir del bucle
flag = True

while flag:
  # Menú de opciones
  print("\tREGISTRO DE BINGOS")
  print("1. Comprar BINGOS")
  print("2. Visualizar comprar")
  print("3. Configurar información")
  opcion = int(input("Opción: "))
  print()

  if opcion == 1:
    print("COMPRANDO BINGOS")
    nombre = input("Nombre: ")
    dni = input("DNI: ")
    email = input("email: ")
    can_bin = int(input("Cantidad de bingos: "))
    costo = 5*can_bin
    hoy = datetime.today()
    formato_fecha = hoy.strftime("%d/%m/%Y %H:%M")

    print(f"Costo Total S/. {costo}")
    print()

    # Almacenando la imformación
    lista_nombres.append(nombre) 
    
    lista_total.append(costo)
    lista_fechas.append(formato_fecha)
    lista_cantidad.append(can_bin)

    print("Método de pago")
    print("1. VISA")
    print("2. Transferencia BCP")
    print("3. Yape")
    met_pago = int(input("Elege: "))
    print()

    if met_pago == 1:
      print("Compra realizada correctamente")
      print(f"Comprador: {nombre} {dni} {email}")
      print(f"Cantidad de Bingos: {can_bin} Total: S/. {costo} Pagado con: VISA")

    elif met_pago == 2:
      print("Compra realizada correctamente")
      print(f"Comprador: {nombre} {dni} {email}")
      print(f"Cantidad de Bingos: {can_bin} Total: S/. {costo} Pagado con: BCP")

    elif met_pago == 3:
      print("Compra realizada correctamente")
      print(f"Comprador: {nombre} {dni} {email}")
      print(f"Cantidad de Bingos: {can_bin} Total: S/. {costo} Pagado con: Yape")
      
    print(f"Fecha y hora de compra: {formato_fecha}")
    print("\nLos Bingos generados son:")

    num_serie = ""
    for i in range(can_bin):
      num_serie = str(rd(1,75)).rjust(3,'0') + "-" + num_serie
      # Para mostrar los bingos
      print(f"Num serie: {str(rd(1,75)).rjust(3,'0')}")
      print("B\tI\tN\tG\tO")
      print(f"{rd(1,75)}\t{rd(1,75)}\t{rd(1,75)}\t{rd(1,75)}\t{rd(1,75)}")
      print(f"{rd(1,75)}\t{rd(1,75)}\t{rd(1,75)}\t{rd(1,75)}\t{rd(1,75)}")
      print(f"{rd(1,75)}\t{rd(1,75)}\t*\t{rd(1,75)}\t{rd(1,75)}")
      print(f"{rd(1,75)}\t{rd(1,75)}\t{rd(1,75)}\t{rd(0,99)}\t{rd(1,75)}")
      print(f"{rd(1,75)}\t{rd(1,75)}\t{rd(1,75)}\t{rd(1,75)}\t{rd(1,75)}")
      print()
    # Almacenando Cant Num. Serie
    num_serie = num_serie[:len(num_serie)-1]
    lista_num_series.append(num_serie)
  elif opcion == 2:
    print("VISUALIZANDO COMPRAS")
    df = pd.DataFrame(datos, columns=["Nombre", "FechaHora", "Cantidad", "Num. Serie", "Total (S/.)"])
    df.index = range(1, len(df)+1)
    costo_total = df["Total (S/.)"].sum()
    df.loc[len(df.index)+1] = ["Total","","","",costo_total]
    print(df)
    print()
      
  elif opcion == 3:
    print("Información:  BINGO del Asilo San Vicente de Paul")
    print("Fecha:  07 Noviembre 2021")
    print("Hora:  15:00")
    print("Costo S/.: 5")
    print()
  
  print("0. Regresar Menu Principal")
  print("1. Ver Bingos")
  op = input("Opción: ")
  if op == 0:
    break
  elif op == 1:
    print("En proceso")
  print() 
