#Natan Ferreira Alvarenga
#12121EEL016

def main(): #funcao principal
    linha = [] #criacao de lista que sera utilizada depois
    linha2 = [] #criacao de lista que sera utilizada depois
    matriz1 = [] #criacao de lista que sera utilizada depois
    matriz2 = [] #criacao de lista que sera utilizada depois
    l = [] #criacao de lista que sera utilizada depois
    m4 = [] #criacao de lista que sera utilizada depois
    m5 = [] #criacao de lista que sera utilizada depois
    m6 = [] #criacao de lista que sera utilizada depois
    m7 = [] #criacao de lista que sera utilizada depois
    m8 = [] #criacao de lista que sera utilizada depois
    m9 = [] #criacao de lista que sera utilizada depois
    m10 = [] #criacao de lista que sera utilizada depois
    m11 = [] #criacao de lista que sera utilizada depois
    m12 = [] #criacao de lista que sera utilizada depois
    m13 = [] #criacao de lista que sera utilizada depois
    m14 = [] #criacao de lista que sera utilizada depois
    m15 = [] #criacao de lista que sera utilizada depois
    n = int(input()) #input que recebe quantas linhas a matriz teraa
    for i in range(n): #for para adicionar cada linha da matriz
        linha = input()
        linha = list(linha)
        matriz1.append(linha)
    for b in range(len(matriz1)): #for que copia toda a matriz 1 na matriz2 
        matriz2.append(matriz1[b][:])
    linha2 = [(x) for x in input().split()] #input que recebe as coordenadas de onde se inicia a fake news
    i = int(linha2[0]) #variaveis que representarao as linhas e colunas, cada uma, de onde comeca a fake news
    j = int(linha2[1])
    q = int(linha2[0])
    t = int(linha2[1])
    m = (int(matriz2[i][j]))
    k = 0
    #chamada das funcoes
    matriz1, matriz2, m4, m5, m6 = trocamatriz1(matriz1, matriz2, i, j, k, m, q, t, m4, m5, m6) 
    matriz1, matriz2, m7, m8, m9 = trocamatriz2(matriz1, matriz2, i, j, k, m, q, t, m7, m8, m9)
    matriz1, matriz2, m10, m11, m12 = trocamatriz3(matriz1, matriz2, i, j, k, m, q, t, m10, m11, m12)
    matriz1, matriz2, m13, m14, m15 = trocamatriz4(matriz1, matriz2, i, j, k, m, q, t, m13, m14, m15)
    
#aqui, cada while observa se eu ainda tenho numeros nas listas que salvei as posicoes das pessoas contaminadas, pois, como
#como observado abaixo, a cada iteracao eu troco os numeros por ., ou seja, quando nao houver mais ponto, devo parar de
#analisar aquela direcao
    while 1 in m4 or 2 in m4 or 3 in m4 or 4 in m4 or 5 in m4 or 6 in m4 or 7 in m4 or 8 in m4 or 9 in m4:
        if m4 == []: #caso nao haja mais numero, saio do while
            break
        else:
            matriz1, matriz2, m4, m5, m6 = trocamatriz1(matriz1, matriz2, int(m4[k]), int(m5[k]), int(m6[k]), int(m6[k]), int(m4[k]), int(m5[k]), m4, m5, m6)
            #chamada da funcao que analisa no sentido da funcao 1
            m4[k] = "." #troco numero por ponto
            m5[k] = "."
            m6[k] = "."
            k += 1
    k = 0
        
#while similar ao primeiro, mas que gera posicoes compativeis com a funcao 2
    while 1 in m7 or 2 in m7 or 3 in m7 or 4 in m7 or 5 in m7 or 6 in m7 or 7 in m7 or 8 in m7 or 9 in m7:
        if m7 == []:
            break
        else:
            matriz1, matriz2, m7, m8, m9 = trocamatriz2(matriz1, matriz2, int(m7[k]), int(m8[k]), int(m9[k]), int(m9[k]), int(m7[k]), int(m8[k]), m7, m8, m9)
            m7[k] = "."
            m8[k] = "."
            m9[k] = "."
            k += 1
    k = 0
#while similar ao primeiro, mas que gera posicoes compativeis com a funcao 3
    while 1 in m10 or 2 in m10 or 3 in m10 or 4 in m10 or 5 in m10 or 6 in m10 or 7 in m10 or 8 in m10 or 9 in m10:
        if m10 == []:
            break
        else:
            matriz1, matriz2, m10, m11, m12 = trocamatriz3(matriz1, matriz2, int(m10[k]), int(m11[k]), int(m12[k]), int(m12[k]), int(m10[k]), int(m11[k]), m10, m11, m12)
            m10[k] = "."
            m11[k] = "."
            m12[k] = "."
            k += 1
    k = 0
#while similar ao primeiro, mas que gera posicoes compativeis com a funcao 4
    while 1 in m13 or 2 in m13 or 3 in m13 or 4 in m13 or 5 in m13 or 6 in m13 or 7 in m13 or 8 in m13 or 9 in m13:
        if m13 == []:
            break
        else:
            matriz1, matriz2, m13, m14, m15 = trocamatriz4(matriz1, matriz2, int(m13[k]), int(m14[k]), int(m15[k]), int(m15[k]), int(m13[k]), int(m14[k]), m13, m14, m15)
            m13[k] = "."
            m14[k] = "."
            m15[k] = "."
            k += 1
    k = 0
    
    for i in range(n):
        l = matriz1[i]
        l = "".join(l)
        print(l)

#aqui, cada funcao faz a mesma coisa, unica diferenca e que a funcao1 olha as linhas abaixo de onde comeca a fake news
#a 2 olha as colunas a frente da fake news, a 3 olha as linhas acima da fake news e a 4 olhas a coluna anterior à fake news  
def trocamatriz1(matriz1, matriz2, i, j, k, m, q, t, m4, m5, m6):
    if (i==len(matriz2) or i > q+m): #criterio de parada da funcao, para que eu nao continue analisando posicoes que nao existem na lista
        return matriz1, matriz2, m4, m5, m6
    if matriz2[i][j] != ".": #caso a posicao possua um ponto, ja pulo para a proxima posicao
        if matriz2[i][j] == "#": #caso a posicao analisada seja #, nao analiso mais as posicoes daquela direcao
            return matriz1, matriz2, m4, m5, m6
        else:
            if matriz1[i][j] == "X": #caso a posicao possua X, ou seja, uma pessoa ja contaminada, pulo para a proxima posicao
                return trocamatriz1(matriz1, matriz2, i+1, j, k, m, q, t, m4, m5, m6)
            else:
                m4.append(i) #aqui, caso eu encontre um numero, salvo as posicoes das linhas, colunas e qual numero representa a posicao
                m5.append(j)
                m6.append(matriz2[i][j])
                matriz1[i][j] = "X" #troco o numero por X
    return trocamatriz1(matriz1, matriz2, i+1, j, k, m, q, t, m4, m5, m6)
#funcao correspondente a funcao1, mas que analisa posicoes de outras direcoes
def trocamatriz2(matriz1, matriz2, i, j, k, m, q, t, m7, m8, m9):
    if (j==len(matriz2[0]) or j > t+m):
        return matriz1, matriz2, m7, m8, m9
    if matriz2[i][j] != ".":
        if matriz2[i][j] == "#":
            return matriz1, matriz2, m7, m8, m9
        else:
            if matriz1[i][j] == "X":
                return trocamatriz2(matriz1, matriz2, i, j+1, k, m, q, t, m7, m8, m9)
            else:
                m7.append(i)
                m8.append(j)
                m9.append(matriz2[i][j])
                matriz1[i][j] = "X"
    return trocamatriz2(matriz1, matriz2, i, j+1, k, m, q, t, m7, m8, m9)
#funcao correspondente a funcao1, mas que analisa posicoes de outras direcoes
def trocamatriz3(matriz1, matriz2, i, j, k, m, q, t, m10, m11, m12):
    if (i<0 or i < q-m):
        return matriz1, matriz2, m10, m11, m12
    if matriz2[i][j] != ".":
        if matriz2[i][j] == "#":
            return matriz1, matriz2, m10, m11, m12
        else:
            if matriz1[i][j] == "X":
                return trocamatriz3(matriz1, matriz2, i-1, j, k, m, q, t, m10, m11, m12)
            else:
                m10.append(i)
                m11.append(j)
                m12.append(matriz2[i][j])
                matriz1[i][j] = "X"
    return trocamatriz3(matriz1, matriz2, i-1, j, k, m, q, t, m10, m11, m12)
#funcao correspondente a funcao1, mas que analisa posicoes de outras direcoes
def trocamatriz4(matriz1, matriz2, i, j, k, m, q, t, m13, m14, m15):
    if (j<0 or j < t-m):
        return matriz1, matriz2, m13, m14, m15
    if matriz2[i][j] != ".":
        if matriz2[i][j] == "#":
            return matriz1, matriz2, m13, m14, m15
        else:
            if matriz1[i][j] == "X":
                return trocamatriz4(matriz1, matriz2, i, j-1, k, m, q, t, m13, m14, m15) 
            else:
                m13.append(i)
                m14.append(j)
                m15.append(matriz2[i][j])
                matriz1[i][j] = "X"
    return trocamatriz4(matriz1, matriz2, i, j-1, k, m, q, t, m13, m14, m15) 
if __name__ == "__main__":
    main()

