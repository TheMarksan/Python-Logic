l = float(input("Digite a largura do terreno: "))
c = float(input("Digite o comprimento do terreno: "))
v = float(input("Digite o valor de metro quadrado: "))

area = l*c
p = area*v

print(f"Área do terreno = {area:.2f}")
print(f"Preço do terreno = {p:.2f}")