años = int(input("Cuántos años va a considerar? "))
sucur = int(input("Cuántas sucursales? "))
matrix = []

for i in range (años):
    rows = []
    for j in range (sucur):
        venta = float(input(f"Cuánto vendió en la sucur {j+1} en el año {i+1} "))
        rows.append(venta)
    matrix.append(rows)

for row in matrix:
    print(row)

max = 0
for j in range (sucur):
    suma_sucur = 0
    for i in range (años):
        suma_sucur += matrix [i][j]
        if suma_sucur > max:
            max = suma_sucur
            ganadora = j
    print(f"La sucursal {j+1} vendio en total: ", suma_sucur)
print(f"La sucursal que más vendió fue la {ganadora + 1} con {max} ingresos ")


max_prom = 0
mayor_prom = 0

for i in range (años):
    suma_año= 0
    for j in range (sucur):
        suma_año += matrix [i][j]
    promedio = suma_año/sucur
    if promedio > max_prom:
        max_prom = promedio
        mayor_prom = i
    print(f"El promedio en el año {i +1} es: ", promedio)
print (f"El mayor promedio fue {max_prom} en el año {mayor_prom + 1}")
