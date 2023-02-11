#Natan Ferreira Alvarenga
#12121EEL016

def main():
    matriz1 = []
    matriz2 = []
    m3 = 0
    lista4 = []
    lista5 = []
    lista6 = []
    soma = 0
    maior = 0
    p = 0
    n = int(input())
    for i in range(n):
        linha1 = [int(x) for x in input().split()]
        matriz1.append(linha1)
    m = int(input())
    for i in range(m):
        linha2 = [int(z) for z in input().split()]
        matriz2.append(linha2)
    for k in range(len(matriz1)-len(matriz2)+1):
        for g in range(len(matriz1[0])-len(matriz2[0])+1):
            for j in range(len(matriz2)):
                for l in range(len(matriz2[0])):
                    if j == 0 and l == 0:
                        lista5.append(j+k)
                        lista6.append(l+g)
                    if matriz2[j][l] == matriz1[j+k][l+g]:
                        soma = soma + 1
                    else:
                        continue
            
            m3 = soma/(m*m)
            lista4.append(m3)
            soma = 0
            m3 = 0
            for a in range(len(lista4)):
                if a == 0:
                    maior = lista4[a]
                    p = a
                else:
                    if maior < lista4[a]:
                        maior = lista4[a]
                        p = a
                    else:
                        continue

            
    print("Posição: ({},{})".format(lista5[p],lista6[p]))
    print("Similaridade máxima: {:.2f}%".format(maior*100))


main()
