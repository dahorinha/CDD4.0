senhac = '123'
x = 1
tentativas = 1
senha = (input("digite sua senha: "))
while senha != senhac:
    if x > 2:
        print("maximo de tentativas otario")
        break
    senha = (input(f"senha invalida, vc ainda tem {3-tentativas} tentativas digite novamente: "))
    x += 1
    tentativas += 1
else:
    print("bem vindo gostoso")




