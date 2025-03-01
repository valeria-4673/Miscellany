filas = int(input("Cuantas filas: "))
columnas = int(input("Cuantas columnas: "))
if (filas != columnas):
    print("NO SIMETRICA")

matrix_a = []

for i in range (filas):
    matrix_a.append([])
    for j in range (columnas):
        matrix_a[i].append(int(input(f"De la matriz A Escriba la celda {i+1}.{j+1}: ")))
print("La matriz A: ", matrix_a)

copia = []
for row in matrix_a:
    copia.append(row[:])
print("La copia es: ", copia)

for i in range (filas):
    for j in range (columnas):
        copia[i][j] = matrix_a [j][i]
print("La traspuesta de A es: ", copia)

diferencia = True
for i in range (filas):
    for j in range (columnas):
        if matrix_a[i][j] != matrix_a[j][i]:
            print("NO SIMETRICA")
            diferencia = False
            break
    if (diferencia == False):
        break
if diferencia:
    print("Es simétrica")
