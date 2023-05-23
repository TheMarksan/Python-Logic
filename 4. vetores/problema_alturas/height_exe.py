n = int(input("Quantas pessoas serão digitadas? "))
nome: [str] = [0 for x in range(n)]
idade: [int] = [0 for x in range(n)]
altura: [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Dados da {i+1}ª pessoa: ")
    nome[i] = input("Nome: ")
    idade[i] = int(input("Idade: "))
    altura[i] = float(input("Altura: "))

soma = 0
for i in range(0, n):
    soma = soma + altura[i]
media = soma/n
print(f"Altura média: {media:.2f}")

cont = 0
for i in range(0, n):
    if idade[i] < 16:
        cont = cont + 1
perc16 = (cont*100)/n
print(f"Pessoas com menos de 16 anos: {perc16:.1f}%")

for i in range(0, n):
    if idade[i] < 16:
        print(f"{nome[i]}")

