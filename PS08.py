#Natan Ferreira Alvarenga
#12121EEL016

def main(): #funcao principal main
    matriz1 = [] #inicializacao de listas que receberao listas de listas
    matriz2 = [] #inicializacao de listas que receberao listas de listas
    lista4 = [] #lista que recebera os valores de similaridade
    lista5 = [] #lista que recebera as linhas das similaridades
    lista6 = [] #lista que recebera as colunas das similaridades
    soma = 0 #variavel que sera utilizada abaixo
    maior = 0 #variavel que sera utilizada abaixo
    p = 0 #variavel que sera utilizada abaixo
    n = int(input()) #input do numero de linhas e colunas da matriz maior
    for i in range(n): #for utilizada para que eu consiga adicionar as n linhas, uma linha de cada vez
        linha1 = [int(x) for x in input().split()]
        matriz1.append(linha1) #adiciono cada linha digitada do teclado na lista matriz1, assim, formo listas de listas
    m = int(input()) #input do numero de linhas e colunas da matriz menor
    for i in range(m): #for utilizada para que eu consiga adicionar as m linhas, uma linha de cada vez
        linha2 = [int(z) for z in input().split()]
        matriz2.append(linha2) #adiciono cada linha digitada do teclado na lista matriz2, assim, formo listas de listas
    lista5, lista6, p, maior = comparamatriz(matriz1, matriz2, lista4, lista5, lista6, soma, m, p) #chamada da funcao comparamatriz
    print("Posição: ({},{})".format(lista5[p],lista6[p])) #imprime a posicao x,y onde a matriz menor possui maior similaridade com a matriz maior
    print("Similaridade máxima: {:.2f}%".format(maior*100)) #imprime a maior similaridade possivel entre a matriz maior e menor

def comparamatriz(matriz1, matriz2, lista4, lista5, lista6, soma, m, p): #funcao comparamatriz com seus argumentos necessarios para funcionar
    for k in range(len(matriz1)-len(matriz2)+1): #for utilizado para, somado ao for de j, percorrer a matriz maior nas linhas
        for g in range(len(matriz1[0])-len(matriz2[0])+1): #for utilizado para, somado ao for de l, percorrer a matriz maior nas colunas
            for j in range(len(matriz2)): #for utilizado para percorrer as linhas da matriz menor
                for l in range(len(matriz2[0])): #for utilizado para percorrer as colunas da matriz menor
                    if j == 0 and l == 0:
                    #if para que sempre que eu esteja inicializando a varredura nas linhas e colunas da matriz menor eu salve as posicoes de onde
                    #se encontra a varredura da matriz maior 
                        lista5.append(j+k) #adiciono as linhas da matriz maior que são iniciadas junto com o inicio da varredura da lista menor na lista 5
                        lista6.append(l+g) #adiciono as colunas da matriz maior que são iniciadas junto com o inicio da varredura da lista menor na lista 6
                    if matriz2[j][l] == matriz1[j+k][l+g]: #caso as posicoes analisadas na lista maior e menor sejam iguais, somo 1 na variavel soma
                        soma = soma + 1
                    else: #comando para continuar com o for caso o if acima nao seja satisfeito
                        continue
            lista4, p, maior, soma = razaoeposicoes(lista4, soma, m, p) #chamada da funcao razaoeposicoes
    return lista5, lista6, p, maior #retorno da funcao comparamatriz

def razaoeposicoes(lista4, soma, m, p): #funcao razaoeposicoes e seus argumentos
    m3 = 0 #inicializacao de variavel
    maior = 0 #inicializacao de variavel
    m3 = soma/(m*m) #variavel que recebe o valor das similaridades entre as duas matrizes
    lista4.append(m3) #adiciono todas as similaridades entre as matrizes na lista 4
    soma = 0 #reinicio a variavel soma
    m3 = 0 #reinicio a variavel m3
    for a in range(len(lista4)): #for utilizado para eu encontrar, dentro da lista4, o maior valor de similaridade possivel entre as duas matrizes
        if a == 0:
            maior = lista4[a]
            p = a
        else:
            if maior < lista4[a]:
                maior = lista4[a]
                p = a #alem de encontrar o maior valor de similaridade possivel, tambem salvo a posicao da maior similaridade possivel
            else:
                continue
    return lista4, p, maior, soma #retorno da funcao razaoeposicoes
main() #chamada da main
