nota = []
soma= 0
for x in range(5):
    nota.append(float(input("digite a nota: ")))
for i in range(5):
    soma = soma+nota[i]
media = soma/5
for v in range(5):
    if nota[v]>=media:
        print(nota[v])


