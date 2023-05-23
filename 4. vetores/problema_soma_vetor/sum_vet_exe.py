n = int(input("Quantos números você vai digitar? "))
vet = [0 for x in range(n)]

soma = 0
for i in range(0, n):
    vet[i] = float(input("Digite um número: "))
    soma = soma + vet[i]

media = soma/n

print("VALORES = ", end="")
for i in range(0, n):
    print(f"{vet[i]:.1f} ", end="")

print()
print(f"SOMA = {soma:.2f}")
print (f"MÉDIA = {media:.2f}")