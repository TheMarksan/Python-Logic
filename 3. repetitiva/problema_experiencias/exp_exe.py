n = int(input("Quantas cobaias serão digitadas? "))

somaTotal = 0
somaC = 0
somaR = 0
somaS = 0

for i in range(0, n):
    q = int(input("Quantidade de cobaias: "))
    t = input("Tipo de cobaias: ")
    somaTotal = somaTotal + q
    if t == "C":
        somaC = somaC + q
    elif t == "R":
        somaR = somaR + q
    elif t == "S":
        somaS = somaS + q

percC = (somaC*100)/somaTotal
percR = (somaR*100)/somaTotal
percS = (somaS*100)/somaTotal

print()
print("RELATÓRIO FINAL: ")
print(f"Total = {somaTotal} cobaias")
print(f"Total de coelhos: {somaC}")
print(f"Total de ratos: {somaR}")
print(f"Total de sapos: {somaS}")
print(f"Percentual de coelhos: {percC:.2f}%")
print(f"Percentual de ratos: {percR:.2f}%")
print(f"Percentual de sapos: {percS:.2f}%")