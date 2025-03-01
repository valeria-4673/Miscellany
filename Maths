# e**x

x = int(input("X: "))

def factorial (n):
    result = 1
    for i in range (2, n+1):
        result = i * result
    return result

exponente = 2
suma = 0

while True:
    limitante = x**exponente/factorial(exponente)
    suma += limitante
    exponente += 1
    if limitante < 0.000001:
        break

print(f"e a la {x} es: ", 1+x+suma)

#SERIE 
x = int(input("X: "))

denominadores = []

for i in range (1, x+1):
    if i ==1:
        valor = 1
    elif i % 2 !=0:
        valor = + 1/i
    else:
        valor = - 1/i
    denominadores.append(valor)

suma = 0

for valor in denominadores:
    suma += valor
print(suma)

# ORDER NUMBER WITHOUT METHODS
x = int(input("Cuantos numeros va a ingresar: "))
numeros = []
for i in range (x):
    num = int(input(f"Ingrese num {i+1}: "))
    numeros.append(num)
print("los originales son: ", numeros)

def ordenando (numeros):
    for i in range (len(numeros)-1):
        if numeros [i] >= numeros [i+1]:
            numeros [i], numeros [i+1] = numeros [i+1], numeros [i]

diferencia = -1

while (diferencia < 0):
    for i in range (len(numeros)-1):
        diferencia = numeros [i+1]-numeros [i]
        ordenando(numeros)
print("los ordenados son: ", numeros)
