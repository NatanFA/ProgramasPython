def main():
    lista1 = []
    lista2 = []
    lista3 = []

    for i in range(5):
        dado = int(input("Digite os elementos da lista 1: "))
        lista1.append(dado)

    for i in range(5):
        dado = int(input("Digite os elementos da lista 2: "))
        lista2.append(dado)

    print("A lista 1 é: {}".format(lista1))
    print("A lista 2 é: {}".format(lista2))

    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if (lista1[i] == lista2[j]):
                lista3.append(lista1[i])
    print("A lista 3 é: {}".format(lista3))
                


main()
