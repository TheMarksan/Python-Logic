print("Digite dois números: ")
x = int(input())
y = int(input())

if x > y:
    troca = x
    x = y
    y = troca

somaI = 0

for i in range(x+1, y):
    if i%2 != 0:
        somaI = somaI + i


print(f"SOMA DOS IMPARES = {somaI}")