columnas = int(input("Cuantas columnas: "))
matrix_a = []
matrix_b = []
matrix_c = []

for i in range (filas):
    matrix_a.append([])
    matrix_b.append([])
    matrix_c.append([])
    for j in range (columnas):
        matrix_a[i].append(float(input(f"De la matriz A Escriba la celda {i+1}.{j+1}: ")))
        matrix_b[i].append(float(input(f"De la matriz B Escriba la celda {i+1}.{j+1}: ")))
        matrix_c[i].append(matrix_a[i][j]+matrix_a[i][j])
print("La matriz A: ", matrix_a)
print("La matriz B: ", matrix_b)
print("La matriz C: ",matrix_c)
