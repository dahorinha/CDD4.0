def soma(n1,n2,n3):
    res=n1+n2+n3
    print(res)

def mult(n1,n2,n3):
    res=n1*n2*n3
    print(res)

def sub(n1,n2,n3):
    res=n1-n2-n3
    print(res)
def div(n1,n2,n3):
    res=n1/n2/n3
    print(res)
def coisa(n):
    for x in range (n+1):
        for y in range(1, x + 1):
            print(y, end=" ")
        print()
def contador():
    cont=0
    texto= "o rato roeu a roupa do rei de roma"
    for x in texto:
        if x in "aeiouAEIOU":
            cont+=1
    print(f"o total de vogais é de {cont}")
def estoque(quant, valor):
    calculo = quant * valor
    return calculo

def pnz(numero):
    if numero > 0:
        return("P")
    elif numero < 0:
        return("N")
    else:
        return("Z")
def nota(nota1,nota2):
    notaf= (nota1+nota2)/2
    return notaf

def media(calculo):
    if calculo >= 7:
        print("passou otario!")
    else:
        print("reprovou otario!")