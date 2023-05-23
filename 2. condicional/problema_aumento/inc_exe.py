salario = float(input("Digite o salário da pessoa: "))

if salario <= 1000:
    new = salario * 1.2
    aumento = new - salario
    perc = ((100 * new) / salario) - 100
elif salario > 1000 and salario <= 3000:
    new = salario * 1.15
    aumento = new - salario
    perc = ((100 * new) / salario) - 100

elif salario > 3000 and salario <= 8000:
    new = salario * 1.1
    aumento = new - salario
    perc = ((100 * new) / salario) - 100
else:
    new = salario * 1.05
    aumento = new - salario
    perc = ((100 * new) / salario) - 100

print(f"Novo salário = R$ {new:.2f}")
print(f"Aumento = R$ {aumento:.2f}")
print(f"Porcentagem = {perc:.0f}%")




