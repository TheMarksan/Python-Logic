n = int(input("Quantos pessoas serão digitadas? "))
altura: [float] = [0 for x in range(n)]
genero: [str] = [0 for x in range(n)]

for i in range(0, n):
    altura[i] = float(input(f"Altura da {i+1}ª pessoa: "))
    genero[i] = input(f"Gênero da {i+1}ª pessoa: ")

menor = altura[0]
maior = altura[0]
for i in range(0, n):
    if altura[i] < menor:
        menor = altura[i]
    if altura[i] > maior:
        maior = altura[i]

print(f"Menor altura = {menor:.2f}")
print(f"Maior altura = {maior:.2f}")

somaF = 0
contF = 0
contM = 0
for i in range(0, n):
    if genero[i] == "F":
        somaF = somaF + altura[i]
        contF = contF + 1
    elif genero[i] == "M":
        contM = contM + 1

mediaF = somaF/contF

print(f"Média das alturas das mulheres = {mediaF:.2f}")
print(f"Número de homens = {contM}")