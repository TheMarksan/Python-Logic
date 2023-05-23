n = int(input("Quantos números você vai digitar? "))
vet = [0 for x in range(n)]
pares: [int] = [0 for x in range(n)]

cont = 0
for i in range(0, n):
    vet[i] = float(input("Digite um número: "))
    if vet[i] % 2 == 0:
        pares[cont] = vet[i]
        cont = cont + 1

print("NÚMEROS PARES: ")
for i in range(0, cont):
    print(f"{pares[i]:.0f} ", end=" ")

print()
print(f"QUANTIDADE DE PARES = {cont}")