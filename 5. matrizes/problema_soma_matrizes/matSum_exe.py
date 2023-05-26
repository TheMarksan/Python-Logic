m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))
matA = [[0 for x in range(n)] for x in range(m)]
matB = [[0 for x in range(n)] for x in range(m)]
soma = [[0 for x in range(n)] for x in range(m)]

print(f"Digite os valores da matriz A:")
for i in range(0, m):
    for j in range(0, n):
        matA[i][j] = float(input(f"Elemento [{i},{j}]: "))

print(f"Digite os valores da matriz B:")
for i in range(0, m):
    for j in range(0, n):
        matB[i][j] = float(input(f"Elemento [{i},{j}]: "))

print("MATRIZ SOMA: ")
for i in range(0, m):
    for j in range(0, n):
        soma[i][j] = matA[i][j] + matB[i][j]
        print(f"{soma[i][j]:.0f} ", end=" ")
    print()