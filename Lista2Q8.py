segundos = int(input("Qual o valor em segundos que deseja converter? "))

HH = segundos//3600
resto = segundos%3600
MM = resto//60
SS = resto%60

print(HH, ":", MM, ":", SS, ":")
