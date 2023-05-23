def quadrado(a):
    quad = pow(a, 2)
    return quad
def triangulo(a, c):
    triang = (a*b)/2
    return triang
def trapezio(a, b, c):
    trap = ((a+b)*c)/2
    return trap

a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))

quad = quadrado(a)
triang = triangulo(a, b)
trap = trapezio(a, b, c)

print(f"ÁREA DO QUADRADO = {quad:.4f}")
print(f"ÁREA DO TRIÂNGULO = {triang:.4f}")
print(f"ÁREA DO TRAPÉZIO = {trap:.4f}")
