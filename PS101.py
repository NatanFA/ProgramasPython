#Natan Ferreira Alvarenga
#12121EEL016

def main():
    linha = []
    linha2 = []
    matriz1 = []
    matriz2 = []
    l = []
    n = int(input())
    for i in range(n):
        linha = input()
        linha = list(linha)
        matriz1.append(linha)
    matriz2 = matriz1[:]
    linha2 = [(x) for x in input().split()]
    i = int(linha2[0])
    j = int(linha2[1])
    trocamatriz1(matriz1, matriz2, i, j)
    trocamatriz2(matriz1, matriz2, i, j)
    trocamatriz3(matriz1, matriz2, i, j)
    trocamatriz4(matriz1, matriz2, i, j)
    for i in range(n):
        l = matriz1[i]
        l = "".join(l)
        print(l)
    
def trocamatriz1(matriz1, matriz2, i, j):
    if (i==len(matriz2)):
        return matriz1, matriz2
    if matriz2[i][j] != "X" and matriz2[i][j] != ".":
        if matriz2[i][j] == "#":
            return matriz1, matriz2
        else:
            matriz1[i][j] = "X"            
    return trocamatriz1(matriz1, matriz2, i+1, j)
def trocamatriz2(matriz1, matriz2, i, j):
    if (j==len(matriz2[0])):
        return matriz1, matriz2
    if matriz2[i][j] != "X" and matriz2[i][j] != ".":
        if matriz2[i][j] == "#":
            return matriz1, matriz2
        else:
            matriz1[i][j] = "X"             
    return trocamatriz2(matriz1, matriz2, i, j+1)
def trocamatriz3(matriz1, matriz2, i, j):
    if (i<0):
        return matriz1, matriz2
    if matriz2[i][j] != "X" and matriz2[i][j] != ".":
        if matriz2[i][j] == "#":
            return matriz1, matriz2
        else:
            matriz1[i][j] = "X"            
    return trocamatriz3(matriz1, matriz2, i-1, j)
def trocamatriz4(matriz1, matriz2, i, j):
    if (j<0):
        return matriz1, matriz2
    if matriz2[i][j] != "X" and matriz2[i][j] != ".":
        if matriz2[i][j] == "#":
            return matriz1, matriz2
        else:
            matriz1[i][j] = "X"              
    return trocamatriz4(matriz1, matriz2, i, j-1) 
main()
