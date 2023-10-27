x =1
n1 = float(input("digite um valor: "))
n2 = float(input("digite um valor: "))
while n2 == 0:
    print("numero invalido")
    n2 = float(input("digite novo valor: "))
    x+=1
    if x > 5:
        print("errou demais otario")
        break
else:
    operacao = n1 / x
    print(f"a divisão é: {operacao}")
