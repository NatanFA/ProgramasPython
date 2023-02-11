def main(): #funcao principal
    lista1 = [] #pesos dos itens
    lista2 = [] #valores dos itens
    lista3 = [] #valor/peso
    lista4 = [] #recebe o maior valor da razao valor/peso
    maior = 0 #variavel utilizada para achar o maior valor da lista3
    valorfin = 0 #recebe o valor final da soma dos itens escolhidos para entrarem na mochila
    pesofin = 0 #recebe o peso final da soma dos itens escolhidos para entrarem na mochila
    t = 0 #variaveis utilizadas para os lacos
    z = 0
    j = 0
    itens = int(input()) #recebe a quantidade de itens disponiveis 
    capac = int(input()) #recebe a capacidade maxima da mochila
    for i in range(itens):
        lista1.append(int(input())) #laco para receber cada peso dos itens e agrupa-los em uma lista
    while (j < itens):
        lista2.append(int(input())) ##laco para receber cada valor dos itens e agrupa-los em uma lista
        j+= 1
    for i in range(itens): #laco para colocar na lista3 a razao valor/peso de cada item
        lista3.append((lista2[i])/(lista1[i]))
    valorfin, pesofin = mochila(valorfin, pesofin, t, z, itens, capac, lista1, lista2, lista3, lista4)
    print(valorfin)
    print(pesofin)  #impressao dos valores e pesos finais contidos na mochila

def mochila(valorfin, pesofin, t, z, itens, capac, lista1, lista2, lista3, lista4):
    for k in range(itens):
        for c in range(len(lista3)): #laco que me permite obter o maior valor da lista3, ou seja, que me permite achar a maior razao valor/peso
            if c == 0:
                maior = lista3[c]
                z = c
            else:
                if (maior < lista3[c]):
                    maior = (lista3[c]) #guardo o maior valor/peso na variavel maior
                    z = c    #guardo a posicao do maior valor/peso na variavel z
                else:
                    continue
        lista4.append(lista3[z]) #adiciono na lista4 o maior valor/peso
        del(lista3[z]) #deleto da lista3 o maior valor/peso, porém, exclui o valor uma vez, ou seja, se ha dois valores considerados os maiores que sao iguais, ainda terei um valor considerado como maior
        if(lista4[0] in lista3): #analiso se haviam dois valores iguais e se esses valores eram considerados as maiores razoes de valor/peso
            for a in range(len(lista3)):
                if(lista4[0] == lista3[a]):
                   t = a #ja possuo a posicao de um dos numeros considerados os maiores, e aqui obtenho a posicao do segundo numero tambem considerado como maior
            if(lista1[t] < lista1[z]): #como tenho duas razoes valor/peso consideradas as maiores, para saber qual item devo colocar na mochila, devo encontrar e colocar na mochila o item com menor peso
               if(lista1[t] + pesofin) <= capac: #aqui verifico se o item na posicao t tem o menor peso
                  pesofin = pesofin + lista1[t]
                  valorfin = valorfin + lista2[t] #se t tem o menor peso adiciono o item da posicao t na mochila e somo seu valor e seu peso
                  lista4 = []
                  del(lista2[t]) #aqui deleto tanto o peso quanto o valor do item t nas listas2 e 1 para que assim eu consiga analisar mais facilmente os proximos itens
                  del(lista1[t])
            else:
                if(lista1[z] + pesofin) <= capac: #aqui verifico se o item na posicao z tem o menor peso
                   pesofin = pesofin + lista1[z]
                   valorfin = valorfin + lista2[z] #se z tem o menor peso adiciono o item da posicao z na mochila e somo seu valor e seu peso
                   lista4 = []
                   del(lista1[z]) #aqui deleto tanto o peso quanto o valor do item z nas listas2 e 1 para que assim eu consiga analisar mais facilmente os proximos itens
                   del(lista2[z])
        else: #caso nao exista duas razoes valor/peso iguais, venho direto para ca, pois ja encontrei a maior razao/peso unica
            if (lista1[z] + pesofin) <= capac: #verifico que, caso eu coloque o item na mochila, o peso total nao passe do especificado
                pesofin = pesofin + lista1[z]
                valorfin = valorfin + lista2[z] #somo o peso e o valor do item
                lista4 = []
                del(lista1[z]) #deleto tanto o peso quanto o valor do item para facilitar na analise dos proximos itens
                del(lista2[z])
            else:
                del(lista1[z]) #caso o item analisado, ao ser colocado na mochila, ultrapasse a carga maxima, o item, seu peso e seu valor sao excluidos
                del(lista2[z])
                lista4 = []
                continue
        itens = itens - 1
    return (valorfin, pesofin)
main()
