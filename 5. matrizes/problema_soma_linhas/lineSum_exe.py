m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))
mat = [[0 for x in range(n)] for x in range(m)]
vet = [0 for x in range(n)]

for i in range(0, m):
    print(f"Digite os elementos da {i + 1}ª linha:")
    for j in range(0, n):
        mat[i][j] = float(input())

soma = 0
for i in range(0, m):
    for j in range(0, n):
        soma = soma + mat[i][j]
    vet[i] = soma
    soma = 0

print("VETOR GERADO:")
for i in range(m):
    print(f"{vet[i]:.1f}")
