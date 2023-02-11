#Natan Ferreira
#12121EEL016

#Entrada de dados do usuario

N = int(input())

#Operacoes matematicas que resultam no que os usuarios desejam

D = N // 86400
Resto1 = N % 86400
H = Resto1 // 3600
Resto2 = Resto1 % 3600
M = Resto2 // 60
S = Resto2 % 60

#Saida de dados

print(D, "dia(s),", H, "hora(s),", M, "minuto(s) e", S, "segundo(s).")
