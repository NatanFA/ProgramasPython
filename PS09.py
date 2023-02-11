#Natan Ferreira Alvarenga
#12121EEL016

def main(): #funcao principal
    linha = [] #inicializacao de variavel que sera utilizada depois como lista
    linha2 = [] #inicializacao de variavel que sera utilizada depois como lista
    matriz1 = [] #inicializacao de variavel que sera utilizada depois como lista
    matriz2 = [] #inicializacao de variavel que sera utilizada depois como lista
    matriz3 = [] #inicializacao de variavel que sera utilizada depois como lista
    matriz4 = [] #inicializacao de variavel que sera utilizada depois como lista
    x = [] #inicializacao de variavel que sera utilizada depois como lista
    y = [] #inicializacao de variavel que sera utilizada depois como lista
    soma = 0 #inicializacao de variavel
    a = 0 #inicializacao de variavel
    for i in range(10): #for utilizado para que a variavel linha receba 10 inputs, e cada input recebido sera adicionado na lista matriz1,
        #o que formara uma matriz (lista de listas), contendo cada linha e coluna do tabuleiro 10x10
        linha = [(x) for x in input().split()]
        matriz1.append(linha)
    for j in range(10): #for utilizado para que eu percorra toda a matriz1, encontrando as posicoes das linhas e das colunas que contem letras,
        #ou seja, encontro a posicao da linha e da coluna que possui algo diferente de um ponto
        #alem disso, armazeno a posicao da linha na lista x e adiciono a posicao da coluna na lista y, e adiciono na lista 3 e 4 qual letra
        #foi encontrada
        for t in range(10):
            if matriz1[j][t] != ".":
                x.append(j)
                y.append(str(t+1))
                matriz3.append(matriz1[j][t])
                matriz4.append(matriz1[j][t])
    x = trocaletra(x) #chamada da funcao trocaletra
    comparacao(x, y, linha2, matriz2, matriz3, matriz4, soma, a) #chamada da funcao comparacao
    
def trocaletra(x): #como podemos ver no enunciado do trabalho dessa semana, o usuario digitara as posicoes na seguinte forma:
    #uma letra e um numeros, os quais fazem referencia a uma posicao do tabuleiro, e eu armazenei as posicoes do tabuleiro
    #que contêm letras nas listas x e y, porem, as posicoes de x foram armazenadas como numeros, e nao como letras, que e a forma
    #que o usuario digitara, entao a funcao trocaletra tem a funcao de trocar cada posicao em formato de numero da lista x, a qual
    #referencia as linhas do tabuleiro para uma respectiva letra do tabuleiro
    for z in range(len(x)):
        if x[z] == 0:
            x[z] = "A"
        if x[z] == 1:
            x[z] = "B"
        if x[z] == 2:
            x[z] = "C"
        if x[z] == 3:
            x[z] = "D"
        if x[z] == 4:
            x[z] = "E"
        if x[z] == 5:
            x[z] = "F"
        if x[z] == 6:
            x[z] = "G"
        if x[z] == 7:
            x[z] = "H"
        if x[z] == 8:
            x[z] = "I"
        if x[z] == 9:
            x[z] = "J"
    return x #retorno a lista x para poder usa-la na funcao comparacao

def comparacao(x, y, linha2, matriz2, matriz3, matriz4, soma, a):            
    p = int(input()) #variavel que recebe quantas tentativas o usuario tera de acertar o navio
    for i in range(p): #for utilizado para que eu adicione na lista vazia linha2 a posicao que o usuario digitou contendo uma letra e um numero
        #que o usuario digitou, de acordo com a quantidade p de tentativas que o usuario tem
        linha2 = [(d) for d in input().split()]
        matriz2.append(linha2) #lista que recebe linha2, ou seja, recebe as posicoes da linha e coluna que o usuario digitou, assim,
        #matriz2 torna-se uma lista de listas
        a = 0 #inicializacao de variavel
        soma = 0 #inicializacao de variavel
        for j in range(len(x)): #for utilizado para que eu percorra as matrizes x e y a cada vez que o usuario utilize uma de suas
            #tentativas, ou seja, como a matriz2 possui a posicao da linha(letra) e da coluna (numero) que o usuario digitou para tentar
            #acertar um navio, eu percorro a matriz2 nas posicoes [i][a] e [i][a+1], e coloco [a+1], pois o usuario sempre digitara
            #2 coisas, a posicao da linha e da coluna, e como mando isso para uma lista de listas, a primeira posicao sera [i] (linha) e [a]
            #sera a coluna, dessa forma, [a+1] referencia a coluna 2 da primeira linha
            if matriz2[i][a] == x[j] and matriz2[i][a+1] == y[j]:
                #if utilizado para que, caso a posicao digitada pelo usuario seja igual a algum par linha e coluna contidos respectivamente
                #na lista x e y, eu entre no if e reproduza os comandos contidos nele
                soma = 1 #variavel que recebe 1 se o par de coordenadas digitas pelo usuario estiver na lista x e y
                matriz3[j] = "#" #todo navio e representado por uma letra, assim, quando um navio e acertado, eu troco a letra
                #daquela posicao na matriz3 por #, pois, assim, quando nao houver mais aquela letra na matriz 3, o navio afundou
                #contudo, a matriz4, a qual continha os mesmos elementros da matriz3, nunca sera alterada, pois assim eu consigo
                #utilizar a letra daquela posicao quando o navio for atingido mais de uma vez naquela mesma posicao
                if matriz4[j] not in matriz3: #if para verificar se aquela letra atingida ainda esta na matriz3, pois, se nao estiver,
                    #todas as posicoes do navio foram acertadas, logo, o navio afundou
                    print("afundou o navio {}".format(matriz4[j]))
                else: #se ainda existir aquela letra na matriz3, significa que o navio foi atingido em uma nova posicao, antes nao atingida
                    print("atingiu o navio {}".format(matriz4[j]))
        if soma == 0: #if utilizado para caso eu nao entre em momento algum no if matriz2[i][a] == x[j] and matriz2[i][a+1] == y[j]:, ou seja
            #como nao entrei no if, nao modifiquei soma para 1, o que significa que ela manteve-se 0, e isso demonstra
            #que a posicao que o usuario digitou nao esta respectivamente nas listas x e y, ou seja, nao possui navio naquela
            #posicao, logo, printo agua
            print("agua")

if (__name__ == "__main__"):
    main()
