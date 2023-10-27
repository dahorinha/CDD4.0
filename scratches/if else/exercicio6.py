he1 = int(input("digite a hora: "))
me1 = int(input("digite o minuto: "))
he2 = int(input("digite a segunda hora: "))
me2 = int(input("digite o segudno minuto: "))
htemp = 0
if he1 > 12:
    he1 = he1-12
if he2 > 12:
    he2 = he2-12
totalmin = me1 + me2
if totalmin >=60:
    totalmin -=60
    htemp = 1
horatotal = he1 + he2 + htemp
if horatotal > 12:
    horatotal = horatotal-12
print(f"a soma é: {horatotal} hrs:{totalmin} minutos ")
