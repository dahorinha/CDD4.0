continuar = 's'
while continuar == 's':
    nota1 = float(input("digite a nota 1: "))
    nota2 = float(input("digite a nota 2: "))
    media = (nota1 + nota2) / 2
    print(f"a media é: {media}")
    if media >= 7:
        print("aprovado")
    elif media >= 4:
        print("recuperação")
    else:
        print("reprovado")
    continuar = input("deseja continuar?(s/n): ")



