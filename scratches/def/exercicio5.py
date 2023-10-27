from biblioteca import *
nome = str(input("qual o produto?: "))
quant= int(input("quantos tem?:"))
valor= float(input("quanto custa?:"))
v= estoque(quant, valor)
print(v)