import math

base = float(input("Base do retângulo: "))
altura = float(input("Altura do retãngulo: "))

area = base * altura
perimetro = 2*(base + altura)
diagonal = math.sqrt(pow(base, 2) + pow(altura, 2))

print(f"ÁREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")