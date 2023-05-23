p = float(input("Preço unitário do produto: "))
q = int(input("Quantidade comprada: "))
d = float(input("Dinheiro recebido: "))

v = p * q

if d < v:
    rest = v - d
    print(f"DINHEIRO INSUFICIENTE. FALTAM {rest:.2f} REAIS")
else:
    troco = d - v
    print(f"TROCO = {troco:.2f}")