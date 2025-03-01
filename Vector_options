tamaño = int(input("De cuánto el vector? "))
vector = [i for i in range (tamaño)]

def preguntar():
    opcion = int(input("0 para exit. Eliga una opción 1, 2, 3, 4, 5, 6 : "))
    return opcion

opcion = preguntar()
while (opcion != 0 and 1 <= opcion <=6 ):

    if opcion == 1:
        for i in range (tamaño):
            vector[i]= int(input("Escriba el elemento: "))
        print(vector)
        opcion = preguntar()

    elif opcion == 2:
            elimi = int(input("Ponga el numero que quiere eliminar: "))
            no_deleted = []
            for i in range (tamaño):
                if elimi != vector[i]:
                    no_deleted.append(vector[i])
            print(no_deleted)
            opcion = preguntar()

    elif opcion == 3:
         print("Hola mundo")
         opcion = preguntar()

    elif opcion == 4:
         contar = int(input("Qué numero quiere contar "))
         counter = 0
         for i in range (tamaño):
              if contar == vector[i]:
                counter +=1
         print(f"El numero {contar} aparece {counter} veces")
         opcion = preguntar()

    else:
         suma = 0
         for i in range (tamaño):
              suma += vector[i]
         promedio = suma/ tamaño
         print("El promedio es: ", promedio)
         vector.sort()
         print("El maximo es: ", vector[tamaño -1])
         opcion = preguntar()
#Other program

vector = []
answer = int(input("De cuánto el vector? "))
for i in range (answer):
    animal = input("Write number: ")
    vector.append(animal)
buscar = input("Qué busca? ")

for i in range(answer):
    if vector[i] == buscar:
        print(f"El anterior es {vector[i-1]} y el poterior es {vector[i+1]}")
