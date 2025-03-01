list = []
nums = [i for i in range(4, 1000)]
primos = 2
for num in nums:
    if (num == 1) or (num == 2) or (num == 3):
        pass
    flag = False
    for i in range (2, num):
        if (num % i == 0):
            flag = True
            break
    if not flag:
        primos += 1
        list.append(num)

list.insert(0, 3)
list.insert(0, 2)
print(list)
print(f"hay {primos} primos")

# OTHER PROGRAM PRIME

x = int(input("escriba num: "))
numeros= [i for i in range(2, x)]
for num in numeros:
    if x % num == 0:
        print("No es primo")
        break
    else:
        print("Primo")
        break
