#Natan Ferreira Alvarenga
#12121EEL016

def main(): #funcao main
    fitaDNA = input() #fita de DNA recebida do teclado
    primer = input() #primer digitado pelo teclado
    primereverso = primer[::-1] #variavel que recebe uma string com os nucleotideos do primer invertidos (de trás pra frente)
    listaprimereverso = list(primereverso) #variavel que transforma a string primereverso em lista, contendo os nucleotidos de trás pra frente
    listaDNA = list(fitaDNA) #variavel que transforma a string fitaDNA em lista
    lista4 = [] #lista que será utilizada para receber as posicoes da fita de DNA que podem ser emparelhadas com o primer
    listaprimereverso = reverse(listaprimereverso) #chamada da funcao reverse
    comparacao(listaDNA, listaprimereverso, lista4) #chamada da funcao comparacao

    #a funcao reverse serve, basicamente, para eu trocar todas as bases existentes na lista contendo o primer invertido
    #ou seja, se tenho A na listaprimereverso, troco a string A por T, pois T é a base nitrogenada que se emparelha com A
    #Assim, tendo diretamente uma lista com as respectivas bases que devem se emparelhar com o primer, consigo comparar mais
    #facilmente a lista contendo o primer com a lista contendo a fita de DNA, pois, se a lista primereverso, contém, na
    #mesma ordem, um primer que se liga corretamente à fita, basta analisarmos se primereverso é igual ao fatiamento da
    #lista contendo o DNA


def reverse(listaprimereverso): #funcao reverse explicada acima
    for i in range(len(listaprimereverso)-1): 
        if listaprimereverso[i+1] == "A":     
            listaprimereverso[i+1] = "T"      
        elif listaprimereverso[i+1] == "T":   
            listaprimereverso[i+1] = "A"      
        elif listaprimereverso[i+1] == "C":   
            listaprimereverso[i+1] = "G"       
        elif listaprimereverso[i+1] == "G":
            listaprimereverso[i+1] = "C"
    return listaprimereverso

def comparacao(listaDNA, listaprimereverso, lista4): #funcao utilizada para verificarmos se a lista contendo o primer reverso é igual ou não a um fatiamento
    #da lista contendo o DNA 
    for i in range(1,len(listaDNA)-1):  #Aqui utilizamos um range que comeca da posicao 1 e vai ate o tamanho da lista-1,
        #para que assim nao analisemos a primeira e a ultima posicao das listas, pois elas nao contem nucleotideos, elas contem apenas 5 e 3
        #Aqui abaixo podemos observar que estamos verificando se a lista contendo o primer e igual a cada fatiamento que podemos fazer com a
        #lista contendo DNA, e esse fatiamento sempre ocorre de acordo com o tamanho do primer, se tenho um primer com 4 nucleotideos, faco
        #um fatimento sempre de 4 posicoes na fita de DNA, contando da primeira posicao para frente e assim por diante
        if listaprimereverso[1:len(listaprimereverso)-1] == listaDNA[i:i+len(listaprimereverso)-2]:                                   
            lista4.append(i) #adiciono a posicao da fita de DNA que pode ser emparelhada com o primer corretamene na lista4            
        else:
            continue
    if lista4 == []:
        print("Nenhuma ligacao") #Agora, caso a lista seja vazia, ou seja, nao ha local na fita de DNA que se emparelhe corretamente
        #com o primer, imprimo nenhuma ligacao
    else:
        for z in range(len(lista4)): #caso exista local na fita que se emparelhe com o primer, ou seja, caso a lista 4 nao seja vazia,
            #imprimo cada uma dessas posicoes com um for
            print("Ligacao na posicao {}".format(lista4[z]))
    return None

main()
