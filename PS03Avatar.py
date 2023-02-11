#12121EEL016
#Natan Ferreira Alvarenga
#Entrada de dados pelo teclado

n = input()

#Valores iniciais das variaveis relacionadas ao treinamento do avatar

Ar = 0
Terra = 0
Fogo = 0
Agua = 0

#Operações aritmeticas para descobrirmos os valores finais das variaveis apos os treinamentos de cada elemento

while (n == "A" or n == "F" or n == "W" or n == "E"):
 if (n == "A"):
     t = int(input())
     Ar = Ar + t
     Terra = Terra - (t / 2)
     if (Terra < 0):
         Terra = 0
     n = input()
     
 if (n == "F"):
     t = int(input())
     Fogo = Fogo + t
     Agua = Agua - (t / 2)
     if (Agua < 0):
         Agua = 0
     n = input()
     
 if (n == "E"):
     t = int(input())
     Terra = Terra + t
     Ar = Ar - (t / 2)
     if (Ar < 0):
         Ar = 0
     n = input()
     
 if (n == "W"):
     t = int(input())
     Agua = Agua + t
     Fogo = Fogo - (t / 2)
     if (Fogo < 0):
         Fogo = 0
     n = input()

#Impressão dos valores finais das variaveis    

if (n == "X"):
 print("Pontuacao Final")
 print("Agua: {:.1f}".format(Agua))
 print("Terra: {:.1f}".format(Terra))
 print("Fogo: {:.1f}".format(Fogo))
 print("Ar: {:.1f}".format(Ar))

#Impressao para sabermos se o avatar precisa ou não de mais treinamento

if (Agua == 0 or Fogo == 0 or Terra == 0 or Ar == 0):
 print("Realize mais treinamentos.")
else:
 print("Treinamento realizado com sucesso.")

