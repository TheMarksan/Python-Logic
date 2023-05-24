n = int(input("Quantos alunos serão digitados? "))
nome: [str] = [0 for x in range(n)]
nota: [float] = [0 for x in range(n)]
nota2: [float] = [0 for x in range(n)]
media: [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Digite nome, primeira e segunda nota do {i+1}º aluno: ")
    nome[i] = input()
    nota[i] = float(input())
    nota2[i] = float(input())
    media[i] = (nota[i] + nota2[i])/2

print("Alunos aprovados: ")
for i in range(0, n):
    if media[i] >= 6.0:
        print(f"{nome[i]}")
