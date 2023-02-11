def main():
    n = int(input("Digite o fatorial! "))
    k = fatorial(n)
    print("A resposta é: {}".format(k))

def fatorial(n):
    if (n == 0):
        return 1
    else:
        return n * fatorial(n-1)

main()


    
