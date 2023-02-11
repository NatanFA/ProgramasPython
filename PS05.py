#Natan Ferreira Alvarenga
#12121EEL016

def main(): #funcao main
    sequencia = [] #lista vazia que receberá as senhas do usuário
    b = True #variavel responsavel por manter o while ativo ou o fecha-lo
    a = 0 #variavel utilizada para sabermos se a sequencia é crescente ou nao crescente
    sequencia = [int(i) for i in input().split()] #comando para receber os valores que o usuario deseja adicionar na lista
    while (b):
        for i in range(len(sequencia) - 1): #for utilizado para que, caso o usuario já digite uma senha crescente, eu verifique se a senha realmente é crescente para dar a essa senha o status de correta.
            if (sequencia[i]<sequencia[i+1]):
                a = True
            else:
                a = False
                break
                
        if (a == True): #caso a senha já seja crescente, ou seja, caso o for anterior verifique que a senha digitada já é crescente, imprimo o que se pede
            print("Klift, Kloft, Still, a porta se abriu")
            b = False
        else:
            fun1(sequencia) #caso a senha digitada não seja crescente, mando a lista que contem a senha para a fun1
            for i in range(len(sequencia) - 1): 
                if (sequencia[i]>sequencia[i+1]):
                    a = True
                    break
                else:
                    a = False
            
            if (a == True): #ao retornar a senha, como ela nao possui rotacoes que a transformem em uma senha crescente, imprimo senha incorreta
                print("Senha incorreta") 
                b = False
            else:
                b = False
            
def fun1(sequencia): #fun1 é a funcao responsavel por fazer n quantidades de rotacoes circulares na senha, sendo n o numero de caracteres que a senha tem
                     #caso eu faca as rotacoes e em algum momento encontrd uma senha crescente, imprimo o que se pede, pois a senha esta correta
                     #caso eu faca as n rotacoes e nao encontre senhas crescentes, retorno a senha
    for i in range(len(sequencia)):
        sequencia.append(sequencia[0]) 
        del(sequencia[0])
        for i in range(len(sequencia) - 1):
            if (sequencia[i]<sequencia[i+1]):
                a = True
            else:
                a = False
                break
        if (a == True):
            print("Klift, Kloft, Still, a porta se abriu") 
            break
        else:
            continue
    return sequencia
    
        
main()
