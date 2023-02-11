def main():
    n = int(input())
    i = 0
    D2 = 0
    D1 = 0
    D1A = 0
    D2A = 0
                
    while (i < n):
        D1 = D1 + int(input())
        i += 1
        if i == n:
            D2 = 0
            D1A = 0
            break
        D2 = D2 + int(input())
        if (D1 == D2 or D2 > D1):
            D1 = 0
            D1A = 0
            i += 1
        if (D2 < D1):
            D1A = D1 - D2
            D2A = D1A
            D1 = D1 - D2
            D2 = D2 + D1
            D1 = (int(input()) - D1)
            D1A = D1
            i += 1
            c = int(input())
            i += 1
            D2 = D2 + c
            if (D1 > D2):
                D1 = D1 - c
                D1A = D1
                i += 1
                d = int(input())
                D1 = D1 - d
                D2 = D2 + d
                D1A = D1
                i += 1
   
    print("Pessoas completamente imunizadas:", D2)
    print("Pessoas imunizadas apenas com uma dose:", D1)
    print("Pessoas que tomaram a segunda dose com atraso:", D2A)
    print("Pessoas esperando a segunda dose com atraso:", D1A)        
            
main()


        



