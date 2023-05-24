n = int(input("Quantos elementos vai ter o vetor? "))
vet = [0 for x in range(n)]

somaP = 0
contP = 0
for i in range(0, n):
    vet[i] = float(input("Digite um número: "))
    if vet[i]%2 == 0:
        somaP = somaP + vet[i]
        contP = contP + 1

if somaP == 0:
    print("NENHUM NÚMERO PAR")
else:
    mediaP = somaP/contP
    print(f"MÉDIA DOS PARES = {mediaP:.1f}")