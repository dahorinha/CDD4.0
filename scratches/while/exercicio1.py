quant = int(input("quantas notas?: "))
media = 0
q = 1
while q <= quant:
    nota = float(input("digite sua nota: "))
    media = media + nota
    q += 1
calculo = media / quant
print(f"sua media é: {calculo}")

