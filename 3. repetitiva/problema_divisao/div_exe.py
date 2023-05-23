n = int(input("Quantos casos você vai digitar? "))

for i in range(0, n):
    num = float(input("Entre com o numerador: "))
    den = float(input("Entre com o denominador: "))
    if den == 0:
        print("DIVISÃO IMPOSSIVEL")
    else:
        div = num/den
        print(f"DIVISÃO = {div:.2f}")