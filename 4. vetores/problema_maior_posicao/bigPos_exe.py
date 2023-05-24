n = int(input("Quantos números você vai digitar? "))
vet = [0 for x in range(n)]

maior = vet[0]
for i in range(0, n):
    vet[i] = int(input("Digite um número: "))
    if vet[i] > maior:
        maior = vet[i]
        posMaior = i

print(f"MAIOR VALOR = {maior:.1f}")
print(f"POSIÇÃO DO MAIOR VALOR = {posMaior}")