o = int(input("Qual a ordem da matriz? "))
mat = [[0 for x in range(o)] for x in range(o)]

for i in range(0, o):
    for j in range(0, o):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

maior = mat[0][0]

print("MAIOR ELEMENTO DE CADA LINHA:")
for i in range(0, o):
    for j in range(0, o):
        if mat[i][j] > maior:
            maior = mat[i][j]
    print(f"{maior}")
    maior = 0
