def generador(number):
    lista = [0, 1]
    for i in range (number):
        añadir = lista[-1] + lista [-2]
        lista.append(añadir)
    return lista
print(generador(6))
