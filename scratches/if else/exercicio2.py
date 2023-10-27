nota1 = float(input("digite nota 1: "))
nota2 = float(input("digite nota 2: "))
nota3 = float(input("digite nota 3: "))

if (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10) or (nota3 < 0 or nota3 > 10):
    print ("nota invalida")
else:
    notaf = (nota1 + nota2 + nota3) / 3
    if notaf >= 7:
        print("Aprovado")
    else:
        if notaf >= 4:
            print ("Recuperação")
        else:
            print ("Reprovado")







