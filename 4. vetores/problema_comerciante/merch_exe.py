n = int(input("Serão digitados dados de quantos produtos? "))
nome: [str] = [0 for x in range(n)]
compra: [float] = [0 for x in range(n)]
venda: [float] = [0 for x in range(n)]
lucro: [float] = [0 for x in range(n)]

totalC = 0
totalV = 0
for i in range(0, n):
    print(f"Produto {i+1}:")
    nome[i] = input("Nome: ")
    compra[i] = float(input("Preço de compra: "))
    venda[i] = float(input("Preço de venda: "))
    totalC = totalC + compra[i]
    totalV = totalV + venda[i]

totalLucro = 0
for i in range(0, n):
    lucro[i] = venda[i] - compra[i]
    totalLucro = totalLucro + lucro[i]

perc10 = 0
perc10_20 = 0
perc20 = 0
for i in range(0, n):
    perc = (lucro[i])/compra[i]*100.0
    if perc < 10.0:
        perc10 = perc10 + 1
    elif perc >= 10.0 and perc <= 20.0:
        perc10_20 = perc10_20 + 1
    else:
        perc20 = perc20 + 1

print("RELATÓRIO: ")
print(f"Lucro abaixo de 10%: {perc10}")
print(f"Lucro entre 10% e 20%: {perc10_20}")
print(f"Lucro acima de 20%: {perc20}")
print(f"Valor total de compra: {totalC:.2f}")
print(f"Valor total de venda: {totalV:.2f}")
print(f"Lucro total: {totalLucro:.2f}")