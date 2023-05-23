q = int(input("Digite a quantidade de minutos: "))

if q > 100:
    v = 50 + ((q-100)*2)
else:
    v = 50

print(f"Valor a pagar: R$ {v:.2f}")