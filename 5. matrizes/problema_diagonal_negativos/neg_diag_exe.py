o = int(input("Qual a ordem da matriz? "))
mat = [[0 for x in range(o)] for x in range(o)]

for i in range(0, o):
    for j in range(0, o):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("DIAGONAL PRINCIPAL: ")
for i in range(0, o):
    for j in range(0, o):
        if i == j:
            print(f"{mat[i][j]} ", end="")

cont = 0
for i in range(0, o):
    for j in range(0, o):
        if mat[i][j] < 0:
            cont = cont + 1

print()
print(f"QUANTIDADE DE NEGATIVOS = {cont}")