n = int(input("Quantos elementos vai ter o vetor? "))
vet = [0 for x in range(n)]
abaixoM = [0 for x in range(n)]

soma = 0
for i in range(0, n):
    vet[i] = float(input("Digite um número: "))
    soma = soma + vet[i]

media = soma/n
print(f"MÉDIA DO VETOR = {media:.3f}")

cont = 0
for i in range(0, n):
    if vet[i] < media:
        abaixoM[cont] = vet[i]
        cont = cont + 1

print("ELEMENTOS ABAIXO DA MÉDIA:")
for i in range(0, cont):
    print(f"{abaixoM[i]:.1f}")