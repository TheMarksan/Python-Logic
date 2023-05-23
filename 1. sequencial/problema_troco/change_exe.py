p = float(input("Preço unitário do produto: "))
q = int(input("Quantidade comprada: "))
d = float(input("Dinheiro recebido: "))

v = p*q
troco = d - v

print(f"TROCO = {troco:.2f}")