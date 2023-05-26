o = int(input("Qual a ordem da matriz? "))
mat = [[0 for x in range(o)] for x in range(o)]

for i in range(0, o):
    for j in range(0, o):
        mat[i][j] = float(input(f"Elemento [{i},{j}]: "))

soma = 0
cont = 0
for i in range(0, o):
    cont = cont + 1
    for j in range(cont, o):
        soma = soma + mat[i][j]

print(f"SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {soma:.0f}")