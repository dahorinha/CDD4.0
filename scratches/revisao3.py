idade = int(input("digite sua idade: "))
mes = int(input("digite o mes de nascimento: "))
mesatual = int(input("digite o mes atual: "))
ano = 2023-idade
ano2 = ano-1
if mes <= mesatual:
    print(f"nasceu em {ano}")
else:
    print(f"nasceu em {ano2}")