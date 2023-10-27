v= [0,0,0,0,0,0,0,0,0,0]
for x in range (10):
    v[x]= int(input("digite um numero: "))
    for y in range (10):
        if v[y]%2 !=0:
            print(f"esses são impar {v[y]}")
        else:
            print(f"esses são par {v[x]}")
        if v[y]<0:
            print(f"esses sao negativos {v[y]}")
        elif v[y]>0:
            print(f"esses sao positivos {v[x]}")
        else:
            print("tem zero otario")
        print()
