proximo = "s"
while proximo == "s":
    n1 = float(input("digite a nota 1: "))
    while n1 > 10 or n1 < 0:
        print ("nota invalida")
        n1 = float(input("digite a nota 1 novamente: "))
    n2 = float(input("digite a nota 2: "))
    while n2 > 10 or n2 < 0:
        print("nota invalida")
        n2 = float(input("digite a nota 2 novamente: "))
    calculo = (n1 + n2) / 2
    print(f"a media é {calculo}")
    proximo = input("deseja continuar? responda com S ou N: ")

