continuar = 's'
while continuar == 's':
    n = int(input("digite um numero: "))
    while n == 0:
        n= int(input("digite novamente: "))
    if n >= 1:
        print("positivo")
    else:
        print("negativo")
    continuar = input('deseja continuar?: ')