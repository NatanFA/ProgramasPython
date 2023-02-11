#Natan Ferreira Alvarenga
#12121EEL016


#Funcao principal

def main():
    
#Variaveis iniciais
    
    n = int(input())
    i = 0
    D2 = 0
    D1 = 0
    D1A = 0
    D2A = 0

#funcao while para fazermos operacoes aritmeticas com vacinas de varios meses e utilizando dados de meses anteriores
#várias funcoes if para que consigamos satisfazer cada necessidade, por exemplo,
#se o número de pessoas com segunda dose atrasada é maior que zero, devo vacinar essas pessoas primeiro

    while (i < n):
        vac = int(input())
        if (D1A > 0):
            if (vac > D1A):
                D2A = D2A + D1A
                D2 = D2 + D1A
                D1 = vac - D1A
                D1A = 0
                
            if (vac < D1A):
                D2A = D2A + D1A
                D2 = D2 + vac
                D1 = D1 - vac
                D1A = D1
                                
            if (vac == D1A):
                D2A = D2A + D1A
                D2 = D2 + vac
                D1 = 0
                D1A = 0
                
        elif (D1 > 0):
            if (vac > D1):
                D2 = D2 + D1
                D1 = vac - D1
                D1A = D1
                
            if (vac < D1):
                D2 = D2 + vac
                D1 = D1 - vac
                D1A = D1

            if (vac == D1):
                D2 = D2 + D1
                D1 = 0
                D1A = 0
                
        else:
            D1 = D1 + vac

        i += 1

#print dos dados finais
        
    print("Pessoas completamente imunizadas:", D2)
    print("Pessoas imunizadas apenas com uma dose:", D1)
    print("Pessoas que tomaram a segunda dose com atraso:", D2A)
    print("Pessoas esperando a segunda dose com atraso:", D1A)        
            
main()
