n = int(input("quantos alunos tem na sala?: "))
alunos_sala = []
for x in range(n):
    alunos_sala.append(input("digite um nome: "))
for i in range (n):
    print(i,alunos_sala[i], i+1)