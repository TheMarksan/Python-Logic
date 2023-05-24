n = int(input("Quantos valores vai ter cada vetor? "))
a = [0 for x in range(n)]
b = [0 for x in range(n)]
soma = [0 for x in range(n)]

print("Digite os valores do vetor A:")
for i in range(0, n):
    a[i] = int(input())

print("Digite os valores do vetor B:")
for i in range(0, n):
    b[i] = int(input())

print(f"VETOR RESULTANTE:")
for i in range(0, n):
    soma[i] = a[i] + b[i]
    print(f"{soma[i]}")