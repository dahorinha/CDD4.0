from biblioteca import *
repetir = 's'
while repetir == 's':
    operação = str(input("qual operação quer usar? 1(+) 2(-) 3(x) 4(/): "))
    n1 = int(input("digite um numero: "))
    n2= int(input("digite um numero: "))
    n3= int(input("digite um numero: "))
    if operação == '1':
        soma(n1,n2,n3)
    if operação == '2':
        sub(n1,n2,n3)
    if operação == '3':
        mult(n1,n2,n3)
    if operação == '4':
        div(n1,n2,n3)
    repetir = input("quer fazer de novo?(s) ou (n): ")