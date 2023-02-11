#Crie uma lista e depois imprima os elementos da lista ao contrário
def main():
    lista = []
    i = 1

    while True:
        n = int(input("Valor de lista{}: ".format(i)))
        if (n == 0):
            break
        else:
            lista.append(n)
        i += 1

    print(lista)

    #método for

    t = len(lista)

    for i in range(t-1, -1, -1):
        print("lista[{}] = {}".format(i, lista[i]))

    print()

    #metodo while

    t = len(lista) - 1
    while (t >= 0):
        print("lista[{}] = {}".format(t, lista[t]))
        t = t - 1

main()
