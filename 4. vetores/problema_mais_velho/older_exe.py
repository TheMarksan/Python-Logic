n = int(input("Quantos pessoas você vai digitar? "))
nome: [str] = [0 for x in range(n)]
idade: [int] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Dados da {i+1}ª pessoa: ")
    nome[i] = input("Nome: ")
    idade[i] = int(input("Idade: "))

older = idade[0]
for i in range(0, n):
    if idade[i] > older:
        older = idade[i]
        olderName = nome[i]

print(f"PESSOA MAIS VELHA: {olderName}")