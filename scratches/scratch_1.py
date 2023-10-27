nimpar= 0
cont= 0
while True:
    if cont %2 != 0:
        print(cont)
        nimpar+=1
    cont+=1
    if nimpar >= 10:
        break