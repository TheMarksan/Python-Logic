n = int(input("Digite o valor de N: "))


for i in range(1, n):
    if n == 0:
        n = 1
    else:
        n = n * i

print(f"FATORIAL = {n}")