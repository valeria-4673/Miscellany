valor = int(input("De cuánto el vector? "))
vector = []

for i in range(valor):
    num = int(input("Ingrese número: "))
    vector.append(num)
max = 0
descendente = []
for num in vector:
    if num >= max:
       descendente.insert(0, num)
       max = num
    else:
        descendente.append(num)
print(descendente)

# Odd and even 

vector = []
answer = int(input("De cuánto el vector? "))
for i in range (answer):
    num = int(input("Write number: "))
    vector.append(num)

pares = []
impares = []

num_par = 0
num_impar = 0

for i in range(answer):
    if vector[i] % 2 == 0:
        valor = vector [i]
        pares.append(valor)
        num_par += 1
    else:
        valor = vector [i]
        impares.append(valor)
        num_impar += 1


print(f"Ingresó {num_par} numeros pares y {num_impar} numeros impares")
print(pares)
print(impares)
