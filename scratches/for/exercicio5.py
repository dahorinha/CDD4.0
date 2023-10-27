nega = 0
totaln = 0
posi = 0
for n in range(10):
    n = int(input("digite um numero: "))
    if n > 0:
        posi = 1 + posi
    if n < 0:
        nega = 1 + nega
        totaln = n + totaln
        print(f" {n} é negativo: ")
print(f"existem {nega} numeros negativos")
print(f"a soma deles é {totaln}")
print(f"os positivos são {posi}")