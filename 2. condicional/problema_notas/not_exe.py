a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))

nota = a + b

if nota >= 60.0:
    print(f"NOTA FINAL = {nota:.1f}")
else:
    print(f"NOTA FINAL = {nota:.1f}")
    print("REPROVADO")