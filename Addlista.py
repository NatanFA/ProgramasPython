def main():
    notas = []

    n = int(input("Quantas notas gostaria de digitar? "))

    soma = 0
    for i in range(n):
        dado = float(input())
        notas.append(dado)
        soma = soma + dado

    print("A lista é: {} ".format(notas))
    print("A média é: {}".format(soma/n))

    del(notas[1])
    print("A lista com a posição 1 removida é {}".format(notas))

    notas.clear()
    print("A lista com todos os elementos removidos é {}".format(notas))
    
main()
    

    
