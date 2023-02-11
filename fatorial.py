#Fatorial usando for:

def main():
    n = int(input("Digite o valor de n: "))
    res = fatorial(n)
    print("Fatorial de {} é {}". format(n, res))

def fatorial(n):
    fat = 1
    for i in range(2, n + 1):
        fat = fat * i
    return fat

main()

#Fatorial usando while:

i = 2
fat = 1

n = int(input("Digite o valor de n: "))

while (i <= n):
    fat = fat * i
    i += 1

print("Fatorial de {} é {}". format(n, fat))



